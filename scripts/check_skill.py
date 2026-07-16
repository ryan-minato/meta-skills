#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml"]
# ///
"""Per-skill validator: one skill's file structure and its SKILL.md content.

Usage: check_skill.py PATH [PATH...] | --all
`--all` discovers published skills (skills/<catalog>/<skill>/) and this
repository's own skills (.agents/skills/<skill>/). A skill is *published*
when it lives under skills/; published skills must carry the marker and be
fully self-contained, while internal skills must not carry the marker and
may link outside their root.

Check IDs (each has a self-test fixture proving it fires):

    S1-S3  structure (warnings): non-canonical entries, READMEs,
           unreferenced files under references/ and scripts/
    M1-M6  SKILL.md content (errors; M4 warns near the description cap;
           M6 gates the `metadata.internal` flag skill installers honor)
    L1     markdown links (errors): must resolve; published skills' links
           must not escape the skill root. Inline-code mentions are not
           links and are not checked.

Warnings are printed but do not fail the run; errors do. The self-test runs
first on every invocation (`--self-test` alone, `--no-self-test` to skip)
because the published catalogs may be empty.

MARKER below is one of the aligned copies of the marker literal; the
sync-contract skill owns the alignment procedure when the marker changes.

Exit codes: 0 clean or warnings only, 1 error found, 2 broken validator.
"""

from __future__ import annotations

import argparse
import copy
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

import yaml

MARKER = "Disposable meta-skill (delete after the harness is built):"
ALLOWED_ENTRIES = {
    "SKILL.md": "file",
    "references": "directory",
    "scripts": "directory",
    "assets": "directory",
}
REFERENCED_DIRS = ("references", "scripts")
REPO_ONLY_TOKENS = ("README.zh", "validate_repo", "check_skill", "meta-skill-contract")
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


@dataclass
class Issue:
    check: str
    severity: str  # "error" | "warning"
    path: str
    message: str

    def __str__(self) -> str:
        return f"[{self.check}] {self.severity}: {self.path}: {self.message}"


