# meta-skills

A library of **disposable meta-skills**: an agent installs them into a target
project, uses them to build that project's harness, then deletes them.

## Two Audiences — Read This First

Material from this repository is read by two disjoint groups. Each must ignore
the other's rules.

| | Agents working **in this repo** | Agents in a **target project** |
|---|---|---|
| Read | this file, `ARCHITECTURE.md`, `.agents/`, catalog `CONTEXT.md` | only the installed `SKILL.md` files |
| Job | author and review meta-skills | build *that* project's harness, then delete the meta-skills |
| Harness | already built — **do not build one here** | does not exist yet; that is the job |

- **Product rules never leak inward.** The marker, self-containment, and disposal
  apply to `skills/**` only. This repo's `.agents/skills/` are durable; marking
  one would let a cleanup pass delete this repo's own harness.
- **Repo rules never leak outward.** Catalogs, bilingual READMEs, the Linear
  workflow, and `just check` are this repository's conventions. A meta-skill must
  never impose them on a target project.

You are almost certainly in the first column. This repo's *subject* is
harness-building; that does not mean your task is to build one here.

## Purpose

A meta-skill is one-time scaffolding, not a durable project skill. A user copies
a catalog into a target project, hands that project's requirements to an agent
and asks for a harness, the agent invokes the meta-skills to build it, and once
the harness is verified the agent **deletes them** to reclaim context.

Everything else follows from that last step: a meta-skill must be findable in
order to be removed, and must leave nothing behind that depends on it.

## Catalogs

`core` is the only catalog today. The authoritative list, and the repository
layout, live in [ARCHITECTURE.md](ARCHITECTURE.md) — the validator parses that
list, and it defines the legal commit scopes.

## Core Conventions

- **The marker.** Every published skill's resolved `description` begins with
  `[META-SKILL: remove after harness setup] ` (41 chars, trailing space).
  Identification is by **description, never by name** — installers rename skills
  to avoid collisions, so the name channel cannot be trusted; the `meta-` name
  prefix only groups the file tree. `[` opens a YAML flow sequence, so a plain
  scalar is invalid YAML: use `description: >` and let the fold supply the
  trailing space. Never type that space; never leave a blank line after the
  marker.
- **Self-containment.** Installed skills lose everything outside their own
  directory. No relative link may escape the skill root; no skill may depend on a
  sibling's behavior. Keep `README.md` out of a skill root.
- **Layout.** `skills/<catalog>/<skill>/SKILL.md`. Every catalog carries
  `CONTEXT.md`, `README.md`, and `README.zh.md`. Read a catalog's `CONTEXT.md`
  before changing anything in it.
- **Language.** English is authoritative; every `README.md` has a mirrored
  `README.zh.md`.
- **Commits.** Conventional Commits, English. **Scope is the catalog changed**
  (`feat(core): …`); omit the scope when the change belongs to no catalog, such
  as the harness itself (`docs: …`).
- **Gates.** Run `just check` before proposing changes. Never `--no-verify`: the
  hooks are the secret and PII gate, and a secret committed is leaked even if a
  later commit removes it.

## When To Read What

| Situation | Read |
|---|---|
| Authoring, reviewing, renaming, or removing anything under `skills/` | [meta-skill-contract.md](.agents/knowledge/meta-skill-contract.md) |
| Starting or landing a tracked change | [contribution-workflow.md](.agents/knowledge/contribution-workflow.md) |
| Repo layout, the catalog list, or why a mechanism is absent | [ARCHITECTURE.md](ARCHITECTURE.md) |
| Deciding whether a skill belongs in a catalog | that catalog's `CONTEXT.md` |
| Agent Skills spec questions | the `agentskills` MCP server |

## Development Environment

- The devcontainer is the expected environment and is fully isolated, so commands
  inside it need no per-command approval. Run `just setup` once after cloning.
- Toolchain: `just`, `uv`, `ruff`, `pre-commit`, `node`, `gh`.
- The GitHub MCP server reads `GH_TOKEN` from the host environment. Unset, it
  fails; Linear and `agentskills` still work.

## Validation

| Check | Command |
|---|---|
| Everything (use this before proposing changes) | `just check` |
| Project file structure | `just validate-repo` |
| Every skill | `just check-skills` |
| One skill | `just check-skill <path>` |
| Prove the marker and link checks fire | `just selftest` |
| Lint `scripts/` | `just lint` |

When a `just` recipe changes, update this table and the Quality Gates table in
`ARCHITECTURE.md`.

## Workflow

Linear issue → branch from the **root** issue → atomic commits → pull request.
Only the root issue gets a pull request. Read
[contribution-workflow.md](.agents/knowledge/contribution-workflow.md) for issue
structure, labels, progress reporting, and the fallbacks when Linear or GitHub
auth is unavailable.

Agents may create and update Linear issues, push branches, and open pull
requests. Humans own merging, releases, and what enters a catalog.

## Keeping The Harness Current

Sync is owned by skills, one per concern: `sync-catalog` (a catalog or skill is
added, renamed, or removed), `sync-translation` (a `README.md` changed), and
`sync-contract` (the marker contract changed). They announce themselves; invoke
the one whose trigger fired, and do not duplicate their rules here.
