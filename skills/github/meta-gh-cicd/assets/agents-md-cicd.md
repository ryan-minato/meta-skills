# AGENTS.md Section: CI

Copy the block below into the target's AGENTS.md — as a new section, or
merged into the existing structure — then rework every line against the
workflow actually written and delete anything this project did not
decide.

```markdown
## CI

CI mirrors the local checks: every job in
`.github/workflows/checks.yml` runs a command you can run yourself.

| CI job | Local command |
|---|---|
| <job name> | `<command>` |

- A CI failure reproduces locally with the mapped command; fix it there,
  never by editing the workflow to pass.
- Required checks: <which jobs block merging>. Renaming a job breaks the
  merge gate — update the repository's protection settings in the same
  change.
- Scheduled or manual jobs: <what runs outside PRs, and who watches it>.
```
