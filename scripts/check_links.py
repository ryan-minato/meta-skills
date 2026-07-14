#!/usr/bin/env python3
"""Check local Markdown links without fetching remote content."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

LINK = re.compile(r"(?<!!)\[[^]]*\]\(([^)]+)\)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    for markdown in root.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        for target in LINK.findall(markdown.read_text(encoding="utf-8")):
            target = target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            destination = target.split("#", 1)[0]
            if destination and not (markdown.parent / destination).resolve().exists():
                errors.append(f"{markdown.relative_to(root)}: missing {target}")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print("Local Markdown links are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
