---
name: meta-harness-sync
description: >-
  Disposable meta-skill (delete after the harness is built): plans and
  installs the mechanisms that keep the harness true to the code —
  bidirectional sync triggers, exactly one mechanism per concern, a
  periodic entropy-reclamation routine for long-lived projects, and the
  propose-after-task rule for compromise-mode harnesses. Use when the
  harness plan calls for keep-current mechanisms, or when harness
  documents and the implementation keep drifting apart. Not for
  performing a one-off document fix.
---

# Harness Sync And Entropy

This skill installs the mechanisms that keep harness content true: stale
harness content is worse than none, because agents follow it with
confidence. Every mechanism built here is project-visible — future agents
can find when it runs, what it updates, and how it verifies. It expects a
harness plan (default `.agents/knowledge/harness-plan.md`); without one,
ask the user only for the evolution mode and whether the project uses
skills.

Every mechanism is bidirectional:

- **forward** — it names the change that triggers it and the document that
  change updates ("renaming a section updates its pointers, same change");
- **reverse** — when someone asks to update a document, it names the
  implementation artifacts to inspect first, so implementation-versus-doc
  drift surfaces on every doc touch, not only on a schedule.

## Workflow

1. Read the evolution mode and sync family from the harness plan. The mode
   sets obligations: self-evolving → thick automated checks plus realtime
   sync plus periodic reclamation are hard dependencies; compromise →
   additionally install the propose-after-task rule (step 4); fixed →
   long-lived projects still get realtime sync.
2. List the sync concerns: each pairing of a harness document with the
   implementation artifacts it describes (entrypoint ↔ commands and
   checks, architecture document ↔ structure, knowledge docs ↔ their
   subjects, skills ↔ their procedures). One concern, one mechanism —
   never two.
3. Install one bidirectional mechanism per concern, in the plan's family:
   - **skill family** (the project uses or will use skills): read
     [skill-mechanisms.md](references/skill-mechanisms.md), build each
     mechanism from [sync-skill.md](assets/sync-skill.md);
   - **entrypoint family** (the harness is the entrypoint alone): read
     [entrypoint-mechanisms.md](references/entrypoint-mechanisms.md),
     build from
     [sync-entrypoint-section.md](assets/sync-entrypoint-section.md).
   Copy the asset, then rework it: real documents, real artifacts, real
   triggers; delete the guidance.
4. If the evolution mode is compromise, install the propose-after-task
   rule from [proposal-rule.md](assets/proposal-rule.md) in the family's
   form: after a task the agent may propose harness changes, the user
   decides, and the default is not adopting.
5. If the project is long-lived, read
   [periodic-reclamation.md](references/periodic-reclamation.md) and
   install the routine in the family's form —
   [reclamation-skill.md](assets/reclamation-skill.md) or
   [reclamation-section.md](assets/reclamation-section.md).
6. Verify: every concern has exactly one owner; every forward trigger
   names a concrete change; every reverse trigger names concrete
   artifacts; everything is reachable from the entrypoint.

Done when: every sync concern has one project-visible bidirectional
mechanism, the evolution mode's obligations are installed, and long-lived
projects have a periodic reclamation routine.

## Gotchas

- Two mechanisms for one concern drift apart and then contradict each
  other; the second one is a bug, not redundancy.
- A generic "keep docs in sync" rule has no precise trigger, so it fires
  never or always — name the change and the document, per concern.
- Forward-only triggers let entropy accumulate invisibly: nothing
  re-checks a document that nobody happened to edit. The reverse
  direction is what reclaims it.
- A self-evolving harness without thick automated checks is drift by
  design; refuse to install that combination without the checks planned
  first.
