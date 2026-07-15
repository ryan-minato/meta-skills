# Claude Code

Anthropic's coding agent. Notes verified **2026-07-15**. Fetch before you write.

## Fetch these first

| What | URL |
|---|---|
| **Doc index, machine-readable** | <https://code.claude.com/docs/llms.txt> |
| Overview | <https://code.claude.com/docs/en/overview> |
| Settings | <https://code.claude.com/docs/en/settings> |
| Entry file | <https://code.claude.com/docs/en/memory> |
| MCP | <https://code.claude.com/docs/en/mcp> |
| Hooks | <https://code.claude.com/docs/en/hooks> |
| Skills | <https://code.claude.com/docs/en/skills> |
| Subagents | <https://code.claude.com/docs/en/sub-agents> |
| Permissions | <https://code.claude.com/docs/en/permissions> |
| Sandboxing | <https://code.claude.com/docs/en/sandboxing> |

`llms.txt` is the best anchor here: a plain-text index of every doc page as a
`.md` URL. Start there rather than guessing a path — and every page also serves
clean markdown by appending `.md`.

**The domain moved.** `docs.claude.com/en/docs/claude-code/*` now **301**s to
`code.claude.com/docs/en/*`. Old links still work; write the new ones.

## The five questions

**1. Which instruction files, in what order?**

**`CLAUDE.md`. Not `AGENTS.md`.** The docs are blunt about it:

> "Claude Code reads `CLAUDE.md`, not `AGENTS.md`."

This is the sharpest divergence in the landscape and the single easiest thing to
get wrong. Every other major framework reads `AGENTS.md` natively.

Two documented workarounds. An import inside `CLAUDE.md` — preferred, and the
only one that works on Windows:

```markdown
@AGENTS.md

## Claude Code

<Claude-specific additions go here.>
```

Or a symlink, when you need no Claude-specific content: `ln -s AGENTS.md
CLAUDE.md`. On Windows a symlink needs Administrator or Developer Mode, so use
the import.

Load order, broadest to most specific:

1. Managed policy — `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS),
   `/etc/claude-code/CLAUDE.md` (Linux/WSL),
   `C:\Program Files\ClaudeCode\CLAUDE.md` (Windows)
2. User — `~/.claude/CLAUDE.md`
3. Project — `./CLAUDE.md` or `./.claude/CLAUDE.md`
4. Local — `./CLAUDE.local.md`

**This is not override precedence.** All discovered files are **concatenated**
into context rather than replacing one another; Claude walks up the tree, and
`CLAUDE.local.md` is appended after `CLAUDE.md` within a directory. Do not write
a "more specific file wins" rule — nothing wins, everything accumulates. Two
files that contradict each other both arrive, and the model picks.

**2. Where do skills live?**

- Personal — `~/.claude/skills/<name>/SKILL.md`
- Project — `.claude/skills/<name>/SKILL.md`
- Plugin — `<plugin>/skills/<name>/SKILL.md`

Nested `.claude/skills/` below the working directory also load. On a name
collision: enterprise overrides personal, personal overrides project.

**3. Where does MCP config go?**

`.mcp.json` at the project root; `~/.claude.json` for user scope. Prefer project
scope, and keep secrets out of it — reference an environment variable instead.

**4. Hooks?**

Yes, and extensively — the hooks reference documents around **30** events,
including `SessionStart`, `PreToolUse`, `PostToolUse`, `UserPromptSubmit`,
`Stop`, `PreCompact`, plus many Claude Code has that others do not (`Setup`,
`PostToolUseFailure`, `InstructionsLoaded`, `WorktreeCreate`, `SessionEnd`).
Configured in `settings.json`. **Fetch the page for the current list** — this is
the fastest-moving surface here.

**5. Rules, permissions, sandbox?**

- Settings: `~/.claude/settings.json` (user), `.claude/settings.json` (project),
  `.claude/settings.local.json` (local, gitignored), plus managed files at the
  policy paths above.
- Precedence, highest first: **managed → CLI arguments → local → project →
  user**. One exception the docs call out: **permission rules merge** across
  scopes rather than override.
- `.claude/rules/*.md`, with optional `paths:` frontmatter for path-scoped
  loading.
- Sandboxing is OS-level (Seatbelt, bubblewrap): macOS, Linux, WSL2 — **not
  native Windows**.

## What changes often

Hook events, and the settings schema. The doc domain itself moved recently. The
entry-file rule (`CLAUDE.md`, not `AGENTS.md`) has been stable and is the one
thing here worth relying on between fetches.

## Verify by fetching

Hook event names, the settings key schema, and the exact managed-policy paths
for the platform you are targeting. Everything in this file is a starting point
for a fetch, not a substitute for one.
