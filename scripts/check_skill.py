#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Check one skill: its file structure, its SKILL.md, and its links.

Errors are hard rules; warnings are recommendations and never fail the run.
Every message states what failed, why it matters, and how to fix it.

Usage:
    check_skill.py <skill-dir> [<skill-dir> ...]
    check_skill.py --all          every published skill under skills/
    check_skill.py --selftest     assert the checks themselves still fire

Exit codes: 0 clean or warnings only, 1 error found, 2 bad arguments.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SKILLS = REPO / "skills"
INTERNAL_SKILLS = REPO / ".agents" / "skills"

# Keep in sync with .agents/knowledge/meta-skill-contract.md (source of truth),
# the Core Conventions line in AGENTS.md, and MARKER in validate_repo.py.
# The contract-sync skill owns that alignment.
MARKER = "[META-SKILL: remove after harness setup] "

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
NAME_MAX = 64
DESCRIPTION_MAX = 1024
DESCRIPTION_WARN = 900
BODY_WARN_LINES = 500

ALLOWED_DIRS = {"references", "scripts", "assets"}
LINKED_DIRS = ("references", "scripts")

# Standard markdown links: [text](target). Not images, not reference links.
LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE_RE = re.compile(r"^[ \t]*(`{3,}|~{3,}).*?^[ \t]*\1", re.MULTILINE | re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, location: str, reason: str, why: str, fix: str) -> None:
        self.errors.append(_render("ERROR", location, reason, why, fix))

    def warn(self, location: str, reason: str, why: str, fix: str) -> None:
        self.warnings.append(_render("WARNING", location, reason, why, fix))


def _render(level: str, location: str, reason: str, why: str, fix: str) -> str:
    return (
        f"{level}  [{location}]\n  Reason: {reason}\n  Why:    {why}\n  Fix:    {fix}"
    )


def strip_code(text: str) -> str:
    """Blank out fenced blocks and inline code so links inside them never match.

    Newlines are preserved so line numbers stay meaningful.
    """

    def blank(match: re.Match[str]) -> str:
        return re.sub(r"[^\n]", " ", match.group(0))

    return INLINE_CODE_RE.sub(blank, FENCE_RE.sub(blank, text))


def parse_frontmatter(text: str) -> tuple[dict | None, str]:
    """Return (frontmatter mapping, reason-if-unusable).

    Parse-then-check: a folded scalar re-wraps lines, so the marker may legally
    span a line break. Only the resolved value can be tested.
    """
    if not text.startswith("---\n"):
        return None, "SKILL.md does not begin with YAML frontmatter at byte 0."
    end = text.find("\n---", 3)
    if end == -1:
        return None, "the YAML frontmatter is never closed by a '---' line."
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        first = str(exc).splitlines()[0] if str(exc) else exc.__class__.__name__
        return None, f"the YAML frontmatter does not parse ({first})."
    if not isinstance(data, dict):
        return None, "the YAML frontmatter is not a mapping."
    return data, ""


def codepoint_diff(actual: str) -> str:
    """Show where a near-miss marker first diverges, by codepoint."""
    for i, (want, got) in enumerate(zip(MARKER, actual)):
        if want == got:
            continue
        return (
            f"            expected: {MARKER[:i]!s}<U+{ord(want):04X} {unicodedata.name(want, '?')}>\n"
            f"            actual:   {actual[:i]!s}<U+{ord(got):04X} {unicodedata.name(got, '?')}>\n"
            f"            first difference at character {i}"
        )
    if len(actual) < len(MARKER):
        missing = MARKER[len(actual)]
        return (
            f"            the value ends after {len(actual)} characters; "
            f"expected <U+{ord(missing):04X} {unicodedata.name(missing, '?')}> next"
        )
    return "            (no codepoint difference found)"


def check_structure(skill: Path, report: Report) -> None:
    name = skill.name
    for entry in sorted(skill.iterdir()):
        if entry.name == "SKILL.md":
            continue
        if entry.is_dir() and entry.name in ALLOWED_DIRS:
            continue
        if entry.name == "README.md":
            report.warn(
                f"{name}/README.md",
                "a skill root contains README.md.",
                "Keeping a README in a skill root is discouraged: the whole "
                "directory ships into target projects, so the file costs context "
                "in every install while serving a browsing audience the installed "
                "copy never has. The catalog README is where a skill is described.",
                "Move the content to the catalog's README.md and delete this file.",
            )
            continue
        kind = "directory" if entry.is_dir() else "file"
        report.warn(
            f"{name}/{entry.name}",
            f"unexpected {kind} in the skill root.",
            "A skill root is expected to hold SKILL.md plus the directories "
            "references/, scripts/, and assets/. Anything else ships to every "
            "target project too, and is usually a stray file rather than a "
            "deliberate one.",
            "Move it into references/, scripts/, or assets/, or delete it.",
        )


