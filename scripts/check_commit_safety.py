#!/usr/bin/env python3
"""Scan staged changes and committer identity before a repository commit."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys

PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "likely token": re.compile(
        r"(?i)(?:github_pat_[a-z0-9_]{16,}|ghp_[a-z0-9]{16,}|glpat-[a-z0-9_-]{16,}|sk-[a-z0-9]{16,})"
    ),
    "personal email": re.compile(
        r"(?i)\b[A-Z0-9._%+-]+@(?!users\.noreply\.github\.com\b|example\.(?:com|org|net)\b)[A-Z0-9.-]+\.[A-Z]{2,}\b"
    ),
}


def command(*args: str) -> str:
    return subprocess.run(args, check=True, text=True, capture_output=True).stdout


def main() -> int:
    argparse.ArgumentParser(description=__doc__).parse_args()
    try:
        email = command("git", "config", "user.email").strip()
        diff = command("git", "diff", "--cached", "--no-ext-diff", "--unified=0")
    except (OSError, subprocess.CalledProcessError) as error:
        print(f"ERROR: unable to inspect Git state: {error}", file=sys.stderr)
        return 2
    errors: list[str] = []
    if not re.fullmatch(r"[^@\s]+@users\.noreply\.github\.com", email):
        errors.append("committer email must be an anonymous GitHub noreply address")
    for name, pattern in PATTERNS.items():
        if pattern.search(diff):
            errors.append(f"staged diff contains {name}")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(
        "Staged commit safety gate passed."
        if diff
        else "No staged changes; committer identity is safe."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
