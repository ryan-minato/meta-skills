---
name: meta-gl-planning-release
description: >-
  Disposable meta-skill (delete after the harness is built): establishes
  how work is planned and how finished work ships on a GitLab-hosted
  project — a label taxonomy (scoped labels where the tier allows),
  milestone, board, epic, and iteration usage sized to the team, then the
  versioning scheme, tag format, changelog policy, and release procedure
  (manual or pipeline-driven), with platform capabilities and versioning
  specs always fetched live. Use when a harness build on a GitLab project
  (gitlab.com or self-managed) must define task tracking, milestones,
  labels, versioning, changelogs, or releases. Not for the CI quality
  gates or merge protections a release depends on — those are separate
  concerns of the harness.
---

# GitLab Planning and Releases

This skill produces the target project's recorded planning vocabulary
(labels with meanings, milestone usage, whether a board or epics exist)
and its release contract (versioning scheme, tag format, changelog
policy, a step-by-step release procedure), deposited into AGENTS.md. It
expects a repository whose origin remote is a GitLab instance and a user
who can say how the team actually tracks work.

## Workflow

1. Assess what exists: current labels, milestones, boards, epics, tags,
   releases, any changelog file, and the version recorded in the
   project's manifests. Existing working usage stays — record it.
2. Read [docs-navigation.md](references/docs-navigation.md) before the
   session's first fetch from docs.gitlab.com, or when any recorded URL
   no longer resolves. Locate the planning topics (milestones, boards,
   epics, iterations) and the releases topic through the llms.txt
   index; read every tier badge — epics, iterations, and scoped labels
   are paid-tier features, so design the free-tier fallback (labels
   plus milestones) first.
3. Planning: agree the tracking granularity with the user — a small
   label set where every label has a recorded meaning, what milestones
   group, and when an issue is required versus just doing the work.
   Read [boards-epics.md](references/boards-epics.md) when the team
   wants a board, epics, or iterations rather than plain issues and
   milestones.
4. Apply labels and milestones with `glab` or the API when
   authenticated; otherwise record them in the AGENTS.md deposit for
   manual creation.
5. Releases: agree the versioning scheme — fetch the chosen spec live
   (<https://semver.org/> or <https://calver.org/>) — plus the tag
   format and who bumps the version where.
6. Changelog policy, one source only: a hand-maintained file — copy
   [changelog.md](assets/changelog.md) to `CHANGELOG.md` — or the
   platform's changelog generation from commit trailers, configured
   against mechanics fetched live this session. Never both.
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
- Epics, iterations, and scoped labels are tier-gated — verify on this
  instance before building the taxonomy around them, and design the
  free-tier fallback first.
- Size planning to the team: a solo project gets labels and milestones,
  not a board nobody grooms.
- One changelog source: a hand-written CHANGELOG plus generated entries
  drift into two half-truths.
- Tag, manifest version, and changelog entry move together — record who
  bumps what, and in which order.
