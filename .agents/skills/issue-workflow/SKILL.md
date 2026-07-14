---
name: issue-workflow
description: Manages Linear-backed repository changes from issue creation through draft pull request handoff.
metadata:
  internal: "true"
---

# Linear Issue Workflow

Use this workflow for a repository change that needs Linear tracking, commits,
push, and draft PR handoff.

1. Resolve the target Linear team and project; do not guess assignees, dates,
   priorities, cycles, or leads. Create or update the issue before code changes.
2. For a parent delivery, create the parent and child issues first. Use the
   parent's Linear `gitBranchName` to branch from the current origin default
   branch. Preserve unrelated dirty work; never reset or stash it implicitly.
3. Move the active child to In Progress, implement its focused scope, and run
   `just check`. Keep commits atomic and use a scoped Conventional Commit.
4. Before committing, run `just commit-gate`; never bypass hooks with
   `--no-verify`. Post an English milestone comment after a successful commit,
   then move that child to Done.
5. Push the parent branch and attempt a draft PR. Keep the parent In Progress;
   only the normal merge integration closes it. Do not mark it In Review until
   a user confirms the PR URL.
6. If push succeeds but PR creation fails, add an English blocker comment,
   retain In Progress, and provide the exact title and template-rendered body
   for a human to create the draft PR. If push fails, stop external delivery and
   provide the precise push and PR commands without claiming success.

For the active repository, the project is Meta Skills in the Aoi team. Resolve
it dynamically because names and IDs may change. Use `knowledge-sync` only
after merge; Git's default branch remains the knowledge authority.
