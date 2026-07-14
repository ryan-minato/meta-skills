from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class McpConfigTests(unittest.TestCase):
    def test_render_is_idempotent_and_checkable(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".agents").mkdir()
            shutil.copy(
                ROOT / ".agents" / "mcp-servers.json",
                root / ".agents" / "mcp-servers.json",
            )
            command = [
                sys.executable,
                "scripts/render_mcp_configs.py",
                "--root",
                str(root),
            ]
            self.assertEqual(
                subprocess.run(command + ["--write"], cwd=ROOT, check=False).returncode,
                0,
            )
            self.assertEqual(
                subprocess.run(command + ["--check"], cwd=ROOT, check=False).returncode,
                0,
            )
            self.assertEqual(
                subprocess.run(command + ["--write"], cwd=ROOT, check=False).returncode,
                0,
            )
            self.assertIn(
                "github", json.loads((root / ".mcp.json").read_text())["mcpServers"]
            )

    def test_bad_manifest_returns_usage_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".agents").mkdir()
            (root / ".agents" / "mcp-servers.json").write_text("{}")
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/render_mcp_configs.py",
                    "--root",
                    str(root),
                    "--check",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 2)
