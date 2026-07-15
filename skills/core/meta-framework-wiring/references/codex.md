# OpenAI Codex

OpenAI's coding agent. Notes verified **2026-07-15**. Fetch before you write.

## Fetch these first

| What | URL |
|---|---|
| Config reference | <https://learn.chatgpt.com/docs/config-file/config-reference> |
| Entry file | <https://learn.chatgpt.com/docs/agent-configuration/agents-md> |
| MCP | <https://learn.chatgpt.com/docs/extend/mcp> |
| Hooks | <https://learn.chatgpt.com/docs/hooks> |
| Skills | <https://learn.chatgpt.com/docs/build-skills> |
| Subagents | <https://learn.chatgpt.com/docs/agent-configuration/subagents> |

**The domain moved**, and the destination is not what you would expect.
`developers.openai.com/codex` now **308**s to `learn.chatgpt.com/docs` — the
**general ChatGPT documentation hub**, not a Codex landing page. Its navigation
covers the API, the Agents SDK, Apps SDK, Commerce, and more; Codex is one
section among many. So link the specific pages above rather than sending anyone
to the root expecting to find Codex there.

The reorganisation is recent (pages carry "July 6–10, 2026" recency markers), so
treat these deep links as the likeliest thing in this file to rot.

## The five questions

**1. Which instruction files, in what order?**

**`AGENTS.md`, natively — it is the primary format.** There is no proprietary
Codex entry file.

Resolution order:

1. **Global** — in `$CODEX_HOME` (defaults to `~/.codex`): `AGENTS.override.md`
   if present, otherwise `AGENTS.md`. Only the first non-empty file at this
   level.
2. **Project** — from the project root (typically the git root) walking down to
   the working directory. Per directory: `AGENTS.override.md`, then `AGENTS.md`,
   then any name in `project_doc_fallback_filenames`. At most one file per
   directory.
3. **Merge** — concatenated root-down, joined with blank lines.

Capped by `project_doc_max_bytes`, **32 KiB by default**. A long entry file gets
truncated rather than rejected, which fails quietly — worth knowing before
writing a large one.

**Codex does not read `CLAUDE.md`.** The docs never say it does; do not claim it
does. What exists is a generic fallback: `project_doc_fallback_filenames`, which
is consulted **only when `AGENTS.md` is missing in that directory**. A user can
put any filename in it. Third-party posts show `CLAUDE.md` in that list — that
is somebody's configuration, not documented behaviour.

**2. Where do skills live?**

**`.agents/skills/` — not `.codex/skills/`.** This is a common wrong guess.
Documented paths: `$CWD/.agents/skills`, `$CWD/../.agents/skills`,
`$REPO_ROOT/.agents/skills`, `$HOME/.agents/skills`, and `/etc/codex/skills` for
admins.

**Mind the asymmetry**, because it catches people: skills live under `.agents/`,
while config (`.codex/config.toml`) and subagents (`~/.codex/agents/`,
`.codex/agents/`) live under `.codex/`.

**3. Where does MCP config go?**

In `config.toml`, under `[mcp_servers.<id>]`. There is also a CLI: `codex mcp
add`, `codex mcp list`, `codex mcp login`. Keep secrets out of the file — use
environment-variable indirection.

**4. Hooks?**

Yes. Ten events: `SessionStart`, `SubagentStart`, `PreToolUse`,
`PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`,
`UserPromptSubmit`, `SubagentStop`, `Stop`. Configured in `~/.codex/hooks.json`,
`<repo>/.codex/hooks.json`, or inline in either `config.toml`.

The names overlap with Claude Code's, which is a real convenience — but the sets
are **not** the same size, so a hook config is not portable between them without
checking.

**5. Rules, permissions, sandbox?**

- Config is **TOML**: `~/.codex/config.toml` (user), `.codex/config.toml`
  (project, trusted projects only). Profiles at
  `$CODEX_HOME/<profile>.config.toml`.
- `approval_policy`: `untrusted`, `on-request`, `never`, or a granular table
  form (`{ granular = { sandbox_approval, rules, mcp_elicitations,
  request_permissions, skill_approval } }`).
- `sandbox_mode`: `read-only`, `workspace-write`, `danger-full-access`.
- Subagents are **TOML** files in `~/.codex/agents/` or `.codex/agents/` — not
  markdown, unlike most other frameworks.

## What changes often

The doc URLs — this reorganisation is weeks old. Hook events and the config
schema. The `.agents/` vs `.codex/` split is the sort of thing that gets
consolidated eventually.

## Verify by fetching

The config keys, hook event names, and the default for
`project_doc_fallback_filenames` — the docs do not state that default, so do not
assume it is empty or that it contains anything in particular.