def read_frontmatter(path: Path) -> tuple[dict | None, str | None]:
    """Parse the YAML frontmatter block; return (mapping, error)."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, "no YAML frontmatter block at the top of the file"
    end = text.find("\n---", 4)
    if end == -1:
        return None, "frontmatter block is never closed with `---`"
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        return None, f"frontmatter is not valid YAML ({exc})"
    if not isinstance(data, dict):
        return None, "frontmatter is not a YAML mapping"
    return data, None


def markdown_links(text: str) -> list[str]:
    """Local link targets, ignoring code fences, inline code, URLs, anchors."""
    targets: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK_RE.finditer(re.sub(r"`[^`]*`", "", line)):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if target:
                targets.append(target)
    return targets


def skill_mentions(text: str) -> set[str]:
    """Paths SKILL.md explicitly points at: link targets and inline code.

    Inline-code spans also count word by word, so `uv run scripts/x.py`
    mentions scripts/x.py. Bare prose must not count — a substring test let
    `references/config` pass whenever `references/config.md` was linked.
    """
    mentions = set(markdown_links(text))
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for span in re.findall(r"`([^`]+)`", line):
            mentions.add(span)
            mentions.update(span.split())
    return mentions


def check_structure(skill: Path, rel_base: Path) -> list[Issue]:
    """S1-S3: canonical entries only, no READMEs, no unreferenced files."""
    issues: list[Issue] = []

    def rel(path: Path) -> str:
        return str(path.relative_to(rel_base))

    for entry in sorted(skill.iterdir()):
        expected = ALLOWED_ENTRIES.get(entry.name)
        actual = (
            "file"
            if entry.is_file()
            else "directory"
            if entry.is_dir()
            else "special entry"
        )
        if expected == actual:
            continue
        if entry.name.startswith("README"):
            continue  # S2 reports READMEs with the sharper message
        message = (
            f"is a {actual}, but `{entry.name}` in a skill must be a "
            f"{expected}. A mistyped entry dodges every later check and "
            "ships to targets unvalidated. Fix its type or remove it."
            if expected
            else "unexpected entry in a skill directory. A skill holds only "
            "SKILL.md plus references/, scripts/, and assets/; anything "
            "else ships to targets as unexplained clutter. Move it into "
            "one of the canonical folders or remove it."
        )
        issues.append(Issue("S1", "warning", rel(entry), message))
    for readme in sorted(skill.rglob("README*")):
        issues.append(
            Issue(
                "S2",
                "warning",
                rel(readme),
                "do not create a README per skill. The catalog README "
                "documents the skill; a README inside the skill ships to "
                "targets as clutter. Move the content into SKILL.md or the "
                "catalog README.",
            )
        )
    skill_md = skill / "SKILL.md"
    body = skill_md.read_text(encoding="utf-8") if skill_md.is_file() else ""
    mentions = skill_mentions(body)
    for folder in REFERENCED_DIRS:
        base = skill / folder
        if not base.is_dir():
            continue
        for file in sorted(p for p in base.rglob("*") if p.is_file()):
            mention = file.relative_to(skill).as_posix()
            if mention not in mentions:
                issues.append(
                    Issue(
                        "S3",
                        "warning",
                        rel(file),
                        f"`{mention}` is never referenced in SKILL.md as a "
                        "link target or inline-code path; a bare prose "
                        "mention does not count. A file nothing points to "
                        "is invisible to the agent and dead weight in every "
                        "install. Link it with a load condition, or remove "
                        "it.",
                    )
                )
    return issues


def check_skill_md(skill: Path, rel_base: Path, published: bool) -> list[Issue]:
    """M1-M6: frontmatter, name, marker, size, portability, internal flag."""
    issues: list[Issue] = []
    skill_md = skill / "SKILL.md"
    rel = str(skill_md.relative_to(rel_base))
    if not skill_md.is_file():
        issues.append(
            Issue(
                "M1",
                "error",
                str(skill.relative_to(rel_base)),
                "no SKILL.md. A skill directory without SKILL.md is not a "
                "skill; agents cannot load it. Create SKILL.md or remove "
                "the directory.",
            )
        )
        return issues
    data, err = read_frontmatter(skill_md)
    name = data.get("name") if data else None
    description = data.get("description") if data else None
    if err or not isinstance(name, str) or not isinstance(description, str):
        issues.append(
            Issue(
                "M1",
                "error",
                rel,
                f"{err or 'frontmatter is missing `name` or `description`'}. "
                "Skills are loaded and identified by their frontmatter; "
                "without it the skill cannot ship. Add a `---` YAML block "
                "with string `name` and `description`.",
            )
        )
        return issues
    prefix_ok = name.startswith("meta-") if published else True
    if name != skill.name or not NAME_RE.match(name) or len(name) > 64 or not prefix_ok:
        expectation = (
            "lowercase kebab-case of at most 64 chars, starting with `meta-`"
            if published
            else "lowercase kebab-case of at most 64 chars"
        )
        issues.append(
            Issue(
                "M2",
                "error",
                rel,
                f"name `{name}` must equal its directory `{skill.name}` and "
                f"be {expectation}. The Agent Skills spec ties the name to "
                "the directory; the meta- prefix groups published skills in "
                "the tree. Rename the directory or fix the name field.",
            )
        )
    if published and not description.startswith(MARKER + " "):
        issues.append(
            Issue(
                "M3",
                "error",
                rel,
                "description must start with the marker followed by one "
                "space. The marker is how target-project agents find and "
                "delete installed meta-skills; without it this skill would "
                f"survive cleanup. Begin the description with: `{MARKER} `",
            )
        )
    if not published and MARKER in description:
        issues.append(
            Issue(
                "M3",
                "error",
                rel,
                "carries the marker but is not a published skill. The "
                "marker means 'disposable in a target project'; on this "
                "repository's own skills it would invite deletion of the "
                "harness. Remove the marker from this description.",
            )
        )
    if len(description) > 1024:
        issues.append(
            Issue(
                "M4",
                "error",
                rel,
                f"description is {len(description)} chars; the Agent Skills "
                "spec caps it at 1024, and every excess char loads into "
                "each session. Shorten it.",
            )
        )
    elif len(description) >= 900:
        issues.append(
            Issue(
                "M4",
                "warning",
                rel,
                f"description is {len(description)} chars, close to the "
                "1024 spec cap. Consider tightening it before the cap "
                "forces a rushed cut.",
            )
        )
    if published:
        for md_file in sorted(skill.rglob("*.md")):
            text = md_file.read_text(encoding="utf-8")
            for token in REPO_ONLY_TOKENS:
                if token in text:
                    issues.append(
                        Issue(
                            "M5",
                            "error",
                            str(md_file.relative_to(rel_base)),
                            f"mentions `{token}`, which exists only in this "
                            "repository. Published skills run in target "
                            "projects, where the reference would misdirect "
                            "the agent. Describe the requirement without "
                            "repo-only names.",
                        )
                    )
    metadata = data.get("metadata")
    internal_flag = metadata.get("internal") if isinstance(metadata, dict) else None
    if published and internal_flag:
        issues.append(
            Issue(
                "M6",
                "error",
                rel,
                "sets `metadata.internal`, which skill installers honor by "
                "hiding the skill — a published skill flagged internal "
                "disappears from installs. Remove the flag.",
            )
        )
    if not published and internal_flag is not True:
        issues.append(
            Issue(
                "M6",
                "error",
                rel,
                "is missing `metadata.internal: true`. Skill installers "
                "hard-scan `.agents/skills/` and `.claude/skills/`, so an "
                "unflagged internal skill is offered to target projects. "
                "Add the flag to the frontmatter.",
            )
        )
    return issues


def check_links(skill: Path, rel_base: Path, published: bool) -> list[Issue]:
    """L1: markdown links resolve; published skills' links stay inside."""
    issues: list[Issue] = []
    for md_file in sorted(skill.rglob("*.md")):
        rel = str(md_file.relative_to(rel_base))
        for target in markdown_links(md_file.read_text(encoding="utf-8")):
            resolved = (md_file.parent / target).resolve()
            if not resolved.exists():
                issues.append(
                    Issue(
                        "L1",
                        "error",
                        rel,
                        f"link `{target}` does not resolve. Broken links "
                        "strand agents mid-procedure. Fix the path or "
                        "remove the link.",
                    )
                )
            elif published and not resolved.is_relative_to(skill.resolve()):
                issues.append(
                    Issue(
                        "L1",
                        "error",
                        rel,
                        f"link `{target}` escapes the skill directory. "
                        "Installed skills lose everything outside their own "
                        "directory. Point the link inside the skill or "
                        "inline the content.",
                    )
                )
    return issues


