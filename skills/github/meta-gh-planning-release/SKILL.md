---
name: meta-gh-planning-release
description: >-
  Disposable meta-skill (delete after the harness is built): establishes
  how work is planned and how finished work ships on a GitHub-hosted
  project — a label taxonomy, milestone and Projects usage sized to the
  team, then the versioning scheme, tag format, changelog policy, and
  release procedure, with platform capabilities and versioning specs
  always fetched live. Use when a harness build on a GitHub repository
  must define task tracking, milestones, labels, versioning, changelogs,
  or releases. Not for the CI quality gates or merge protections a
  release depends on — those are separate concerns of the harness.
---

# GitHub Planning and Releases

This skill produces the target project's recorded planning vocabulary
(labels with meanings, milestone usage, whether a board exists) and its
release contract (versioning scheme, tag format, changelog policy, a
step-by-step release procedure), deposited into AGENTS.md. It expects a
repository whose origin remote is GitHub and a user who can say how the
team actually tracks work.

## Workflow

1. Assess what exists: current labels, milestones, Projects, tags,
   releases, any changelog file, and the version recorded in the
   project's manifests. Existing working usage stays — record it.
2. Read [docs-navigation.md](references/docs-navigation.md) before the
   session's first fetch from docs.github.com, or when any recorded URL
   no longer resolves. Planning lives under
   <https://docs.github.com/en/issues>; releases under
   <https://docs.github.com/en/repositories>.
3. Planning: agree the tracking granularity with the user — a small
   label set where every label has a recorded meaning, what milestones
   group, and when an issue is required versus just doing the work. Read
   [projects.md](references/projects.md) when the team wants a board or
   iteration view rather than plain issues and milestones.
4. Apply labels and milestones with `gh` when authenticated; otherwise
   record them in the AGENTS.md deposit for manual creation.
5. Releases: agree the versioning scheme — fetch the chosen spec live
   (<https://semver.org/> or <https://calver.org/>) — plus the tag
   format and who bumps the version where.
6. Changelog policy, one source only: either a hand-maintained file —
   copy [changelog.md](assets/changelog.md) to `CHANGELOG.md` — or the
   platform's generated release notes, configured against the schema
   fetched this session. Never both.
7. Read [release-automation.md](references/release-automation.md) when
   releases should be cut by automation rather than by hand.
8. Copy
   [agents-md-planning-release.md](assets/agents-md-planning-release.md)
   into the target's AGENTS.md and rework it: label meanings, issue
   policy, versioning scheme, tag format, and the release procedure.
   This deposit is what future agents keep after this skill is deleted.

Done when: the label set exists (or is recorded for creation), the
versioning scheme and tag format appear consistently in the manifests
and AGENTS.md, and a release of the current state could be cut by
following AGENTS.md alone.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- Size planning to the team: a solo repository gets labels and
  milestones, not an iteration board nobody grooms.
- One changelog source: a hand-written CHANGELOG plus generated release
  notes drift into two half-truths.
- Tag, manifest version, and changelog entry move together — record who
  bumps what, and in which order.
