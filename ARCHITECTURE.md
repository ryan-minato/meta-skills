# Architecture

How this repository is laid out, what is deliberately absent, and why.

## Layout

```text
AGENTS.md                  <- entrypoint; every rule is reachable from here
CLAUDE.md                  <- points at AGENTS.md
ARCHITECTURE.md            <- this file
README.md / README.zh.md   <- public front door (English authoritative)
.agents/knowledge/         <- agent-facing knowledge, loaded on demand
.agents/skills/            <- this repo's own durable skills (never published)
.claude/skills             <- symlink to ../.agents/skills
skills/<catalog>/          <- published catalogs: CONTEXT.md + README.md + README.zh.md
skills/<catalog>/<skill>/  <- a published skill: SKILL.md [+ references/ scripts/ assets/]
scripts/                   <- validators
justfile                   <- the command surface
```

Catalog depth is exactly two: `skills/<catalog>/<skill>/`. Installation flattens
this to `<skill-root>/<skill>/`. Nesting catalogs is forbidden, because the
target-side disposal procedure may only ever assume `<root>/<name>/SKILL.md`.

## Catalogs

- `core` — required for every harness build; useful regardless of the target's stack.

This list is authoritative in two directions. `scripts/validate_repo.py` checks
it against the directories under `skills/`, and it is the source of legal commit
scopes: a commit touching a catalog uses that catalog as its scope
(`feat(core): …`); a commit touching no catalog omits the scope (`docs: …`).

Adding a catalog means adding it here **and** creating its `CONTEXT.md`,
`README.md`, and `README.zh.md`. The `sync-catalog` skill owns that procedure.

## Skill Visibility

`.claude/skills` symlinks to `../.agents/skills`, so Claude Code sees this
repository's own durable skills. Those skills carry no marker and are never
published.

**Published skills are deliberately not symlinked into `.agents/skills/`.** The
sibling repository `ryan-minato/skills` dogfoods its public skills that way; here
it would be actively wrong, not merely premature. A meta-skill installed into
this repository would announce `[META-SKILL: remove after harness setup]` inside
a repository whose harness is already built, trigger on work nobody does here,
and invite an agent to delete this repository's own product.

This is a conscious break from the sibling's convention. Do not "fix" the missing
symlinks.

## Quality Gates

| Gate | Runs | Covers |
|---|---|---|
| `scripts/validate_repo.py` | `just validate-repo` | project file structure: catalog scaffolds, the catalog list above, README mirrors, misplaced markers |
| `scripts/check_skill.py` | `just check-skill`, `just check-skills` | one skill: file structure, `SKILL.md` text structure, links |
| `check_skill.py --selftest` | `just selftest` | that the marker and link checks actually fire |
| `ruff` | `just lint` | `scripts/` |
| pre-commit hooks | every commit | whitespace, YAML, secrets (detect-secrets, gitleaks), the validators above |
| CI | pull requests | `just check` plus a full-history secret scan |

The two validators are split by concern so each can run independently. Checking a
skill's file structure and its `SKILL.md` text structure is one job, so one script
does both.

`--selftest` exists because the marker and link checks have **zero subjects**
until the first skill lands. Without it they are untested code that would pass
silently forever and then fail to catch the very first violation. It asserts the
conformance and link functions against inline strings, so the logic is exercised
on every run despite the empty catalog.

## Deferred Mechanisms

Each of these is a decision with a trigger, not an oversight. Build it when its
trigger fires — not before.

| Mechanism | Trigger | Why not now |
|---|---|---|
| `.claude-plugin/marketplace.json` | the first published skill | Every catalog is empty; the manifest would advertise nothing |
| Self-containment link checking across a whole catalog | the first skill | `check_skill.py` already enforces it per skill; a catalog-wide sweep has nothing to sweep |
| Per-skill spec linting beyond `check_skill.py` | the first skill, and only if an external skill-authoring linter does not already cover it | Zero subjects; likely duplicates an existing capability |
| Commit-message validation of the scope rule | scopes drift in practice | `.gitmessage` plus the rule in `AGENTS.md` is the cheaper gate first |
| `pyproject.toml` | a validator grows a dependency beyond PyYAML | Ruff's defaults already sit inside the `.editorconfig` width |
| Unit tests for the validators | their logic branches enough to need fixtures | `--selftest` plus a real run covers the flat scripts |
| Dogfooding public skills | **never** — see Skill Visibility | It would instruct agents to delete this repo's product |

## Gotchas

- The marker literal lives in three places on purpose: the always-loaded
  conventions in `AGENTS.md`, the contract at
  [meta-skill-contract.md](.agents/knowledge/meta-skill-contract.md), and the
  `MARKER` constant in `scripts/check_skill.py`. The `sync-contract` skill pays
  for that duplication.
- The authoring validator here and the disposal procedure that runs in a target
  project cannot share code — different machines, different trees. They agree
  only because both assume `<root>/<name>/SKILL.md`. Keep that invariant.
- This repository's harness is a public reference implementation of the thing it
  sells, which creates pressure to over-build it as a showcase. It is a thin L2
  on purpose: no thick layers, two flat scripts, no marketplace. The restraint is
  the exemplar.
