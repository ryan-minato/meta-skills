# OpenCode

Notes verified **2026-07-15**. Fetch before you write.

## Fetch these first

| What | URL |
|---|---|
| Docs root | <https://opencode.ai/docs/> |
| Config | <https://opencode.ai/docs/config/> |
| MCP | <https://opencode.ai/docs/mcp-servers/> |
| Entry file | <https://opencode.ai/docs/rules/> |
| Agents | <https://opencode.ai/docs/agents/> |
| Skills | <https://opencode.ai/docs/skills/> |
| Plugins | <https://opencode.ai/docs/plugins/> |
| Permissions | <https://opencode.ai/docs/permissions/> |
| **Config JSON Schema** | <https://opencode.ai/config.json> |

The config schema is the best anchor here: a real JSON Schema (draft 2020-12),
machine-readable, and more current than any prose. Fetch it when you need a key
name. There is a second schema for the TUI at <https://opencode.ai/tui.json>.

## The five questions

**1. Which instruction files, in what order?**

`AGENTS.md`, natively and primarily. Lookup order: local files walking **up** the
tree (`AGENTS.md`, `CLAUDE.md`) → `~/.config/opencode/AGENTS.md` →
`~/.claude/CLAUDE.md`.

The rule that surprises people, verbatim:

> "The first matching file wins in each category. For example, if you have both
> `AGENTS.md` and `CLAUDE.md`, only `AGENTS.md` is used."

**Not concatenated — the first match wins.** So a project carrying both files
has a `CLAUDE.md` that OpenCode never opens, while Claude Code reads *only* that
file. The same two files, two frameworks, and no overlap in what gets read. If a
project serves both, one file must be authoritative and the other must point at
it.

`CLAUDE.md` is read as an explicit compatibility shim, not a native format:

> "For users migrating from Claude Code, OpenCode supports Claude Code's file
> conventions as fallbacks"

Disable with `OPENCODE_DISABLE_CLAUDE_CODE=1`. Extra files can be pulled in via
`instructions: []` (globs, and remote URLs with a 5s timeout).

**2. Where do skills live?**

The widest discovery of any framework here — it reads three conventions:

- `.opencode/skills/<name>/SKILL.md` and `~/.config/opencode/skills/<name>/SKILL.md`
- `.claude/skills/<name>/SKILL.md` and `~/.claude/skills/<name>/SKILL.md`
- `.agents/skills/<name>/SKILL.md` and `~/.agents/skills/<name>/SKILL.md`

Project paths walk up until they reach the git worktree. Note the directories are
**plural** — `.opencode/skills/`, `.opencode/agents/`, `.opencode/plugins/`.

**3. Where does MCP config go?**

In `opencode.json` (project) or `~/.config/opencode/opencode.json` (global).
JSON and JSONC are both accepted. Keep secrets out — use environment-variable
indirection.

**4. Hooks?**

**There is no hooks feature.** `/docs/hooks/` returns 404 and there is no such
page; lifecycle events fold into the **plugin** system instead (`tool.execute.before`
and `.after`, `session.*`, `permission.*`, `file.edited`, compaction hooks).

If a harness design depends on hooks, this is the framework that will not have
them, and a plugin is the answer.

**5. Rules, permissions, sandbox?**

- Config: `opencode.json` / `opencode.jsonc` (project),
  `~/.config/opencode/opencode.json` (global). Env overrides:
  `OPENCODE_CONFIG`, `OPENCODE_CONFIG_DIR`, `OPENCODE_CONFIG_CONTENT`.
- Precedence — *"later sources override earlier ones"*: remote
  (`.well-known/opencode`) → global → `OPENCODE_CONFIG` → project → `.opencode`
  dirs → `OPENCODE_CONFIG_CONTENT` → managed config → macOS managed preferences.
  **Configs merge rather than replace.**
- Permissions: the `permission` key, with `allow` (run without approval), `ask`
  (prompt), `deny` (block). Wildcards work — `*` for zero or more characters,
  `?` for exactly one:

  ```json
  { "permission": { "bash": { "*": "ask", "git *": "allow", "rm *": "deny" } } }
  ```

  The legacy boolean `tools` config is deprecated and merged into `permission`.
  The `--auto` flag approves anything not explicitly denied.
- **Sandboxing: the docs describe none.** The documented isolation model is
  approval-based (`permission`). Be careful how you state this — the docs are
  *silent* on sandboxing rather than declaring its absence, so "OpenCode has no
  sandbox" is an inference, not a quote. What is safe to say: nothing in the
  documentation describes a sandboxing mechanism, and the permission system is
  what stands between an agent and the machine. If isolation matters for a
  project, that is a question to put to the user rather than an assumption to
  make either way.

## What changes often

The permission model consolidated recently (`tools` → `permission`). Plugin
lifecycle event names. The docs are the most complete and best-structured of the
group, and the JSON Schema makes drift easy to catch.

## Verify by fetching

Plugin event names and the permission key set — take them from
<https://opencode.ai/config.json> rather than from prose, since the schema is
what the tool actually enforces.
