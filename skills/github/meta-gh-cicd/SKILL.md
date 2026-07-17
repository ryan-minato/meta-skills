---
name: meta-gh-cicd
description: >-
  Disposable meta-skill (delete after the harness is built): turns a
  GitHub-hosted project's local quality checks into GitHub Actions
  workflows that gate pull requests — CI mirrors the commands developers
  and agents already run locally, with workflow syntax, action versions,
  and runner capabilities always fetched live from the Actions docs,
  never recalled from memory. Use when a harness build on a GitHub
  repository must add or restructure CI. Not for choosing which linters
  or tests the project runs (CI mirrors checks that already exist), and
  not for merge protections or release automation — those are separate
  concerns of the harness.
---

# GitHub Actions as the Quality Gate

This skill produces a pull-request-gating workflow that runs exactly the
project's existing local checks, plus an AGENTS.md section mapping every
CI job to the local command that reproduces it. It expects a repository
whose origin remote is GitHub and whose local checks (test, lint,
format, type) already exist and pass.

## Workflow

1. Inventory the local gates: task-runner recipes, git hooks, and the
   test, lint, format, and type-check commands the project actually
   runs. CI mirrors these; a check with no local equivalent is a design
   smell to raise with the user, never to add silently.
2. Assess `.github/workflows/` — existing working workflows stay. Note
   their job and check names: platform protections elsewhere in the
   harness key on those names, so renames are breaking changes.
3. Read [docs-navigation.md](references/docs-navigation.md) before the
   session's first fetch from docs.github.com, or when any recorded URL
   no longer resolves. Fetch current workflow syntax, trigger semantics,
   and the default token permissions from
   <https://docs.github.com/en/actions> before writing any YAML.
4. Agree the gate design with the user: which checks run on pull
   requests, on pushes to the default branch, and on a schedule; which
   are required versus advisory; and a runtime budget for the required
   set.
5. Copy [workflow-checks.md](assets/workflow-checks.md) to
   `.github/workflows/checks.yml` and rework every line: each job runs
   the project's real local command verbatim, the permissions block is
   minimal and explicit, and third-party actions are referenced the way
   the fetched docs currently recommend.
6. Read [monorepo-paths.md](references/monorepo-paths.md) when the
   repository hosts more than one independently checked package or app.
   Read [slow-checks.md](references/slow-checks.md) when any required
   check would exceed the agreed runtime budget.
7. Copy [agents-md-cicd.md](assets/agents-md-cicd.md) into the target's
   AGENTS.md and rework it — it states the CI-to-local command mapping
   and how to reproduce any CI failure locally. This deposit is what
   future agents keep after this skill is deleted.

Done when: a pull-request-triggered workflow runs exactly the project's
local check commands and passes on the current tree, and AGENTS.md maps
every CI job to the local command that reproduces it.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- Never deploy a canned workflow: action references, runner labels, and
  syntax are fetched live this session — a remembered action version may
  already be stale or unmaintained.
- CI that checks what local hooks don't (or the reverse) trains everyone
  to ignore one of them — one command set, two runners.
- Keep required checks inside the runtime budget; anything expensive or
  hardware-bound runs on a schedule or on demand, never as a PR gate.
