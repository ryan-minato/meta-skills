# Auditing An Existing Harness

Read when the project already has a harness in any form — an agent
instructions file, agent-facing docs, project skills, or checks built for
agent work. Audit before planning changes; never plan a rebuild on top of
an uninspected harness.

## Sequence

1. **Inventory.** List every agent-visible harness component: entrypoint
   files, knowledge or reference documents, project skills, CI checks,
   hooks, lint configs, templates. Note where each lives.
2. **Discovery check.** From the entrypoint, follow every pointer. Anything
   an agent cannot reach from the entrypoint is invisible in practice, no
   matter how good its content is.
3. **Compare against the project.** For each component, check its claims
   against the code and the team's current workflow: paths that exist,
   commands that run, rules that are still true.
4. **Classify** every finding:
   - stale — contradicts the current code or workflow
   - duplicated — the same rule stated in more than one place
   - invisible — unreachable from the entrypoint
   - excessive — thicker than the project's traits justify
   - orphaned — a mechanism whose trigger can no longer fire
5. **Disposition** per finding: update, reconnect, move, merge, split, or
   remove. Prefer the cheapest disposition that fixes the class.

## Folding Into The Plan

- Record the inventory and each finding's classification and disposition in
  the plan's audit section.
- Dispositions become plan work items alongside new builds, each assigned
  to the builder skill that owns the artifact.
- Keep what works: an audited component with no finding is recorded as
  kept, and its layer keeps its current thickness rating unless a trait
  says otherwise.
