#!/usr/bin/env python3
"""Validate the focused Agent Skill contract used by this repository."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MARKER = (
    "> **META-SKILL** — One-time harness scaffolding; remove this skill after "
    "the target project's harness is verified."
)
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def frontmatter(text: str) -> tuple[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    return text[4:end], text[end + 5 :]


def scalar(header: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", header)
    if not match:
        return None
    return match.group(1).strip().strip("\"'")


def internal_value(header: str) -> str | None:
    match = re.search(
        r"(?ms)^metadata:\s*\n(?:^[ \t].*\n?)*?^[ \t]+internal:\s*(.+?)\s*$", header
    )
    return match.group(1).strip().strip("\"'") if match else None


def validate(path: Path, *, internal: bool | None = None) -> list[str]:
    errors: list[str] = []
    skill_file = path / "SKILL.md" if path.is_dir() else path
    if skill_file.name != "SKILL.md" or not skill_file.is_file():
        return [f"{path}: expected a SKILL.md file or its directory"]
    skill_dir = skill_file.parent
    if not NAME_RE.fullmatch(skill_dir.name):
        errors.append(f"{skill_dir}: directory name must be lowercase kebab-case")
    parsed = frontmatter(skill_file.read_text(encoding="utf-8"))
    if parsed is None:
        return errors + [
            f"{skill_file}: frontmatter must start at byte zero and close with ---"
        ]
    header, body = parsed
    name = scalar(header, "name")
    description = scalar(header, "description")
    if name != skill_dir.name:
        errors.append(f"{skill_file}: frontmatter name must match directory name")
    if not description:
        errors.append(f"{skill_file}: frontmatter requires a description")
    is_internal = internal if internal is not None else internal_value(header) == "true"
    if is_internal:
        if internal_value(header) != "true":
            errors.append(
                f'{skill_file}: internal skills require metadata.internal: "true"'
            )
        if "[META-SKILL] " in (description or "") or MARKER in body:
            errors.append(
                f"{skill_file}: internal skills must not carry META-SKILL markers"
            )
    else:
        if not (description or "").startswith("[META-SKILL] "):
            errors.append(
                f"{skill_file}: public skills require a [META-SKILL] description prefix"
            )
        first = next((line for line in body.splitlines() if line.strip()), "")
        if first != MARKER:
            errors.append(
                f"{skill_file}: public skills require the exact first-body META-SKILL marker"
            )
        if internal_value(header) == "true":
            errors.append(
                f"{skill_file}: public skills may not declare metadata.internal"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths", nargs="+", type=Path, help="skill directories or SKILL.md files"
    )
    parser.add_argument(
        "--internal", action="store_true", help="require internal-skill rules"
    )
    args = parser.parse_args()
    errors: list[str] = []
    for path in args.paths:
        errors.extend(validate(path, internal=True if args.internal else None))
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Validated {len(args.paths)} skill path(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
