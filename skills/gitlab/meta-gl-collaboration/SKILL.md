---
name: meta-gl-collaboration
description: >-
  Disposable meta-skill (delete after the harness is built): establishes
  how changes and reports flow through a GitLab-hosted project — commit
  message format, branch and merge request flow, review expectations, and
  issue intake — writing the merge request and issue description
  templates under `.gitlab/` and depositing the agreed conventions into
  AGENTS.md. Use when a harness build on a GitLab project (gitlab.com or
  self-managed) must define commit, branch, MR, review, or issue
  conventions. Not for CI pipelines, merge protections, or public-facing
  community documents — those are separate concerns of the harness.
---

# GitLab Collaboration Conventions

This skill produces the target project's recorded collaboration
contract — how commits are written, how branches and merge requests
move, what review requires, and how issues arrive — as `.gitlab/`
description templates plus an AGENTS.md section future agents follow. It
expects a repository whose origin remote is a GitLab instance and a user
who can speak for the team's working style.

## Workflow

1. Assess what already exists: `git log --oneline -30` for the de-facto
   commit style, current branch naming, and any templates under
   `.gitlab/merge_request_templates/` and `.gitlab/issue_templates/`.
   Ask the user for team size, project visibility, and — when
   self-managed — the instance URL and version. Existing working
   conventions stay — record them rather than replace them.
2. Read [docs-navigation.md](references/docs-navigation.md) before the
   session's first fetch from docs.gitlab.com, or when any recorded URL
   no longer resolves.
3. Agree the commit message format with the user. When a named spec is
   chosen (Conventional Commits — <https://www.conventionalcommits.org/>
   — is the common one), fetch its current text from its own site —
   never restate a spec from memory — and decide the project-specific
   parts: allowed types, scope meanings, subject length.
4. Agree branch and merge request flow: branching model, draft-MR usage,
   MR size expectations, and merge method (merge commit, squash,
   fast-forward). When a platform feature (merge trains, auto-merge) is
   under consideration, locate its current state through the llms.txt
   index first — several are tier-gated.
5. Agree review conventions: who reviews what, what blocks approval,
   expected response time, and how agent-authored MRs are marked.
6. Read [description-templates.md](references/description-templates.md)
   when writing any template — GitLab's template mechanics differ from
   other forges. Copy [mr-template.md](assets/mr-template.md) to
   `.gitlab/merge_request_templates/Default.md` and rework every line
   against the agreed flow; when the project takes structured issue
   reports from more people than the maintainer, copy
   [issue-template-bug.md](assets/issue-template-bug.md) and
   [issue-template-feature.md](assets/issue-template-feature.md) into
   `.gitlab/issue_templates/`.
7. Copy [agents-md-collaboration.md](assets/agents-md-collaboration.md)
   into the target's AGENTS.md — as a new section, or merged into the
   existing structure — and rework every line. This deposit is what
   future agents keep after this skill is deleted.

Done when: AGENTS.md states the commit format, branch flow, and review
rules a future agent can follow on its own; every template under
`.gitlab/` matches mechanics fetched live this session; and a sample
commit message in the recorded format passes whatever local checks the
project runs.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- Derive the commit format from `git log` before proposing one;
  migration away from a working style happens only when the user asks.
- GitLab description templates are Markdown, not forms — do not port
  YAML issue-form syntax from other forges; structure comes from
  headings and quick actions, whose current syntax is fetched live.
- Templates written for an audience that does not exist are noise: a
  private solo project may need only the AGENTS.md section.
