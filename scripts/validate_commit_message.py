#!/usr/bin/env python3
"""Validate the repository's scoped Conventional Commit subject contract."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

TYPES = "feat|fix|docs|refactor|chore|test|ci|build|perf|revert"
FIXED_SCOPES = {
    "harness",
    "environment",
    "knowledge",
    "quality",
    "ci",
    "readme",
    "catalogs",
    "meta-lifecycle",
}
SUBJECT = re.compile(rf"^({TYPES})\(([^)]+)\)(!)?: ([a-z][A-Za-z0-9 -]*)$")


def allowed_scopes(root: Path) -> set[str]:
    scopes = set(FIXED_SCOPES)
    for base in (root / ".agents" / "skills", root / "skills"):
        if base.is_dir():
            scopes.update(path.parent.name for path in base.rglob("SKILL.md"))
    return scopes


def validate(message: str, root: Path) -> str | None:
    subject = message.splitlines()[0] if message.splitlines() else ""
    if len(subject) > 50:
        return "subject must be 50 characters or fewer"
    match = SUBJECT.fullmatch(subject)
    if not match:
        return (
            "subject must match <type>(<scope>)[!]: <lowercase imperative description>"
        )
    scopes = match.group(2).split(", ")
    valid = allowed_scopes(root)
    unknown = [scope for scope in scopes if scope not in valid]
    if unknown:
        return "unknown scope(s): " + ", ".join(unknown)
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--message", help="commit message to validate")
    source.add_argument("--file", type=Path, help="commit message file")
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    args = parser.parse_args()
    try:
        message = (
            args.message
            if args.message is not None
            else args.file.read_text(encoding="utf-8")
        )
    except OSError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    error = validate(message, args.root.resolve())
    if error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Commit message is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
