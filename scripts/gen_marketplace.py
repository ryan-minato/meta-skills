#!/usr/bin/env python3
"""Generate the future marketplace only when public catalog skills exist."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=False)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    args = parser.parse_args()
    root = args.root.resolve()
    skills = (
        sorted((root / "skills").glob("*/*/SKILL.md"))
        if (root / "skills").is_dir()
        else []
    )
    marketplace = root / ".claude-plugin" / "marketplace.json"
    if not skills:
        if marketplace.exists():
            print("ERROR: marketplace exists without public skills", file=sys.stderr)
            return 1
        print("No public catalogs to generate.")
        return 0
    payload = {
        "name": "meta-skills",
        "skills": [str(skill.parent.relative_to(root)) for skill in skills],
    }
    content = json.dumps(payload, indent=2) + "\n"
    if args.check:
        if (
            not marketplace.is_file()
            or marketplace.read_text(encoding="utf-8") != content
        ):
            print("ERROR: marketplace drift", file=sys.stderr)
            return 1
        return 0
    marketplace.parent.mkdir(parents=True, exist_ok=True)
    marketplace.write_text(content, encoding="utf-8")
    print("Marketplace generated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
