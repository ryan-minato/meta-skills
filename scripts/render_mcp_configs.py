#!/usr/bin/env python3
"""Render or check credential-free MCP declarations for supported clients."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def json_text(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def targets(root: Path) -> dict[Path, str]:
    manifest = json.loads(
        (root / ".agents" / "mcp-servers.json").read_text(encoding="utf-8")
    )
    servers = manifest.get("servers")
    if not isinstance(servers, dict) or not servers:
        raise ValueError(".agents/mcp-servers.json requires a non-empty servers object")
    claude: dict[str, object] = {}
    vscode: dict[str, object] = {}
    toml: list[str] = []
    for name, config in sorted(servers.items()):
        if not isinstance(config, dict) or not isinstance(config.get("url"), str):
            raise ValueError(f"server {name} requires a URL")
        url = config["url"]
        claude_config: dict[str, str | dict[str, str]] = {"type": "http", "url": url}
        if config.get("auth") == "github-pat":
            claude_config["headers"] = {"Authorization": "Bearer ${GH_TOKEN}"}
        claude[name] = claude_config
        vscode[name] = {"type": "http", "url": url}
        toml.extend([f"[mcp_servers.{name}]", f'url = "{url}"'])
        if config.get("auth") == "github-pat":
            toml.append('bearer_token_env_var = "GH_TOKEN"')
        toml.append("")
    return {
        root / ".mcp.json": json_text({"mcpServers": claude}),
        root / ".vscode" / "mcp.json": json_text({"servers": vscode}),
        root / ".codex" / "config.toml": "\n".join(toml).rstrip() + "\n",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--check", action="store_true", help="fail when generated files drift"
    )
    mode.add_argument("--write", action="store_true", help="write generated files")
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    args = parser.parse_args()
    try:
        rendered = targets(args.root.resolve())
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    drift = [
        path
        for path, content in rendered.items()
        if not path.is_file() or path.read_text(encoding="utf-8") != content
    ]
    if args.check:
        if drift:
            print(
                "ERROR: MCP configuration drift: "
                + ", ".join(str(path) for path in drift),
                file=sys.stderr,
            )
            return 1
        print("MCP configurations are synchronized.")
        return 0
    for path, content in rendered.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Wrote {len(rendered)} MCP configuration files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