def check_skill(skill: Path, repo_root: Path) -> list[Issue]:
    skill = skill.resolve()
    rel_base = repo_root if skill.is_relative_to(repo_root) else skill.parent
    published = skill.is_relative_to((repo_root / "skills").resolve())
    issues = check_skill_md(skill, rel_base, published)
    if (skill / "SKILL.md").is_file():
        issues += check_structure(skill, rel_base)
        issues += check_links(skill, rel_base, published)
    return issues


def discover_all(repo_root: Path) -> list[Path]:
    skills: list[Path] = []
    published_root = repo_root / "skills"
    if published_root.is_dir():
        for catalog in sorted(p for p in published_root.iterdir() if p.is_dir()):
            skills.extend(sorted(p for p in catalog.iterdir() if p.is_dir()))
    internal_root = repo_root / ".agents" / "skills"
    if internal_root.is_dir():
        skills.extend(sorted(p for p in internal_root.iterdir() if p.is_dir()))
    return skills


# --- self-test ---------------------------------------------------------------

VALID_SKILL = f"""---
name: meta-good
description: >-
  {MARKER} Scaffolds an example. Use when testing.
---

# Meta Good

A valid body linking [notes](references/notes.md) and running
`scripts/run.sh` when needed.
"""

VALID_INTERNAL = """---
name: helper
description: Helps with repository chores. Use when testing.
metadata:
  internal: true
---

# Helper

Reads [the shared doc](../../shared.md) outside its root, which internal
skills may do.
"""

BASE_FIXTURE: dict[str, str] = {
    "skills/core/meta-good/SKILL.md": VALID_SKILL,
    "skills/core/meta-good/references/notes.md": "notes\n",
    "skills/core/meta-good/scripts/run.sh": "#!/bin/sh\n",
    ".agents/skills/helper/SKILL.md": VALID_INTERNAL,
    ".agents/shared.md": "shared\n",
    "AGENTS.md": "# Agents\n",
}

PUBLISHED = "skills/core/meta-good"
INTERNAL = ".agents/skills/helper"


def _with(edits: dict[str, str | None]) -> dict[str, str]:
    """BASE_FIXTURE with files replaced, or removed when the value is None."""
    fixture = copy.deepcopy(BASE_FIXTURE)
    for path, content in edits.items():
        if content is None:
            fixture.pop(path, None)
        else:
            fixture[path] = content
    return fixture


NO_REFS_SKILL = VALID_SKILL.replace(
    "A valid body linking [notes](references/notes.md) and running\n"
    "`scripts/run.sh` when needed.",
    "A valid body running `scripts/run.sh` when needed.",
)

