# Contribution Workflow

Load this when starting, reporting on, or landing a tracked change.

## Source Of Truth

Git's default branch is the authority for repository content. Linear tracks
delivery only; it never becomes the source of truth for anything in the repo.

## Steps

1. **Create a Linear issue** in project *Meta Skills* (team `Aoi`). Split a
   complex change into sub-issues under one root issue.
2. **Branch from the root issue.** Use the root issue's `gitBranchName`, even when
   sub-issues exist. **Only the root issue gets a pull request** — sub-issues
   track work, not branches.
3. **Commit atomically** as each piece lands. Conventional Commits, English.
   Scope is the catalog changed (`feat(core): …`); omit it when the change belongs
   to no catalog (`docs: …`).
4. **Report progress on the sub-issue** it belongs to: a comment saying what
   landed, the commit, and anything that changed the plan. Then move that
   sub-issue to Done. The root issue stays In Progress until the pull request
   merges.
5. **Open a draft pull request** once the skeleton is in place, then keep working.
   Mark it ready for review only after every check passes. A human reviews after
   that.

## Labels

| Label | Use for |
|---|---|
| `Feature` | a new capability; typical for a root issue |
| `Docs` | documentation, harness docs, knowledge base |
| `Chore` | tooling, CI, validators, repo housekeeping |
| `Improvement` | better behavior in something that already works |
| `Bug` | wrong behavior |

## Before Every Commit

Run `just check`. Review the staged diff yourself for secrets and personal data —
**a secret committed is leaked even if a later commit removes it**, because git
history is permanent and force-pushing a public branch does not recall it. The
hooks are a backstop, not a substitute for reading the diff. Never `--no-verify`.

Commit as the repository's noreply identity. `.gitleaks.toml` rejects
non-anonymous email addresses, allowing only noreply and `example.com` forms.

## Fallbacks

**Linear is unreachable.** You are probably an external contributor rather than a
maintainer. Skip every Linear step and work directly on a descriptive branch. The
pull request is then the only tracking artifact, so its description carries the
context an issue would have held.

**A pull request cannot be created** (GitHub auth is missing or `gh` is not
logged in). Do not attempt a draft pull request. Finish the work, commit it, push
the branch, then hand the user:

- the intended pull request title,
- the full pull request body, and
- the creation link: `https://github.com/ryan-minato/meta-skills/compare/main...<branch>?expand=1`

so they can open it themselves. If the push also fails, say so plainly and leave
the commits local rather than guessing at another route.

## Human Handoff

Agents may create and update Linear issues, push branches, and open pull
requests. Humans own merging, releases, and deciding what enters a catalog.
Never merge your own pull request.