def check_skill_md(skill: Path, report: Report, published: bool) -> dict | None:
    path = skill / "SKILL.md"
    name = skill.name
    if not path.is_file():
        report.error(
            f"{name}/SKILL.md",
            "the skill has no SKILL.md.",
            "SKILL.md is the skill: without it there is nothing to load.",
            f"Create {name}/SKILL.md with YAML frontmatter and a body.",
        )
        return None

    text = path.read_text(encoding="utf-8")
    data, reason = parse_frontmatter(text)
    if data is None:
        report.error(
            f"{name}/SKILL.md:frontmatter",
            reason,
            "Frontmatter carries the name and description. Unparseable "
            "frontmatter means the skill cannot be loaded or identified at all. "
            "Note a plain scalar starting with '[' is invalid YAML: '[' opens a "
            "flow sequence.",
            "Open the file with 'description: >' as a folded block scalar and "
            "ensure the frontmatter is a mapping closed by a '---' line.",
        )
        return None

    _check_name(data, name, report)
    _check_description(data, name, report, published)
    _check_body_size(text, name, report)
    return data


def _check_name(data: dict, name: str, report: Report) -> None:
    value = data.get("name")
    if not isinstance(value, str) or not value:
        report.error(
            f"{name}/SKILL.md:frontmatter:name",
            "'name' is missing or is not a string.",
            "The name identifies the skill to the runtime.",
            f"Add: name: {name}",
        )
        return
    if value != name:
        report.error(
            f"{name}/SKILL.md:frontmatter:name",
            f"'name' is '{value}' but the directory is '{name}'.",
            "The runtime resolves a skill by directory; a mismatched name makes "
            "the skill load under one identity and be referred to by another.",
            f"Set name: {name}, or rename the directory to '{value}'.",
        )
    if not NAME_RE.match(value):
        report.error(
            f"{name}/SKILL.md:frontmatter:name",
            f"'name' ('{value}') is not kebab-case.",
            "The spec requires lowercase alphanumerics separated by single hyphens.",
            "Use lowercase letters, digits, and single hyphens only.",
        )
    if len(value) > NAME_MAX:
        report.error(
            f"{name}/SKILL.md:frontmatter:name",
            f"'name' is {len(value)} characters (limit {NAME_MAX}).",
            "The spec caps the name length.",
            f"Shorten the name to at most {NAME_MAX} characters.",
        )


def _check_description(data: dict, name: str, report: Report, published: bool) -> None:
    location = f"{name}/SKILL.md:frontmatter:description"
    value = data.get("description")
    if not isinstance(value, str) or not value.strip():
        report.error(
            location,
            "'description' is missing or is not a string.",
            "The description is the only thing an agent sees when deciding "
            "whether to load a skill, and for a meta-skill it is also the "
            "identification channel used at cleanup.",
            "Add a description: a capability sentence plus 'Use when ...'.",
        )
        return

    if published:
        _check_marker(value, location, report)

    if len(value) > DESCRIPTION_MAX:
        report.error(
            location,
            f"'description' resolves to {len(value)} characters (limit {DESCRIPTION_MAX}).",
            "The spec caps the description length.",
            f"Trim it to at most {DESCRIPTION_MAX} characters.",
        )
    elif len(value) > DESCRIPTION_WARN:
        report.warn(
            location,
            f"'description' is {len(value)} characters, near the {DESCRIPTION_MAX} cap.",
            "A description close to the cap is usually carrying body content.",
            "Move detail into the body and keep the description to the "
            "capability plus its triggers.",
        )

    body = value[len(MARKER) :] if value.startswith(MARKER) else value
    first = body.strip().split(" ", 1)[0].rstrip(",.").lower()
    if published and first in {"this", "a", "an", "helps", "allows", "provides"}:
        report.warn(
            location,
            f"the description opens with filler ('{first}') after the marker.",
            "Every meta-skill shares an identical 41-character opening, so the "
            "words right after it are the only thing distinguishing this skill "
            "from its siblings in a listing that may clip the rest.",
            "Start with the distinctive action verb or domain noun instead.",
        )


