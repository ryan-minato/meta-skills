# Antigravity CLI (and Gemini CLI, retired)

Google's agent. Notes verified **2026-07-15**.

**Read the warning below before you trust anything here — including this file.**
Antigravity is the one framework in this set whose documentation could not be
read by fetching, which makes it the easiest to get confidently wrong.

## The trap: this site returns 200 for everything

`antigravity.google` is a JavaScript app that serves the **same HTML shell for
any extensionless path**. Verified: `/docs/this-page-does-not-exist-xyz123` and
`/absolute/nonsense/qqqqq-zzzz-9999` both return **HTTP 200**, and the bytes are
identical to `/docs/home`, `/docs/skills`, and `/docs/mcp`.

Consequences you must internalise:

- **A 200 from this domain proves nothing.** Not that the page exists, not that
  it says what you think.
- **`/docs/skills` contains the word "skill" zero times.** So does `/docs/hooks`
  with "hook". They are a `<title>` and a script tag.
- Only *extensionless* paths get the shell — `/docs/skills.md` does return a
  real 404. That is the only place status codes mean anything here.

**Fetch these in a real browser, or with the product installed.** An agent that
reports Antigravity's hook events from a text fetch is reciting something it
found elsewhere, not reading the docs.

## What is actually verified

**`llms.txt` is real.** <https://antigravity.google/llms.txt> — plain text, ~10
KB, 117 lines. It is an **index of roughly 85 URLs with one-line descriptions
and no content whatsoever.**

It proves these URLs are **officially listed**, and roughly what each is *about*.
It proves nothing about what any of them *say*:

`/docs/home`, `/docs/settings`, `/docs/agent-settings`, `/docs/mcp`,
`/docs/skills`, `/docs/hooks`, `/docs/rules-workflows`, `/docs/subagents`,
`/docs/permissions`, `/docs/plugins`, `/docs/gcli-migration`, plus `/docs/cli/*`
and `/docs/ide/*` trees.

"The URL is listed" and "I read the content" are different facts. Keep them
apart.

**MCP configuration** — from a Google Codelab (`codelabs.developers.google.com`,
official, though a codelab rather than reference docs):

> "Antigravity 2.0, IDE, and CLI share a central MCP configuration in the file
> `~/.gemini/config/mcp_config.json`."

The key is `mcpServers`, confirmed by the codelab's own JSON example. Note it is
shared across **three** surfaces — 2.0, IDE, and CLI.

**`AGENTS.md` and `.agents/skills/` — verified, but read the scope carefully.**
From `ai.google.dev/gemini-api/docs/antigravity-agent`:

> "you can mount files like `AGENTS.md` for instructions and skills under
> `.agents/skills/` directly into the sandbox, or pass configuration inline at
> interaction time."

**That sentence is about mounting into a sandbox for the Gemini API's hosted
agent.** It is *not* a statement about where the Antigravity desktop IDE or CLI
reads files from disk. Do not turn it into one. It is good evidence that
Antigravity's world uses `AGENTS.md` and `.agents/skills/`; it is not evidence of
a local path.

## What could not be verified — do not guess these

- **Hook event names.** **This is a known contamination trap.** A web search
  returns `PreToolUse`, `PostToolUse`, `PreInvocation`, `Stop` with great
  confidence. **Those are Claude Code's event names**, bleeding in from pages
  about a different product. The official Antigravity Python SDK uses nothing of
  the sort — its taxonomy is `PreToolCallDecideHook`, `PostToolCallHook`,
  `OnToolErrorHook`, `OnInteractionHook`. And even those are the **Python SDK's**
  hooks, not CLI or IDE hook configuration, so they do not transfer either.
- **Permission keys.**
- **Subagent format.**
- **The settings schema.**
- **Whether a `~/.antigravity/` exists.** Blog and Medium posts offer
  `~/.config/antigravity/config.toml` and `~/.gemini/antigravity-cli/settings.json`.
  Unverified. Do not ship them.

For any of these: **open the listed URL in a browser and read it.** If you cannot,
say so to the user and leave the config unwritten rather than guessing. A wrong
path here is worse than an admitted gap, because it looks like it works.

## Gemini CLI is retired — check before writing for it

Verified from Google's own blog (published **2026-05-19**):

> "On June 18, 2026, Gemini CLI and Gemini Code Assist IDE extensions will stop
> serving requests for Google AI Pro and Ultra, as well as those using it free of
> charge using Gemini Code Assist for individuals"

**That date has passed.** For most users this product no longer serves requests.

**Access continues** for: Gemini Code Assist **Standard or Enterprise** licences;
organisations using Gemini Code Assist for GitHub through Google Cloud; and paid
Gemini and Gemini Enterprise Agent Platform API keys. So it is not dead — but
writing Gemini-CLI-first guidance now serves a shrinking, licensed minority. Ask
before assuming a team is in it.

Carried into Antigravity CLI: *"Agent Skills, Hooks, Subagents, and Extensions
(now as Antigravity plugins)."*

### Gemini CLI, if you must

Docs: <https://geminicli.com/docs/> — despite looking third-party, this is
official: the `google-gemini/gemini-cli` README links it as its docs home. It
carries a deprecation banner, and unlike `antigravity.google` it returns **real
404s**, so status codes are meaningful.

**Entry file is `GEMINI.md`.** `AGENTS.md` is **not native** — it works only as
an opt-in alias:

```json
{ "context": { "fileName": ["AGENTS.md", "CONTEXT.md", "GEMINI.md"] } }
```

`AGENTS.md` appears nowhere in the configuration reference; it shows up in the
docs only as an example value in that array. Config-driven aliasing is not native
support, and a project relying on it silently breaks for anyone without that
setting.

**Settings: four files, and two of them are system-level at opposite ends of
precedence.** Lowest to highest:

1. Defaults
2. **System defaults** — `/etc/gemini-cli/system-defaults.json`,
   `C:\ProgramData\gemini-cli\system-defaults.json`,
   `/Library/Application Support/GeminiCli/system-defaults.json`
3. User — `~/.gemini/settings.json`
4. Project — `.gemini/settings.json`
5. **System settings** — `/etc/gemini-cli/settings.json`,
   `C:\ProgramData\gemini-cli\settings.json`,
   `/Library/Application Support/GeminiCli/settings.json`
6. Environment variables
7. CLI arguments

**System settings override the project**, which is the reverse of every other
framework here:

> "System settings act as overrides, taking precedence over all other settings
> files. May be useful for system administrators at enterprises to have controls
> over users"

A project setting that "does not work" on a managed machine is probably this.

## The relationship: shared directory, different layout

Antigravity **inherited `~/.gemini/`** rather than creating its own directory —
but reorganised inside it. Gemini CLI uses `~/.gemini/settings.json`; Antigravity
uses `~/.gemini/config/mcp_config.json`. **The directory is shared; the file
layout is not.** Finding `~/.gemini/` on a machine tells you nothing about which
product put it there.

The entry file also moved: `GEMINI.md` → `AGENTS.md`, converging with Codex and
OpenCode and away from Gemini CLI's proprietary format.

## Verify by fetching

All of it, in a browser. This file is a map of where to look and a record of what
is already known to be wrong. It is not a substitute for the documentation, and
on this framework more than any other, the gap between the two is where the
fabrications live.
