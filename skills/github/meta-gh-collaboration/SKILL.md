---
name: meta-gh-collaboration
description: >-
  Disposable meta-skill (delete after the harness is built): establishes
  how changes and reports flow through a GitHub-hosted project — commit
  message format, branch and pull request flow, review expectations, and
  issue intake — writing the pull request and issue templates under
  `.github/` and depositing the agreed conventions into AGENTS.md. Use
  when a harness build on a GitHub repository must define commit, branch,
  PR, review, or issue conventions. Not for CI pipelines, merge
  protections, or public-facing community documents — those are separate
  concerns of the harness.
---

# GitHub Collaboration Conventions

This skill produces the target project's recorded collaboration
contract — how commits are written, how branches and pull requests move,
what review requires, and how issues arrive — as `.github/` templates
plus an AGENTS.md section future agents follow. It expects a repository
whose origin remote is GitHub and a user who can speak for the team's
working style.

## Workflow

1. Assess what already exists: `git log --oneline -30` for the de-facto
   commit style, current branch naming, `.github/PULL_REQUEST_TEMPLATE*`,
   and `.github/ISSUE_TEMPLATE/`. Ask the user for team size and
   repository visibility. Existing working conventions stay — record
   them rather than replace them.
2. Read [docs-navigation.md](references/docs-navigation.md) before the
   session's first fetch from docs.github.com, or when any recorded URL
   no longer resolves.
3. Agree the commit message format with the user. When a named spec is
   chosen (Conventional Commits — <https://www.conventionalcommits.org/>
   — is the common one), fetch its current text from its own site —
   never restate a spec from memory — and decide the project-specific
   parts: allowed types, scope meanings, subject length.
4. Agree branch and pull request flow: branching model, draft-PR usage,
   PR size expectations, and merge method. When a platform feature
   (auto-merge, merge queue) is under consideration, fetch its current
   state from <https://docs.github.com/en/pull-requests> first.
5. Agree review conventions: who reviews what, what blocks approval,
   expected response time, and how agent-authored PRs are marked.
6. Copy [pr-template.md](assets/pr-template.md) to
   `.github/PULL_REQUEST_TEMPLATE.md` and rework every line against the
   agreed flow.
7. Read [issue-templates.md](references/issue-templates.md) when the
   project will take structured issue reports — bug reports or feature
   requests from more people than the maintainer. It guides copying
   [issue-form-bug.yml](assets/issue-form-bug.yml) and
   [issue-form-feature.yml](assets/issue-form-feature.yml) into
   `.github/ISSUE_TEMPLATE/`.
8. Copy [agents-md-collaboration.md](assets/agents-md-collaboration.md)
   into the target's AGENTS.md — as a new section, or merged into the
   existing structure — and rework every line. This deposit is what
   future agents keep after this skill is deleted.

Done when: AGENTS.md states the commit format, branch flow, and review
rules a future agent can follow on its own; every template under
`.github/` matches syntax fetched live this session; and a sample commit
message in the recorded format passes whatever local checks the project
runs.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- Derive the commit format from `git log` before proposing one;
  migration away from a working style happens only when the user asks.
- Issue forms are YAML against an evolving schema — validate against
  syntax fetched this session, and prefer a plain Markdown template when
  forms add nothing.
- Templates written for an audience that does not exist are noise: a
  private solo repository may need only the AGENTS.md section.