def _check_marker(value: str, location: str, report: Report) -> None:
    if value.startswith(MARKER):
        if value.count("[META-SKILL:") > 1:
            report.error(
                location,
                "the marker appears more than once in the description.",
                "A duplicated marker is a copy-paste artifact and wastes the "
                "description budget that trigger quality needs.",
                "Keep exactly one marker, at the very start.",
            )
        return

    head = value[:60]
    if "meta-skill" in head.lower():
        report.error(
            location,
            "'description' nearly matches the marker but is not byte-exact.\n"
            + codepoint_diff(value),
            "Matching is byte-exact. A near-miss marker is worse than none: "
            "cleanup will not find this skill, but the author believes it is "
            "marked, so it silently persists in every target project.",
            "Retype the marker as plain ASCII. Do not copy it out of rendered "
            "docs — copy the fenced authoring block in the catalog's CONTEXT.md.",
        )
        return

    report.error(
        location,
        "'description' does not begin with the meta-skill marker.\n"
        f"            expected start: {MARKER!r}\n"
        f"            actual start:   {value[:60]!r}",
        "Published meta-skills are disposable: once a target project's harness "
        "is built, cleanup finds them by this marker in the description — the "
        "only field agents always see, and the only reliable one, since "
        "installers rename skills to avoid collisions. Without the marker this "
        "skill is invisible to cleanup and burns context in every target "
        "project forever.",
        "Make 'description' a folded block scalar whose first line is the "
        "marker; the fold supplies the required trailing space:\n"
        "            description: >\n"
        "              [META-SKILL: remove after harness setup]\n"
        "              Designs ... Use when ...\n"
        "          Do not type a trailing space (the trailing-whitespace hook "
        "strips it). Do not leave a blank line after the marker (it folds to a "
        "newline, not a space).",
    )


def _check_body_size(text: str, name: str, report: Report) -> None:
    end = text.find("\n---", 3)
    body = text[end + 4 :] if end != -1 else text
    lines = len(body.splitlines())
    if lines > BODY_WARN_LINES:
        report.warn(
            f"{name}/SKILL.md",
            f"the body is {lines} lines (soft limit {BODY_WARN_LINES}).",
            "A long body loads in full every time the skill triggers.",
            "Move conditional material into references/ with a precise load condition.",
        )


def check_links(skill: Path, report: Report) -> None:
    linked: set[Path] = set()
    for md in sorted(skill.rglob("*.md")):
        text = strip_code(md.read_text(encoding="utf-8"))
        for target in LINK_RE.findall(text):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            clean = target.split("#", 1)[0].split("?", 1)[0]
            if not clean:
                continue
            location = f"{skill.name}/{md.relative_to(skill)}"
            resolved = (md.parent / clean).resolve()
            try:
                resolved.relative_to(skill.resolve())
            except ValueError:
                report.error(
                    location,
                    f"the link '{target}' resolves outside the skill directory.",
                    "An installed skill loses everything outside its own "
                    "directory, so this link is already broken for every user "
                    "who installs it — it only resolves here, in the "
                    "repository.",
                    "Inline what you need, move the target inside the skill, or "
                    "instruct the user to install the other skill instead of "
                    "linking to it.",
                )
                continue
            if not resolved.exists():
                report.error(
                    location,
                    f"the link '{target}' points to a path that does not exist.",
                    "A dead link sends an agent looking for guidance that is not "
                    "there, and it ships to every target project.",
                    f"Correct the path or create {clean}.",
                )
                continue
            linked.add(resolved)

    for dirname in LINKED_DIRS:
        directory = skill / dirname
        if not directory.is_dir():
            continue
        for path in sorted(p for p in directory.rglob("*") if p.is_file()):
            if path.resolve() in linked:
                continue
            report.warn(
                f"{skill.name}/{path.relative_to(skill)}",
                f"nothing in the skill links to this {dirname} file.",
                "Reference and script files are reached through links; an "
                "unlinked one is unreachable dead weight that still ships to "
                "every target project.",
                "Link it from SKILL.md with its load condition, or delete it.",
            )


def check_skill(skill: Path, report: Report) -> None:
    published = SKILLS in skill.parents
    check_structure(skill, report)
    if check_skill_md(skill, report, published) is not None:
        check_links(skill, report)


