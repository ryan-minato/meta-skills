# GitHub Copilot

Notes verified **2026-07-15**. Fetch before you write.

## Fetch these first

**There is no single doc root.** Copilot is documented across two sites, and
which one is authoritative depends on the surface:

- **`code.visualstudio.com`** — the editor surface.
- **`docs.github.com`** — the CLI, the cloud coding agent, and org policy.

| What | URL |
|---|---|
| Response customization | <https://docs.github.com/en/copilot/concepts/prompting/response-customization> |
| CLI custom instructions | <https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions> |
| Hooks reference | <https://docs.github.com/en/copilot/reference/hooks-reference> |
| Cloud agent MCP | <https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp> |
| VS Code custom instructions | <https://code.visualstudio.com/docs/agent-customization/custom-instructions> |
| VS Code custom agents | <https://code.visualstudio.com/docs/agent-customization/custom-agents> |
| VS Code MCP | <https://code.visualstudio.com/docs/agent-customization/mcp-servers> |

The VS Code paths were reorganised: `/docs/copilot/customization/*` now
redirects to `/docs/agent-customization/*`. Write the new form.

## The five questions

**1. Which instruction files, in what order?**

Copilot reads `.github/copilot-instructions.md`, path-scoped
`.github/instructions/**/*.instructions.md` (with an `applyTo` glob in
frontmatter), and **also** `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md`.

Caveat straight from the docs: agent instruction files are *"currently not
supported by all Copilot features."* Do not assume a rule in `AGENTS.md` reaches
every Copilot surface.

In VS Code these are gated behind settings — `chat.useAgentsMdFile`,
`chat.useClaudeMdFile`, and the experimental `chat.useNestedAgentsMdFiles`. An
`AGENTS.md` that works for a teammate on Codex may simply be switched off here.

Precedence per `docs.github.com`, highest first: **personal → repository →
organization**, where repository resolves path-specific `.instructions.md`, then
`.github/copilot-instructions.md`, then agent instructions such as `AGENTS.md`.

**Copilot CLI deliberately refuses to define one**, and the wording matters:

> "When multiple applicable user-level and repository instruction files exist,
> Copilot CLI combines their instructions. It removes duplicate copies of
> identical user-level copilot-instructions.md, repository-wide, and agent
> instructions, but does not define a general precedence order between these
> files."

So do not write conflicting rules across files and expect one to win — for the
CLI, nothing wins. Keep one file authoritative and have the rest point at it.

**2. Where do skills and agents live?**

Custom agents: `.github/agents/*.agent.md`, `.claude/agents`, `~/.copilot/agents`.
More locations via `chat.agentFilesLocations`.

**Terminology changed — do not write "chat modes":**

> "Custom agents were previously known as custom chat modes. The functionality
> remains the same, but the terminology has been updated…"

> "If you have existing `.chatmode.md` files, rename them to `.agent.md`…"

The rename is manual. An existing `.chatmode.md` does not migrate itself.

**3. Where does MCP config go?**

**Two surfaces, two shapes, and the key names differ. This is the easiest thing
to get wrong here.**

| Surface | Where | Top-level key |
|---|---|---|
| VS Code | `.vscode/mcp.json` | **`servers`** |
| Cloud coding agent | the **repository settings web UI** — Settings → Code & automation → Copilot → MCP servers | **`mcpServers`** |

The cloud agent's config is not a file in the repo at all. Do not try to commit
one.

**4. Hooks?**

Yes, but **on two surfaces only**:

> "Hooks are supported in two Copilot surfaces: Copilot CLI and Copilot cloud
> agent."

The CLI supports the full event set. The cloud agent fires only a subset, honours
only `bash`/`command` entries, and does not support policy hooks.

Events: `preToolUse`, `postToolUse`, `postToolUseFailure`, `preCompact`,
`sessionStart`, `sessionEnd`, `agentStop`, `subagentStart`, `subagentStop`,
`userPromptSubmitted`, `errorOccurred`, `permissionRequest`, `notification`.

Each has a PascalCase payload form for VS Code-extension compatibility — the
same event, a second format, not a separate event. **Two do not transliterate
mechanically**: `agentStop` is `Stop`, and `userPromptSubmitted` is
`UserPromptSubmit`. Deriving them by capitalising the first letter produces names
that do not exist.

Paths: `.github/hooks/*.json` (repo), `~/.copilot/hooks/` or
`$COPILOT_HOME/hooks/` (user), `.github/copilot/settings.json` and
`settings.local.json`, plus policy at `/etc/github-copilot/policy.d/*.json`
(Linux/macOS) or `C:\ProgramData\GitHub\Copilot\policy.d\*.json` (Windows).

**5. Rules, permissions, sandbox?**

Org-level policy lives in the `policy.d` paths above. The cloud coding agent runs
in an ephemeral Linux sandbox. Fetch the pages for current specifics — this
surface moves.

## What changes often

Terminology (chat modes → custom agents happened recently), the VS Code doc
paths (already redirected once), and which features honour `AGENTS.md`. The
two-site split means a fact can be current on one and stale on the other.

## Verify by fetching

The hook event list and per-surface support, the VS Code gating settings, and the
MCP key name for the surface you are actually targeting — `servers` and
`mcpServers` are both correct, for different things.
