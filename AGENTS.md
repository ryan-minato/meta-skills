# Meta Skills Agent Guide

## Purpose

Meta Skills develops disposable, English-first meta-skills that let an agent
scaffold a durable, project-specific harness. This repository is the harness
for creating those future public skills; it does not yet publish any public
skill or catalog.

## Start here

1. Read this file first. It is the only discovery root.
2. Read [DESIGN.md](DESIGN.md) for product scope, profiles, and lifecycle.
3. Read [ARCHITECTURE.md](ARCHITECTURE.md) before changing layout or tooling.
4. Read the relevant file in `.agents/knowledge/` before authoring skills,
   changing markers, or using an external integration.
5. Run `just check` before proposing a handoff or commit.

`CLAUDE.md` intentionally points here. `.claude/skills` is a relative symlink
to `.agents/skills`; do not duplicate skills for another client.

## Repository map

| Path | Responsibility |
| --- | --- |
| `DESIGN.md` | Product contract and user-facing lifecycle |
| `ARCHITECTURE.md` | Directory, adapter, and source-of-truth contract |
| `.agents/knowledge/` | Durable authoring, lifecycle, and source guidance |
| `.agents/skills/` | Internal project workflows only |
| `.agents/mcp-servers.json` | Credential-free MCP declaration source |
| `scripts/` | Stdlib-first validators and deterministic generators |
| `tests/` | Unit fixtures for repository contracts |
| `.github/workflows/` | Required CI and history safety gates |

## Working rules

- Treat Git's default branch as the authoritative knowledge source. Linear
  tracks delivery; `knowledge-sync` only mirrors already-merged knowledge.
- Use `just` commands rather than inventing alternate check sequences.
- Keep changes focused, reversible, English-first, and free of credentials.
- Public meta-skills belong in future `skills/<catalog>/<skill>/` directories.
  Do not create an empty public catalog or marketplace in this bootstrap.
- Internal workflow skills carry `metadata.internal: "true"` and must never
  carry META-SKILL markers.
- Future public meta-skills must carry both lifecycle markers described in
  `.agents/knowledge/meta-skill-lifecycle.md`.
- Do not implement unattended maintenance, self-modifying knowledge, or any
  L3/L4 autonomy. This repository is a human-supervised L2 harness.

## Delivery workflow

Use `.agents/skills/issue-workflow/SKILL.md` for a Linear-backed change.
Resolve the team and project dynamically; the active project is **Meta Skills**
in the Aoi team. Create or link the issue before code changes. Use its Linear
branch name when creating a branch from the current default branch.

Every commit must use scoped Conventional Commits:

`<type>(<scope>)[!]: <description>`

Scopes are mandatory. Use a public skill name for public-skill work; otherwise
use an approved repository scope such as `harness`, `environment`, `knowledge`,
`quality`, `ci`, `readme`, or `catalogs`. The subject is English, imperative,
lowercase, no longer than 50 characters, and has no trailing period. Never use
`--no-verify`.

Post an English milestone comment and set a child issue Done only after its
focused commit succeeds. Keep a parent issue In Progress; Linear/GitHub
integration closes it after merge. A failed PR creation after a successful push
requires a blocker comment and a rendered PR title/body for the human; do not
move the parent to In Review without a user-confirmed PR URL.

## Commands

| Command | Use |
| --- | --- |
| `just setup` | Install local Git hooks and commit template |
| `just validate` | Validate skills, MCP adapters, and local links |
| `just test` | Run stdlib unit tests |
| `just lint` | Check Python style and formatting |
| `just check-skill <path>...` | Validate one or more skill directories |
| `just sync-mcp --check` | Detect generated MCP adapter drift |
| `just gen-marketplace --check` | Check future marketplace output |
| `just commit-gate` | Scan staged changes and committer identity |
| `just check` | Run the complete repository gate |

## Read by task

| Task | Required reading |
| --- | --- |
| Add or revise a skill | `.agents/knowledge/skill-quality.md` and `skill-authoring` |
| Add public scaffolding | `meta-skill-lifecycle.md` and `ARCHITECTURE.md` |
| Change MCP config | `ARCHITECTURE.md`, then run `just sync-mcp --check` |
| Change knowledge docs | `knowledge-sync` before mirroring to Linear |
| Change CI or hooks | `ARCHITECTURE.md`, then `just check` |

## Human boundaries

Humans choose the target profile and topic set, confirm removal of meta-skills,
review pull requests, and merge. Agents may implement, validate, update Linear,
commit, push, and attempt a draft PR only within that approved workflow.
