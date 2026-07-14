from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SkillValidationTests(unittest.TestCase):
    def run_check(self, fixture: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "scripts/check_skill.py", f"tests/fixtures/{fixture}"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_valid_meta_skill_passes(self) -> None:
        self.assertEqual(self.run_check("valid-meta-skill").returncode, 0)

    def test_missing_body_marker_fails(self) -> None:
        result = self.run_check("invalid-meta-skill")
        self.assertEqual(result.returncode, 1)
        self.assertIn("first-body META-SKILL", result.stderr)

    def test_internal_skill_cannot_inherit_marker(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "scripts/check_skill.py",
                "--internal",
                "tests/fixtures/valid-meta-skill",
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("internal skills", result.stderr)
