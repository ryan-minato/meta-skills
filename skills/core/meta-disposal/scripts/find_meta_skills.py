#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""List the skills installed under one or more skill roots, and mark which ones
carry the meta-skill removal marker.

Discovery only. This script never deletes and takes no destructive flag. Removal
is gated on a dry-run a human approves, and a script that could delete would
invite running it instead of the gate. It reports; the agent and the user
decide.

Usage:
    find_meta_skills.py --skill-root .claude/skills
    find_meta_skills.py --skill-root .claude/skills --skill-root .agents/skills
    find_meta_skills.py --skill-root .claude/skills --json

--skill-root is required and repeatable, and has no default. Deletion is scoped
to a project's own skill roots, never a global or user-level one, so a tool this
close to deletion must be told where to look rather than guess.

Exit codes: 0 success (finding nothing is success, not an error), 1 a root could
not be read, 2 bad arguments.
"""

from __future__ import annotations

import argparse
import difflib
import json
import sys
from pathlib import Path

import yaml

# The marker is the contract. A skill is a meta-skill when its *parsed*
# description starts with this exact string — never when its name looks like one.
MARKER = "[META-SKILL: remove after harness setup] "

# How close an opening must be to the marker before it is called a near-miss.
# Real near-misses (a U+00A0, a changed case, a missing trailing space) score
# above 0.82; a description that merely talks about meta-skills scores below
# 0.64. The gap is wide, so this threshold is not delicate.
NEAR_MISS_RATIO = 0.80

# Advisory only, carries no contract: installers rename skills, so this prefix
# proves nothing. It exists to flag "possible meta-skill, marker missing" for a
# human to confirm.
NAME_HINT = "meta-"


def parse_frontmatter(path: Path) -> dict | None:
    """Return SKILL.md's frontmatter mapping, or None if absent or unusable.

    Parse, then test the resolved value. A folded scalar re-wraps lines, so the
    marker may legally span a line break; a regex over the raw text would reject
    a conformant skill and, worse, a recursive grep would match prose that
    merely quotes the marker. Prose has no `description`, so parsing cannot.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None
    return data if isinstance(data, dict) else None


def first_line(description: str) -> str:
    """The description's first line, for the dry-run listing a human reads."""
    return " ".join(description.split())[:100]


def near_miss(description: str) -> str:
    """Describe how a marker-lookalike differs from the marker, or "".

    A near-miss is worse than no marker at all: cleanup skips the skill while
    its author believes it is marked, so it lives in the project forever. The
    difference is usually a U+00A0, a smart quote, or a changed case — all
    invisible on screen, which is exactly why this reports codepoints rather
    than showing the string and letting a human "look" at it.

    The test is whether the *opening* is almost the marker, measured by
    similarity — not whether the description mentions meta-skills somewhere.
    Merely looking for the words flags any skill whose job is to talk about
    meta-skills, and a listing that cries wolf over a skill nobody was going to
    delete is how cleanup starts being frightening. Real near-misses score well
    above this threshold; descriptions that merely discuss the subject score far
    below it.
    """
    if description.startswith(MARKER):
        return ""
    opening = description[: len(MARKER)]
    if difflib.SequenceMatcher(None, MARKER, opening).ratio() < NEAR_MISS_RATIO:
        return ""
    for i, (want, got) in enumerate(zip(MARKER, description)):
        if want != got:
            return (
                f"looks marked but is not: at character {i}, "
                f"expected U+{ord(want):04X} but found U+{ord(got):04X}"
            )
    if len(description) < len(MARKER):
        return "looks marked but is not: the description is shorter than the marker"
    return "looks marked but is not: no codepoint difference found"