# (check id, severity, expected issue path, skill dir, fixture). Pinning the
# path keeps a fixture from passing by firing its check on an unrelated
# subject.
SELF_TEST_CASES: list[tuple[str, str, str, str, dict[str, str]]] = [
    (
        "S1",
        "warning",
        f"{PUBLISHED}/notes.txt",
        PUBLISHED,
        _with({f"{PUBLISHED}/notes.txt": "stray\n"}),
    ),
    # A regular file named after a canonical directory must not slip
    # through on its name.
    (
        "S1",
        "warning",
        f"{PUBLISHED}/references",
        PUBLISHED,
        _with(
            {
                f"{PUBLISHED}/SKILL.md": NO_REFS_SKILL,
                f"{PUBLISHED}/references/notes.md": None,
                f"{PUBLISHED}/references": "a file where a directory belongs\n",
            }
        ),
    ),
    (
        "S2",
        "warning",
        f"{PUBLISHED}/README.md",
        PUBLISHED,
        _with({f"{PUBLISHED}/README.md": "stray\n"}),
    ),
    (
        "S3",
        "warning",
        f"{PUBLISHED}/references/unused.md",
        PUBLISHED,
        _with({f"{PUBLISHED}/references/unused.md": "x\n"}),
    ),
    # `references/config` is a substring of the linked config.md; that must
    # not count as a mention.
    (
        "S3",
        "warning",
        f"{PUBLISHED}/references/config",
        PUBLISHED,
        _with(
            {
                f"{PUBLISHED}/SKILL.md": VALID_SKILL.replace(
                    "[notes](references/notes.md)",
                    "[notes](references/notes.md) and [config](references/config.md)",
                ),
                f"{PUBLISHED}/references/config.md": "config doc\n",
                f"{PUBLISHED}/references/config": "extensionless twin\n",
            }
        ),
    ),
    # A bare prose mention is not a reference either.
    (
        "S3",
        "warning",
        f"{PUBLISHED}/references/prose.md",
        PUBLISHED,
        _with(
            {
                f"{PUBLISHED}/SKILL.md": VALID_SKILL.replace(
                    "when needed.",
                    "when needed. Background sits in references/prose.md nearby.",
                ),
                f"{PUBLISHED}/references/prose.md": "prose\n",
            }
        ),
    ),
    (
        "M1",
        "error",
        f"{PUBLISHED}/SKILL.md",
        PUBLISHED,
        _with({f"{PUBLISHED}/SKILL.md": "no frontmatter\n"}),
    ),
    ("M1", "error", PUBLISHED, PUBLISHED, _with({f"{PUBLISHED}/SKILL.md": None})),
    (
        "M2",
        "error",
        f"{PUBLISHED}/SKILL.md",
        PUBLISHED,
        _with(
            {
                f"{PUBLISHED}/SKILL.md": VALID_SKILL.replace(
                    "name: meta-good", "name: meta-other"
                )
            }
        ),
    ),
    (
        "M3",
        "error",
        f"{PUBLISHED}/SKILL.md",
        PUBLISHED,
        _with(
            {
                f"{PUBLISHED}/SKILL.md": (
                    "---\nname: meta-good\ndescription: No marker here.\n---\n\nBody.\n"
                )
            }
        ),
    ),
    (
        "M3",
        "error",
        f"{INTERNAL}/SKILL.md",
        INTERNAL,
        _with(
            {
                f"{INTERNAL}/SKILL.md": (
                    f'---\nname: helper\ndescription: "{MARKER} Oops."\n---\n\nBody.\n'
                )
            }
        ),
    ),
    # The marker hidden mid-description must fire too.
    (
        "M3",
        "error",
        f"{INTERNAL}/SKILL.md",
        INTERNAL,
        _with(
            {
                f"{INTERNAL}/SKILL.md": (
                    f'---\nname: helper\ndescription: "Helps. {MARKER} Oops."\n---\n\nBody.\n'
                )
            }
        ),
    ),
    (
        "M4",
        "error",
        f"{PUBLISHED}/SKILL.md",
        PUBLISHED,
        _with(
            {
                f"{PUBLISHED}/SKILL.md": (
                    f'---\nname: meta-good\ndescription: "{MARKER} {"x" * 1024}"\n---\n\nBody.\n'
                )
            }
        ),
    ),
    (
        "M4",
        "warning",
        f"{PUBLISHED}/SKILL.md",
        PUBLISHED,
        _with(
            {
                f"{PUBLISHED}/SKILL.md": (
                    f'---\nname: meta-good\ndescription: "{MARKER} {"x" * 860}"\n---\n\nBody.\n'
                )
            }
        ),
    ),
    (
        "M5",
        "error",
        f"{PUBLISHED}/references/notes.md",
        PUBLISHED,
        _with({f"{PUBLISHED}/references/notes.md": "run validate_repo first\n"}),
    ),
    (
        "L1",
        "error",
        f"{PUBLISHED}/SKILL.md",
        PUBLISHED,
        _with(
            {
                f"{PUBLISHED}/SKILL.md": VALID_SKILL.replace(
                    "references/notes.md", "references/missing.md"
                )
            }
        ),
    ),
    (
        "L1",
        "error",
        f"{PUBLISHED}/SKILL.md",
        PUBLISHED,
        _with(
            {
                f"{PUBLISHED}/SKILL.md": VALID_SKILL.replace(
                    "references/notes.md", "../../../AGENTS.md"
                )
            }
        ),
    ),
    # An internal skill without the flag leaks into skill installers, which
    # hard-scan the internal skill directories.
    (
        "M6",
        "error",
        f"{INTERNAL}/SKILL.md",
        INTERNAL,
        _with(
            {
                f"{INTERNAL}/SKILL.md": VALID_INTERNAL.replace(
                    "metadata:\n  internal: true\n", ""
                )
            }
        ),
    ),
    # A published skill carrying the flag vanishes from installs.
    (
        "M6",
        "error",
        f"{PUBLISHED}/SKILL.md",
        PUBLISHED,
        _with(
            {
                f"{PUBLISHED}/SKILL.md": VALID_SKILL.replace(
                    "---\n\n# Meta Good",
                    "metadata:\n  internal: true\n---\n\n# Meta Good",
                )
            }
        ),
    ),
]


