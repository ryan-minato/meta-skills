# Architecture

The project map: layout, catalogs, quality gates, and what is deliberately
absent. [AGENTS.md](AGENTS.md) is the entrypoint; this file carries the map
so the entrypoint stays a thin router.

## Layout

```text
AGENTS.md                  <- entrypoint; every rule reachable from it
CLAUDE.md                  <- @AGENTS.md
.claude-plugin/marketplace.json <- Claude Code marketplace: one plugin per catalog
ARCHITECTURE.md            <- this file
README.md / README.zh.md   <- public front door (English authoritative)
.agents/knowledge/         <- agent-facing knowledge, loaded on demand
.agents/skills/            <- this repo's own durable skills (never published)
.claude/skills             <- symlink to ../.agents/skills for Claude Code
skills/<catalog>/          <- published catalogs: CONTEXT.md + README pair
skills/<catalog>/<skill>/  <- a published skill: SKILL.md [+ references/ scripts/ assets/]
scripts/validate_repo.py   <- repository validator: catalogs, docs, contract
scripts/check_skill.py     <- per-skill validator: structure, SKILL.md, links
justfile                   <- command surface (thin wrappers over pre-commit)
```

Catalog depth is exactly two: `skills/<catalog>/<skill>/`. Installation
flattens this to `<skill-root>/<skill>/`, and the target-side disposal
procedure may only ever assume `<root>/<name>/SKILL.md` — never nest
catalogs.

## Catalogs

- `core` — required for every harness build; useful regardless of the
  target's stack.
- `frontend` — design description and visual language; only for targets
  with a user-facing visual surface, installed on top of `core`.
- `python` — trusted defaults and authoritative doc URLs for Python
  targets: docstring and comment conventions, testing setup, and
  toolchain choices; installed on top of `core`, only for Python
  projects.

The validator reconciles this list against the directories under `skills/`
(check B3), and it defines the legal commit scopes: `feat(core): …` for a
catalog change, no scope otherwise. Each catalog is also exposed as one
plugin in `.claude-plugin/marketplace.json` (plugin name = catalog name,
`skills` listing every skill directory explicitly — the skills-CLI
installer needs the explicit list to group its listing by catalog, so
adding or removing a skill edits the manifest in the same change).
Adding, renaming, or removing a catalog is the `sync-catalog` skill's
procedure, which owns the marketplace manifest too.

## Quality Gates

| Gate | Runs | Covers |
|---|---|---|
| pre-commit registry | `just check`, every commit, CI `checks` job | hygiene, ruff, gitleaks on the working tree, both validators |
| `scripts/validate_repo.py` | inside the registry; `just validate-repo` alone | B1–B3 catalogs, C1–C3 docs/links/translations, D1–D3 marker contract |
| `scripts/check_skill.py` | inside the registry; `just check-skill <path>`, `just check-skills` | one skill: S1–S3 structure (warnings), M1–M6 SKILL.md content, L1 links; errors block, warnings advise |
| validator self-tests | first, on every run of either validator | that all checks fire — the catalogs may be empty, so with zero subjects a green run would otherwise prove nothing |
| CI `secrets` job | pull requests and pushes to main | full-history gitleaks with the same repository ruleset |

Check logic lives once, in `.pre-commit-config.yaml`; `just check` and CI
run the identical registry, so local and CI gates cannot drift.

## Deferred Mechanisms

Each row is a decision with a trigger, not an oversight. Build it when its
trigger fires — not before.

| Mechanism | Trigger |
|---|---|
| `just new-skill` scaffolder | the authoring template still yields frontmatter mistakes by the third published skill |
| Commit-message linting | non-conforming messages recur in PRs; `.gitmessage` plus the AGENTS.md rule is the cheaper gate first |
| Markdown or translation-parity linting | reviews keep catching drift that the existence check (C1) misses |
| Marketplace ↔ catalog validator check | built as a sync-catalog step first; add the check (with its self-test fixture) if manifest drift recurs in review |
| Unit tests for the validator | its logic outgrows the fixture self-test |
| L3+ autonomy (self-maintenance, persistent memory) | explicit user request only |

## Gotchas

- The marker literal is duplicated on purpose: the `MARKER` constants in
  `scripts/validate_repo.py` and `scripts/check_skill.py`, every fence
  tagged `text meta-skill-marker`, the YAML authoring form in the contract,
  and every published description. Check D1 blocks fence and near-miss
  drift; the `sync-contract` skill owns changes.
- Published skills are deliberately never symlinked into this repository's
  own skill directories: a meta-skill active *here* would announce itself as
  disposable inside the one repository that must keep it. Do not "fix" the
  missing wiring.
- `.agents/skills/` and `.claude/skills/` are hard-coded scan roots of the
  skills-CLI installer, with no path-exclusion mechanism. Every internal
  skill therefore carries `metadata.internal: true` (check M6 enforces both
  directions), and install instructions always use `skills/…` subpath
  sources, never the bare repository.
- This harness is a public reference implementation of the thing it sells,
  which creates pressure to over-build it as a showcase. It is thin on
  purpose: one validator, a thin justfile, a one-file marketplace manifest.
  The restraint is the exemplar.
