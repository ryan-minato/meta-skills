---
name: meta-framework-wiring
description: >
  [META-SKILL: remove after harness setup]
  Wires a harness into the coding-agent frameworks a project serves: which file
  each one reads first, where its skills and MCP config go, what hooks and
  permission settings it has — fetching each vendor's current documentation
  rather than trusting notes that go stale. Covers Claude Code, Codex, GitHub
  Copilot, Antigravity, and OpenCode. Use when placing MCP or skill
  configuration, or asking where a framework reads its instructions from. Not
  for deciding which frameworks to serve, and not for what the instructions say.
---

# Framework Wiring

Every coding agent reads a different file, from a different place, with
different rules. This is where those differences live.

## Fetch first. These notes are an index, not an answer.

The bundled references are **a map of where to look and what to watch for**.
They are dated. Config formats change faster than this scaffolding's shelf life,
and two of these vendors moved their entire documentation domain in the weeks
before it was written.

So: **read the reference, then fetch its URLs, then write the config.** In that
order. The reference tells you which page matters and which claim has already
been wrong; the page tells you what is true today.

**No fetch capability?** (offline, air-gapped, no network tool.) Then say so:

> I cannot reach the vendor docs, so I am using notes dated 2026-07-15. The
> shape is stable but specifics may have moved — please check `<url>` before
> relying on this config.

Write the config from the dated shape, mark it unverified, and move on. What you
must not do is present stale notes as current fact.

## The five questions

Every framework answers the same five. This list is the durable part — a
framework not in the table below is handled by asking these of its own docs.

1. **Which instruction file does it read, and in what order?** Does it merge
   files or take the first match? Is `AGENTS.md` native, aliased, or ignored?
2. **Where do skills live, and are they discovered automatically?**
3. **Where does MCP configuration go, and at what scope?**
4. **What lifecycle hooks exist, if any?**
5. **What rules, permissions, or sandboxing does it have?**

## Which reference to read

Take the framework list from the project's decision — what the team actually
uses. If that is not settled, ask; do not infer it from a stray config
directory. An empty `.claude/` proves somebody tried something once.

| Framework | Reference |
|---|---|
| Claude Code | [claude-code.md](references/claude-code.md) |
| OpenAI Codex | [codex.md](references/codex.md) |
| GitHub Copilot | [copilot.md](references/copilot.md) |
| Antigravity CLI (and Gemini CLI, retired) | [antigravity.md](references/antigravity.md) |
| OpenCode | [opencode.md](references/opencode.md) |
| **Anything else** | Ask the five questions of its own documentation. Find the vendor's docs, prefer a machine-readable index (`llms.txt`, a JSON Schema) over prose, and write the config from what you read. |

## Rules that hold across all of them

**One entry file is authoritative; everything else points at it.** Pick the file
the most tools read natively — `AGENTS.md`, in practice — and make every other
entry file a pointer to it. Do not maintain parallel copies. They drift, and
then agents follow whichever one they happened to read.

**The exception is real and unavoidable: Claude Code does not read `AGENTS.md`.**
It reads `CLAUDE.md`. Serve both with an `@AGENTS.md` import inside `CLAUDE.md`,
or a symlink. This is the single most common wiring mistake.

**Never duplicate a rule across per-framework files.** A rule in two places is a
rule that will disagree with itself within a month.

**Never commit a secret in MCP config.** Reference an environment variable. This
holds for every framework and every scope, without exception.

**Prefer project scope to user scope.** A project-scoped config travels with the
repository and works for the next person. A user-scoped one works on your
machine and nowhere else.

**Record what you wired, in the entrypoint.** A config file nobody knows about
is a config file nobody maintains.

## After writing

- The entry file the team's tool actually reads has the content in it — not a
  sibling file it never opens.
- No secret is in any committed config.
- The entrypoint mentions what was wired and where.
- Anything you could not verify is flagged to the user, not quietly guessed.

## Gotchas

- **A 200 is not verification.** At least one vendor's site returns 200 with an
  identical page for every path, including nonsense ones. Check that the content
  is about what you asked for, not merely that something came back.
- **Search results contaminate across frameworks.** These products have
  overlapping vocabulary — `PreToolUse`, `Stop`, `SessionStart` — and a search
  for one framework's hooks will confidently return another's. If a fact did not
  come from the vendor's own page, it is not a fact yet.
- **Hooks are not portable.** Names overlap between frameworks, sets do not
  match, and one framework here has no hooks at all. Rely on them only where the
  whole team uses one tool.
- **A per-framework file that restates `AGENTS.md` will drift.** Point, do not
  copy.
- **"Could not verify" is a finding worth reporting**, not a gap to paper over.
  A wrong path looks like it works right up until it does not.