def discover() -> list[Path]:
    """Every skill in the repository: published ones and this repo's own.

    Internal skills are checked too. They are exempt from the marker (see
    `published` in check_skill), but every other rule applies to them.
    """
    found: list[Path] = []
    if SKILLS.is_dir():
        found += SKILLS.glob("*/*")
    if INTERNAL_SKILLS.is_dir():
        found += INTERNAL_SKILLS.glob("*")
    return sorted(p for p in found if p.is_dir() and (p / "SKILL.md").is_file())


def selftest() -> int:
    """Assert the checks still fire.

    The marker and link checks have no subject until the first skill lands, so
    without this they are untested code that would pass silently forever and
    then fail to catch the very first real violation.
    """
    cases: list[tuple[str, bool, str]] = [
        (
            "folded, marker on its own line",
            True,
            "description: >\n  [META-SKILL: remove after harness setup]\n  Designs harnesses.\n",
        ),
        (
            "folded, marker inline",
            True,
            "description: >\n  [META-SKILL: remove after harness setup] Designs harnesses.\n",
        ),
        (
            "folded, marker wrapped across lines",
            True,
            "description: >\n  [META-SKILL: remove after\n  harness setup] Designs harnesses.\n",
        ),
        (
            "double-quoted one-liner",
            True,
            'description: "[META-SKILL: remove after harness setup] Designs."\n',
        ),
        (
            "plain scalar (invalid YAML)",
            False,
            "description: [META-SKILL: remove after harness setup] Designs.\n",
        ),
        (
            "blank line after marker",
            False,
            "description: >\n  [META-SKILL: remove after harness setup]\n\n  Designs harnesses.\n",
        ),
        ("no marker", False, "description: >\n  Designs harnesses.\n"),
        (
            "near-miss: U+00A0 instead of space",
            False,
            "description: >\n  [META-SKILL: remove after harness setup] Designs.\n",
        ),
        (
            "near-miss: wrong case",
            False,
            "description: >\n  [Meta-Skill: remove after harness setup] Designs.\n",
        ),
    ]
    failures: list[str] = []
    for label, want_ok, source in cases:
        data, _ = parse_frontmatter(f"---\n{source}---\n")
        value = data.get("description") if data else None
        got_ok = isinstance(value, str) and value.startswith(MARKER)
        if got_ok is not want_ok:
            failures.append(
                f"  marker check: {label}: expected "
                f"{'conformant' if want_ok else 'rejected'}, got the opposite"
            )

    link_cases: list[tuple[str, str, list[str]]] = [
        ("plain link is seen", "[a](references/a.md)", ["references/a.md"]),
        ("escaping link is seen", "[a](../../other/b.md)", ["../../other/b.md"]),
        ("fenced code is ignored", "```\n[a](references/a.md)\n```", []),
        ("inline code is ignored", "`[a](references/a.md)`", []),
        ("image is ignored", "![a](assets/a.png)", []),
        ("anchor-only is seen as-is", "[a](#section)", ["#section"]),
    ]
    for label, source, want in link_cases:
        got = LINK_RE.findall(strip_code(source))
        if got != want:
            failures.append(f"  link check: {label}: expected {want}, got {got}")

    if failures:
        print("Self-test FAILED:", file=sys.stderr)
        print("\n".join(failures), file=sys.stderr)
        print(
            "\nThe validator's own logic is broken. Until this passes, a green "
            "run proves nothing.",
            file=sys.stderr,
        )
        return 1

    print(f"Self-test OK ({len(cases)} marker cases, {len(link_cases)} link cases).")
    return 0


def main(argv: list[str]) -> int:
    if argv == ["--selftest"]:
        return selftest()

    if argv == ["--all"]:
        targets = discover()
    elif argv and not argv[0].startswith("-"):
        targets = [Path(a).resolve() for a in argv]
    else:
        print(
            f"usage: {Path(__file__).name} <skill-dir>... | --all | --selftest",
            file=sys.stderr,
        )
        return 2

    for target in targets:
        if not target.is_dir():
            print(f"error: not a directory: {target}", file=sys.stderr)
            return 2

    report = Report()
    for target in targets:
        check_skill(target, report)

    for message in report.warnings:
        print(message, file=sys.stderr)
        print(file=sys.stderr)
    for message in report.errors:
        print(message, file=sys.stderr)
        print(file=sys.stderr)

    count = len(targets)
    if report.errors:
        print(
            f"{len(report.errors)} error(s), {len(report.warnings)} warning(s) "
            f"across {count} skill(s).",
            file=sys.stderr,
        )
        return 1

    print(
        f"{count} skill(s) OK"
        + (f", {len(report.warnings)} warning(s)." if report.warnings else ".")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
