#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Validate this repository's file structure.

Covers what belongs to the project as a whole: catalog scaffolds, the catalog
list in ARCHITECTURE.md, README translation pairs, and misplaced markers.

An individual skill's own structure is not checked here; that is check_skill.py.

Exit codes: 0 clean, 1 error found, 2 bad arguments.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SKILLS = REPO / "skills"
ARCHITECTURE = REPO / "ARCHITECTURE.md"

# Keep in sync with .agents/knowledge/meta-skill-contract.md (source of truth),
# the Core Conventions line in AGENTS.md, and MARKER in check_skill.py.
# The contract-sync skill owns that alignment.
MARKER = "[META-SKILL: remove after harness setup] "

CATALOG_FILES = ("CONTEXT.md", "README.md", "README.zh.md")
CATALOG_LIST_RE = re.compile(r"^- `([a-z0-9][a-z0-9-]*)`", re.MULTILINE)

errors: list[str] = []


def error(location: str, reason: str, why: str, fix: str) -> None:
    errors.append(
        f"ERROR  [{location}]\n  Reason: {reason}\n  Why:    {why}\n  Fix:    {fix}"
    )


def rel(path: Path) -> str:
    return str(path.relative_to(REPO))


def frontmatter(path: Path) -> dict | None:
    """Return parsed frontmatter, or None if absent or unparseable."""
    text = path.read_text(encoding="utf-8")
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


def catalogs_on_disk() -> list[str]:
    if not SKILLS.is_dir():
        return []
    return sorted(p.name for p in SKILLS.iterdir() if p.is_dir())


def catalogs_in_architecture() -> list[str] | None:
    if not ARCHITECTURE.is_file():
        return None
    text = ARCHITECTURE.read_text(encoding="utf-8")
    match = re.search(r"^## Catalogs$(.*?)^## ", text, re.MULTILINE | re.DOTALL)
    if not match:
        return None
    return sorted(CATALOG_LIST_RE.findall(match.group(1)))


def check_catalog_scaffolds(disk: list[str]) -> None:
    for name in disk:
        for filename in CATALOG_FILES:
            path = SKILLS / name / filename
            if path.is_file():
                continue
            error(
                rel(path),
                f"catalog '{name}' is missing {filename}.",
                "Every catalog carries CONTEXT.md plus a README pair. CONTEXT.md "
                "holds the catalog's goal, its constraints on what may enter, and "
                "its catalog-scoped references; agents are told to read it before "
                "changing anything in the catalog. Without it they change the "
                "catalog blind.",
                f"Create {rel(path)}.",
            )


def check_architecture_list(disk: list[str]) -> None:
    listed = catalogs_in_architecture()
    if listed is None:
        error(
            "ARCHITECTURE.md",
            "no '## Catalogs' section with a parseable list was found.",
            "That list is authoritative: it is checked against the directories "
            "under skills/, and it defines the legal commit scopes.",
            "Add a '## Catalogs' section listing each catalog as: - `name` — purpose.",
        )
        return

    for name in sorted(set(disk) - set(listed)):
        error(
            f"skills/{name}",
            f"catalog '{name}' exists on disk but is not listed in ARCHITECTURE.md.",
            "The list drives catalog validation and the legal commit scopes, so an "
            "unlisted catalog is invisible to both.",
            f"Add '- `{name}` — <purpose>' to the '## Catalogs' section, or remove "
            f"the directory. The catalog-sync skill covers this.",
        )

    for name in sorted(set(listed) - set(disk)):
        error(
            "ARCHITECTURE.md",
            f"catalog '{name}' is listed but has no directory under skills/.",
            "A listed catalog that does not exist advertises a scope nobody can "
            "use and sends readers to a missing path.",
            f"Create skills/{name}/ with its scaffold, or remove '{name}' from the "
            f"'## Catalogs' section. The catalog-sync skill covers this.",
        )


def check_translation_pairs() -> None:
    readmes = [REPO / "README.md"]
    readmes += [SKILLS / name / "README.md" for name in catalogs_on_disk()]
    for readme in readmes:
        if not readme.is_file():
            continue
        mirror = readme.with_name("README.zh.md")
        if mirror.is_file():
            continue
        error(
            rel(mirror),
            f"{rel(readme)} has no README.zh.md mirror.",
            "Every README is published in both languages, with English "
            "authoritative. A missing mirror silently drops Chinese readers.",
            f"Create {rel(mirror)} mirroring {rel(readme)}. The translation-sync "
            f"skill covers this.",
        )


def check_marker_placement() -> None:
    """No SKILL.md outside skills/<catalog>/<skill>/ may carry the marker."""
    for path in REPO.rglob("SKILL.md"):
        if ".git" in path.parts:
            continue
        try:
            parts = path.relative_to(REPO).parts
        except ValueError:
            continue
        published = len(parts) == 4 and parts[0] == "skills" and parts[3] == "SKILL.md"
        if published:
            continue
        data = frontmatter(path)
        if not data:
            continue
        description = data.get("description")
        if not isinstance(description, str) or not description.startswith(MARKER):
            continue
        error(
            rel(path),
            "a skill outside skills/<catalog>/<skill>/ carries the meta-skill marker.",
            "The marker means 'delete me after harness setup'. This path is a "
            "durable skill — this repository's own, or a harness artifact meant to "
            "survive in a target project. Carrying the marker makes a cleanup pass "
            "delete a skill that must not be deleted: the harness erases itself "
            "right after a successful build.",
            "Remove the marker from the description. Only "
            "skills/<catalog>/<skill>/SKILL.md may carry it.",
        )


def main(argv: list[str]) -> int:
    if argv:
        print(f"usage: {Path(__file__).name}", file=sys.stderr)
        return 2

    disk = catalogs_on_disk()
    check_catalog_scaffolds(disk)
    check_architecture_list(disk)
    check_translation_pairs()
    check_marker_placement()

    if errors:
        print("\n\n".join(errors), file=sys.stderr)
        print(
            f"\n{len(errors)} error(s) in the repository structure.",
            file=sys.stderr,
        )
        return 1

    print(
        f"Repository structure OK ({len(disk)} catalog(s): {', '.join(disk) or '-'})."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
