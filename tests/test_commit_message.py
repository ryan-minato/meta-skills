from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CommitMessageTests(unittest.TestCase):
    def validate(self, message: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                "scripts/validate_commit_message.py",
                "--message",
                message,
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_accepts_scoped_message(self) -> None:
        self.assertEqual(self.validate("docs(harness): define contracts").returncode, 0)

    def test_rejects_missing_scope(self) -> None:
        self.assertEqual(self.validate("docs: define contracts").returncode, 1)

    def test_rejects_unknown_scope(self) -> None:
        self.assertEqual(self.validate("docs(unknown): define contracts").returncode, 1)

    def test_rejects_sentence_case_and_period(self) -> None:
        self.assertEqual(
            self.validate("docs(harness): Define contracts.").returncode, 1
        )