def materialize(fixture: dict[str, str], root: Path) -> None:
    for rel, content in fixture.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def run_self_test(verbose: bool) -> bool:
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        valid_root = Path(tmp) / "valid"
        materialize(BASE_FIXTURE, valid_root)
        for skill_rel in (PUBLISHED, INTERNAL):
            unexpected = check_skill(valid_root / skill_rel, valid_root)
            if unexpected:
                ok = False
                print(f"self-test: the valid fixture `{skill_rel}` raised issues:")
                for issue in unexpected:
                    print(f"  {issue}")
        for index, (check_id, severity, expected_path, skill_rel, fixture) in enumerate(
            SELF_TEST_CASES
        ):
            case_root = Path(tmp) / f"case{index}"
            materialize(fixture, case_root)
            fired = {
                (issue.check, issue.severity, issue.path)
                for issue in check_skill(case_root / skill_rel, case_root)
            }
            if (check_id, severity, expected_path) not in fired:
                ok = False
                print(
                    f"self-test: fixture {index} for {check_id}/{severity} at "
                    f"{expected_path} did not trip it "
                    f"(fired: {sorted(fired) or 'none'})"
                )
            elif verbose:
                print(f"self-test: {check_id} ({severity}) fires on {expected_path}")
    if ok and verbose:
        print(
            f"self-test: all {len(SELF_TEST_CASES)} negative fixtures fire; "
            "both valid fixtures pass"
        )
    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="skill directories to check")
    parser.add_argument(
        "--all", action="store_true", help="check every published and internal skill"
    )
    parser.add_argument(
        "--self-test", action="store_true", help="run only the fixture self-test"
    )
    parser.add_argument(
        "--no-self-test", action="store_true", help="skip the fixture self-test"
    )
    args = parser.parse_args()

    if not args.no_self_test:
        if not run_self_test(verbose=args.self_test):
            print(
                "check_skill: self-test FAILED — a check is broken; fix the "
                "validator before trusting any green run"
            )
            return 2
        if args.self_test:
            return 0

    repo_root = Path(__file__).resolve().parent.parent
    if args.all:
        skills = discover_all(repo_root)
    elif args.paths:
        skills = [Path(p) for p in args.paths]
    else:
        print("check_skill: pass one or more skill directories, or --all")
        return 2

    issues: list[Issue] = []
    for skill in skills:
        if not skill.is_dir():
            print(f"check_skill: `{skill}` is not a directory")
            return 2
        issues.extend(check_skill(skill, repo_root))
    for issue in issues:
        print(issue)
    errors = sum(issue.severity == "error" for issue in issues)
    warnings = len(issues) - errors
    if errors:
        print(f"check_skill: {errors} error(s), {warnings} warning(s)")
        return 1
    summary = f"{warnings} warning(s)" if warnings else "clean"
    print(f"check_skill: OK (self-test passed, {len(skills)} skill(s), {summary})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