def scan_root(root: Path) -> list[dict]:
    """Every <root>/<name>/SKILL.md, at depth 2 exactly.

    Depth 2 and no deeper: the disposal procedure may only ever assume
    <root>/<name>/SKILL.md, and walking further would reach into a skill's own
    bundled files or through a symlink into a shared install.
    """
    records: list[dict] = []
    root_resolved = root.resolve()

    for child in sorted(root.iterdir()):
        # Symlinks are tested first, before is_dir(). is_dir() follows the link,
        # so a symlink that dangles or points at a file would be dropped by the
        # is_dir() check below and never reported at all — and a candidate that
        # silently vanishes from a deletion listing is the one failure this
        # script must not have.
        #
        # A symlinked skill is reported, never followed. Recursing through it
        # would leave the project and reach a shared or global install, where
        # deleting is never in scope.
        if child.is_symlink():
            try:
                target = str(child.readlink())
            except OSError:
                target = "(unreadable)"
            resolves = child.exists()
            records.append(
                {
                    "root": str(root),
                    "name": child.name,
                    "path": str(child),
                    "symlink": True,
                    "symlink_target": target,
                    "marker": False,
                    "description": "",
                    "name_hint": child.name.startswith(NAME_HINT),
                    "note": (
                        f"symlink -> {target}"
                        + ("" if resolves else " (dangling)")
                        + "; unlink only, never recurse. Confirm by hand."
                    ),
                }
            )
            continue

        if not child.is_dir():
            continue

        # Containment: the resolved directory must still sit under the root.
        try:
            child.resolve().relative_to(root_resolved)
        except ValueError:
            records.append(
                {
                    "root": str(root),
                    "name": child.name,
                    "path": str(child),
                    "symlink": False,
                    "marker": False,
                    "description": "",
                    "name_hint": child.name.startswith(NAME_HINT),
                    "note": "resolves outside the skill root; out of scope",
                }
            )
            continue

        skill_md = child / "SKILL.md"
        if not skill_md.is_file():
            continue

        data = parse_frontmatter(skill_md)
        description = ""
        if data is not None:
            value = data.get("description")
            if isinstance(value, str):
                description = value

        divergence = near_miss(description)
        records.append(
            {
                "root": str(root),
                "name": child.name,
                "path": str(child),
                "symlink": False,
                "marker": description.startswith(MARKER),
                "near_miss": divergence,
                "description": first_line(description),
                "name_hint": child.name.startswith(NAME_HINT),
                "note": divergence,
            }
        )

    return records


def render_table(records: list[dict]) -> str:
    if not records:
        return "No skills found. Nothing to do."

    lines = []
    width = max(len(r["name"]) for r in records)
    for record in records:
        if record["marker"]:
            status = "MARKED"
        elif record["symlink"]:
            status = "SYMLINK"
        elif record.get("near_miss"):
            status = "NEAR-MISS"
        elif record["name_hint"]:
            status = "hint?"
        else:
            status = "-"
        detail = record["note"] or record["description"] or "(no description)"
        lines.append(f"  {status:<9} {record['name']:<{width}}  {detail}")

    marked = sum(1 for r in records if r["marker"])
    misses = sum(1 for r in records if r.get("near_miss"))
    links = sum(1 for r in records if r["symlink"])
    hints = sum(
        1
        for r in records
        if r["name_hint"] and not r["marker"] and not r.get("near_miss")
    )

    lines.append("")
    lines.append(f"  {marked} marked, {len(records)} scanned.")
    lines.append("")
    lines.append("  MARKED     description begins with the marker -> a meta-skill.")
    if misses:
        lines.append(
            "  NEAR-MISS  description ALMOST matches the marker. Cleanup will not"
        )
        lines.append(
            "             find it and its author believes it is marked. Do not"
        )
        lines.append("             judge this by eye — the difference is invisible.")
    if links:
        lines.append("  SYMLINK    reported, never followed. Unlink only.")
    if hints:
        lines.append("  hint?      named meta-* but unmarked -> confirm with a human;")
        lines.append("             the name carries no contract, and may be chance.")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        prog="find_meta_skills.py",
        description="List installed skills and mark the meta-skills. Never deletes.",
    )
    parser.add_argument(
        "--skill-root",
        action="append",
        required=True,
        metavar="PATH",
        help="A project skill root to scan. Repeatable. No default, by design.",
    )
    parser.add_argument(
        "--json", action="store_true", help="Emit JSON instead of a table."
    )
    args = parser.parse_args(argv)

    records: list[dict] = []
    for raw in args.skill_root:
        root = Path(raw)
        if not root.is_dir():
            print(f"error: not a directory: {root}", file=sys.stderr)
            return 1
        records.extend(scan_root(root))

    if args.json:
        print(json.dumps(records, indent=2))
    else:
        print(render_table(records))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
