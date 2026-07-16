---
name: tracked-change-workflow
description: >-
  Runs a tracked change end to end: Linear root issue, branch, atomic
  commits, draft PR, ready for review. Use when starting non-trivial work in
  this repository, opening a pull request, or reporting progress. Includes
  the fallbacks when Linear or GitHub is unavailable.
metadata:
  internal: true
---

# Tracked-Change Workflow

Git on the default branch is the source of truth for content; Linear tracks
delivery only.

## Workflow

1. **Root issue.** Create one Linear issue in project **Meta Skills** (team
   `Aoi`, key `AOI`) describing the outcome, and set a label: Feature, Bug,
   Improvement, Docs, or Chore. Split complex work into sub-issues under it.
   Only the root issue ever gets a branch or a pull request.
2. **Branch** from the default branch using the root issue's
   `gitBranchName`.
3. **Work in atomic commits**, observing the commit gates in AGENTS.md.
   Report progress as you go: move sub-issues through their states, and
   comment on the root issue when direction changes or a chunk lands.
4. **Draft PR** as soon as the skeleton exists — for the root issue only.
   Write the body in the format of
   [PULL_REQUEST_TEMPLATE.md](../../../.github/PULL_REQUEST_TEMPLATE.md) —
   GitHub only pre-fills it in the web UI, so fill it in yourself when
   creating the PR any other way — and link the root issue in its Linear
   section.
5. **Ready for review** only when every check passes locally and in CI. A
   human reviews and merges; never merge your own PR, and never mark a
   failing PR ready.

## Fallbacks

- **Linear unreachable** → the user is likely an external contributor, not
  an internal developer. Skip every Linear step; the Git and PR flow above
  still applies.
- **PR creation impossible** (GitHub auth) → finish the work, push the
  branch, then hand the user the intended PR title, the full PR body text
  (also in the template's format), and the compare URL
  `https://github.com/ryan-minato/meta-skills/compare/main...<branch>?expand=1`
  so they can create the PR themselves.

## Gotchas

- Update this skill in the same change whenever the team changes a workflow
  decision (labels, review flow, branch naming, issue structure).
