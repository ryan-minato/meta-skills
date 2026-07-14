#!/usr/bin/env python3
"""Validate repository skill placement, lifecycle markers, and client links."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from check_skill import validate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    internal_root = root / ".agents" / "skills"
    if not internal_root.is_dir():
        errors.append(".agents/skills is required")
    else:
        for skill in sorted(internal_root.glob("*/SKILL.md")):
            if skill.parent.is_symlink():
                continue
            errors.extend(validate(skill, internal=True))
    claude_link = root / ".claude" / "skills"
    if not claude_link.is_symlink() or claude_link.resolve() != internal_root.resolve():
        errors.append(".claude/skills must be a relative symlink to .agents/skills")
    public_root = root / "skills"
    if public_root.exists():
        public_skills = sorted(public_root.glob("*/*/SKILL.md"))
        for skill in public_skills:
            errors.extend(validate(skill, internal=False))
        if (
            public_skills
            and not (root / ".claude-plugin" / "marketplace.json").is_file()
        ):
            errors.append("public skills require .claude-plugin/marketplace.json")
    for readme in (root / "README.md", root / "README.zh.md"):
        if not readme.is_file():
            errors.append(f"missing required bilingual guide: {readme.name}")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print("Repository skill contracts are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
