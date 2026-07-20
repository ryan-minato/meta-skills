---
name: meta-gl-cicd
description: >-
  Disposable meta-skill (delete after the harness is built): turns a
  GitLab project's local quality checks into a GitLab CI/CD pipeline
  (`.gitlab-ci.yml`) that gates merge requests — the pipeline mirrors the
  commands developers and agents already run locally, with keywords,
  predefined variables, and runner capabilities always fetched live from
  the GitLab docs and matched to the instance's version, never recalled
  from memory. Use when a harness build on a GitLab project (gitlab.com
  or self-managed) must add or restructure CI. Not for choosing which
  linters or tests the project runs (CI mirrors checks that already
  exist), and not for merge protections or release automation — those are
  separate concerns of the harness.
---

# GitLab CI as the Quality Gate

This skill produces a merge-request-gating pipeline that runs exactly
the project's existing local checks, plus an AGENTS.md section mapping
every CI job to the local command that reproduces it. It expects a
repository whose origin remote is a GitLab instance and whose local
checks (test, lint, format, type) already exist and pass.

## Workflow

1. Inventory the local gates: task-runner recipes, git hooks, and the
   test, lint, format, and type-check commands the project actually
   runs. CI mirrors these; a check with no local equivalent is a design
   smell to raise with the user, never to add silently.
2. Assess any existing `.gitlab-ci.yml` — a working pipeline stays. Note
   its job names: platform protections elsewhere in the harness key on
   them, so renames are breaking changes.
3. Read [docs-navigation.md](references/docs-navigation.md) before the
   session's first fetch from docs.gitlab.com, or when any recorded URL
   no longer resolves. Fetch current pipeline keywords, `rules:`
   semantics, and predefined variables from <https://docs.gitlab.com/ci/>
   before writing any YAML — and when the instance is self-managed,
   confirm against `<instance-url>/help`, because a keyword the
   instance's version lacks fails the whole pipeline.
4. Decide who runs the jobs: gitlab.com shared runners, or instance or
   project runners on self-managed — ask the user, and verify live what
   the target actually has; a pipeline with no eligible runner sits
   pending forever.
5. Agree the gate design with the user: which checks run on merge
   requests, on the default branch, and on a schedule; which are
   blocking; and a runtime budget for the blocking set.
6. Copy [gitlab-ci.md](assets/gitlab-ci.md) to `.gitlab-ci.yml` and
   rework every line: each job runs the project's real local command
   verbatim, `rules:` express the agreed triggers, and image choices
   match the project's toolchain.
7. Read [monorepo-paths.md](references/monorepo-paths.md) when the
   repository hosts more than one independently checked package or app.
   Read [slow-checks.md](references/slow-checks.md) when any blocking
   check would exceed the agreed runtime budget.
8. Copy [agents-md-cicd.md](assets/agents-md-cicd.md) into the target's
   AGENTS.md and rework it — it states the CI-to-local command mapping
   and how to reproduce any CI failure locally. This deposit is what
   future agents keep after this skill is deleted.

Done when: a merge-request pipeline runs exactly the project's local
check commands and passes on the current tree, and AGENTS.md maps every
CI job to the local command that reproduces it.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- Never deploy a canned pipeline: keywords, images, and component
  references are fetched live this session — docs.gitlab.com documents
  the newest GitLab, and a self-managed instance may not run it yet.
- CI that checks what local hooks don't (or the reverse) trains everyone
  to ignore one of them — one command set, two runners.
- Keep blocking checks inside the runtime budget; anything expensive or
  hardware-bound runs on a schedule or manually, never as an MR gate.
