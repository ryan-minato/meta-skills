# Organization Default Files

Read when the repository belongs to an organization.

GitHub lets an organization publish default community health files that
apply to every repository lacking its own copy. Before writing anything
repository-level:

1. Fetch the current inheritance mechanism — which files can be
   defaulted, from which repository, and the precedence rules — from
   <https://docs.github.com/en/communities> (organization behavior is
   detailed under <https://docs.github.com/en/organizations>).
2. Check whether the organization already publishes defaults, and read
   them.
3. Inherit by omission: create a repository-level file only where this
   project genuinely differs from the org default — a duplicate copy
   drifts and then contradicts it.
4. Record in the AGENTS.md deposit which files are inherited and from
   where, so future agents do not "fix" their absence.
