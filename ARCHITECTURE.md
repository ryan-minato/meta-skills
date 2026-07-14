# Architecture

## Layers and ownership

The repository is a full L2 harness: a reproducible environment, explicit
targets, discoverable knowledge, strong quality gates, and a Linear/GitHub
delivery workflow. `AGENTS.md` is the sole discovery root; all other documents
are reached from it.

| Layer | Location | Authority |
| --- | --- | --- |
| Agent entrypoint | `AGENTS.md`, `CLAUDE.md` | Git |
| Product and structure | `DESIGN.md`, this file | Git |
| Knowledge | `.agents/knowledge/` | Git default branch |
| Internal workflows | `.agents/skills/` | Git |
| MCP declaration | `.agents/mcp-servers.json` | Git |
| Client adapters | `.mcp.json`, `.codex/config.toml`, `.vscode/mcp.json` | Generated from declaration |
| Quality | `scripts/`, `tests/`, hooks, CI | Git |
| Delivery tracking | Linear project and issues | Linear |

## Skills

Internal workflows live as real directories in `.agents/skills/` and declare
`metadata.internal: "true"`. `.claude/skills` is a relative symlink to that
directory so clients discover one shared implementation.

Future public skills live in `skills/<catalog>/<skill>/` and are exposed for
dogfooding through relative symlinks in `.agents/skills/`. They must be
self-contained, use relative links, pass the Agent Skills contract, and carry
the two META-SKILL lifecycle markers. On the first skill in a catalog, add the
catalog's `README.md`, `README.zh.md`, `CONTEXT.md`, and marketplace entry. No
empty public catalog, `skills/` directory, or marketplace exists before then.

## MCP adapters

`.agents/mcp-servers.json` contains endpoints and auth modes but no credentials.
`scripts/render_mcp_configs.py` deterministically produces:

- Claude: root `.mcp.json` with `mcpServers`.
- Codex: `.codex/config.toml` with `[mcp_servers.<name>]` tables.
- VS Code: `.vscode/mcp.json` with `servers`.

GitHub uses `GH_TOKEN` for Claude/Codex. VS Code intentionally relies on its
OAuth connection. Linear and Agent Skills use their supported remote flows.
Always run `just sync-mcp --check` after adapter changes.

## Validation and safety

The public command surface is the `justfile`. Stdlib-first Python scripts
validate skill shape and markers, generated MCP drift, marketplace conditions,
local Markdown links, scoped commit messages, and staged safety. Pre-commit and
commit-msg hooks run the same contracts locally; GitHub Actions reruns `just
check` and scans history. Secret and PII checks permit GitHub noreply and
`example.*` placeholders but reject likely credentials and personal email.

## Knowledge synchronization

Git's origin default branch is authoritative. `knowledge-sync` fetches it,
compares only merged `.agents/knowledge/` content, and creates or updates
equivalent Linear Documents. It never edits local knowledge from Linear and
never deletes unowned remote documents. Synchronization is post-merge only.
