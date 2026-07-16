---
name: meta-project-skill
description: >-
  Disposable meta-skill (delete after the harness is built): creates,
  improves, or edits durable project-level skills — tests whether a
  procedure deserves a skill, writes a trigger-tight description and short
  body with conditional references, and deposits the project's
  skill-authoring rules so future agents can design skills without it.
  Use when the harness plan calls for project skills, or when a recurring
  procedure is fragile, order-sensitive, or keeps being re-explained. Not
  for one-off tasks, stable background knowledge, or these disposable
  meta-skills themselves.
---

# Project Skills

This skill produces durable skills inside the target project: progressively
loaded manuals for one recurring procedure each. A skill beats a document
when the procedure is repeated, fragile, order-sensitive, or branchy;
otherwise a knowledge file or one entrypoint line is cheaper. It expects a
harness plan (default `.agents/knowledge/harness-plan.md`); without one,
ask the user only which procedures keep going wrong or keep being
re-explained.

## Workflow

1. Test the warrant. If the call is not obvious, read
   [when-warranted.md](references/when-warranted.md) before creating
   anything.
2. When improving an existing skill that misfires, went stale, or triggers
   too broadly, read [retrofit.md](references/retrofit.md) and diagnose in
   its order instead of rewriting blind.
3. Scope one concern per skill; unrelated triggers become separate skills.
4. Create from the skeleton matching the procedure's shape — copy it, then
   rework every line against the real procedure: real commands, real
   paths, the project's actual failure modes; delete the guidance notes.
   - ordered, fragile operations (build, release, migrate) →
     [skeleton-procedure.md](assets/skeleton-procedure.md)
   - symptom-to-cause branching (debugging, triage) →
     [skeleton-diagnosis.md](assets/skeleton-diagnosis.md)
   - checks with pass criteria (audits, gate reviews) →
     [skeleton-validation.md](assets/skeleton-validation.md)
   - anything else → [skeleton-generic.md](assets/skeleton-generic.md)
5. Write the description as trigger + intent: what the user asks for plus
   the project condition, never internal file names. Scripts the skill
   bundles must run non-interactively.
6. Give the skill an update trigger: a project-visible rule naming when it
   must be revised (its commands, paths, or procedure changed). A skill
   nobody updates goes stale silently and is then followed with
   confidence.
7. Deposit the project's skill-authoring rules, in the form matching the
   plan's sync-family decision: a durable authoring skill from
   [authoring-rules-skill.md](assets/authoring-rules-skill.md) when the
   project uses skills as its mechanism family, otherwise an entrypoint
   section from
   [authoring-rules-section.md](assets/authoring-rules-section.md). This
   step is what lets future agents build good skills after the
   meta-skills are gone.

Done when: each new skill loads on its trigger and holds only current
rules, an update trigger exists in project-visible form, the authoring
rules are deposited, and the user approved the set.

## Gotchas

- A broad trigger pollutes every session; a description that lists
  concrete user requests beats an abstract summary.
- The skills built here are durable: their descriptions must never begin
  with the marker these disposable meta-skills carry, or harness cleanup
  will delete them.
- One mechanism per concern — never create a skill that duplicates an
  entrypoint rule; move the rule or drop the skill.
- Most frameworks announce installed skills through their descriptions;
  if the target's does not, add an entrypoint pointer to the skill
  directory or the skill is invisible.
- Deploying a skeleton without reworking it produces a skill that
  describes no real procedure — delete-on-sight material.
