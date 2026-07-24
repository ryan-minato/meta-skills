# meta-skills

A public library of **disposable meta-skills**: one-time scaffolding a target
project installs, uses to build that project's agent harness, then deletes to
reclaim context. Sibling of `ryan-minato/skills`, which ships durable skills;
this repository's products are designed to vanish.

## Two Audiences — Read This First

Two disjoint groups read material from this repository, and each must ignore
the other's rules.

- **`skills/**` is the product.** It is written for agents in *target*
  projects. Everything inside it — including the words "disposable" and
  "delete" — addresses that audience, in that project, after their harness
  is built. It is never a description of this repository.
- **Everything else is this repository's durable harness**: this file,
  `ARCHITECTURE.md`, `.agents/`, `scripts/`, `justfile`, CI. Never delete or
  "clean up" repository files because a skill description says it is
  disposable — and never carry this repository's conventions (bilingual
  READMEs, Linear, `just check`) into a published skill's instructions.

The full product contract, including the marker that identifies a published
skill, is [meta-skill-contract.md](.agents/knowledge/meta-skill-contract.md).

## Layout

`skills/<catalog>/<skill>/SKILL.md` is the product; only skill directories
ship to targets. The project map lives in [ARCHITECTURE.md](ARCHITECTURE.md).

## Conventions

- English everywhere; every `README.md` has a mirrored `README.zh.md`, with
  English authoritative.
- Published skill directories are named `meta-*`. The prefix only groups the
  file tree — identification is by the description marker, never by name,
  because installers rename skills.
- Commits: Conventional Commits, English. Scope is the catalog changed
  (`feat(core): …`); omit the scope when no catalog is touched (`docs: …`).
- Commit under a noreply identity; personal email addresses never enter the
  history (the hooks enforce this).

## Validation

| Command | Does |
|---|---|
| `just setup` | install hooks and the commit template; once after cloning |
| `just check` | every gate — run it before proposing changes |
| `just validate-repo` | repository structure: catalogs, docs, contract |
| `just check-skill <path>` | one skill: structure, SKILL.md, dependencies, links |
| `just check-skills` | every published and internal skill |
| `just validate` | both validators (fast iteration) |
| `just fmt` | format and autofix the validator scripts |

Both validators self-test on every run, and their messages say what failed,
why it matters, and the fix. Errors block; warnings advise. Fix the cause,
never the check — unless the contract itself changed.

## Commit Gates

Before every commit: `just check` is green, the commit is one logical
change, and you have read the staged diff yourself for secrets and personal
data. A secret ever committed is leaked even if a later commit removes it —
stop and tell the user. Never use `--no-verify`.

## Workflow

Every tracked change starts from a Linear root issue and ends in a
human-reviewed pull request; the ordered procedure — sub-issues, branch
naming, draft-to-ready gating, and the fallbacks when Linear or GitHub is
unavailable — is the `tracked-change-workflow` skill. Invoke it when
starting tracked work. Agents never merge.

## When To Read What

| Situation | Read |
|---|---|
| Repo layout, quality gates, why a mechanism is absent, proposing tooling | [ARCHITECTURE.md](ARCHITECTURE.md) |
| Authoring, reviewing, renaming, removing, or declaring dependencies for anything under `skills/`; touching the marker | [meta-skill-contract.md](.agents/knowledge/meta-skill-contract.md) |
| Working inside a specific catalog | that catalog's `CONTEXT.md` |
| Agent Skills spec facts (frontmatter fields, limits) | the `agentskills` MCP server |

## Keeping The Harness Current

Sync is owned by skills, one per concern: `sync-catalog` (a catalog or
published skill is added, renamed, or removed, including the live discovery
sources), `sync-contract` (the marker or its rules change), and
`sync-translation` (a `README.md` changed). Invoke the one whose trigger
fired; their procedures are not duplicated here.

For the concerns no skill owns: a justfile recipe change updates the
Validation table above and the gates table in `ARCHITECTURE.md`; a layout
change updates `ARCHITECTURE.md`'s map; a new or changed validator check
ships its self-test fixture in the same change; a changed team workflow
decision updates the `tracked-change-workflow` skill.

## Environment

The devcontainer is fully isolated, so commands inside it need no
per-command approval. Run `just setup` once after cloning. Toolchain:
`just`, `uv`, `ruff`, `pre-commit`, `node`, `gh`. MCP servers:
`linear-server`, `agentskills`, and `github` (needs `GH_TOKEN` from the host
environment).
