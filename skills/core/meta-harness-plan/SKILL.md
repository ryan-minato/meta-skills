---
name: meta-harness-plan
description: >-
  Disposable meta-skill (delete after the harness is built): plans, audits,
  or improves this project's agent harness and produces a user-approved
  harness plan that records every decision and names the builder skills to
  run. Use when the user asks to set up, review, or improve the project's
  agent harness, agent instructions, or overall agent setup and no approved
  harness plan exists yet. Not for building the artifacts themselves — the
  plan names what to build; the matching builder skills build it.
---

# Harness Planning

This skill produces exactly one artifact: a harness plan the user has
approved, written into the project (default
`.agents/knowledge/harness-plan.md`). A harness is everything agent-visible
that helps agents meet the team's expectations: entrypoint instructions,
constraints, tools, automated checks, and reachable knowledge. Planning
never builds — the plan records each decision and lists the builder skills
that will do the building.

## Decision Axes

Decide each axis independently, per project traits. No axis is a maturity
ladder: whether the harness self-evolves and whether multiple agents run
are separate project choices, not higher levels of the same scale.

1. **Thickness per layer.** Rate every layer omitted / light / medium /
   thick. Capability layers (environment, information tools, workflow
   tools, capability tools) expand what agents can do; constraint layers
   (target, implementation, quality, workflow, repository safety) narrow
   the implementation space. One rating per layer, never one overall.
   - omitted — deliberately absent; record the trigger for building it later
   - light — a one-or-two-line rule or pointer
   - medium — a dedicated section, file, checklist, or skeleton
   - thick — machine-enforced (CI gate, hook, validation script)
2. **Evolution mode.** Self-evolving (agents update the harness from
   experience), fixed (the harness is an authoritative contract, changed
   only by humans or human-approved work), or compromise (after a task the
   agent may propose harness changes; the user decides; the default is not
   adopting). None is better — match the project. Human-in-the-loop
   projects default to compromise unless the project or user says
   otherwise.
3. **Agent topology.** Single agent is the default. Multi-agent is a
   separate choice with real preconditions and costs.
4. **Sync mechanism family.** Project-skill-based (auto-triggering; fits
   projects that use or will use skills) or entrypoint/knowledge-doc-based
   (fits projects whose harness is one instructions file). Record the
   choice; the sync builder skill installs it.
5. **Model class.** A project trait, not a choice: weak or local models
   need thinner, more mechanical documents and a section-lookup aid in the
   entrypoint.

Trait matching: high error cost → quality constraints thick. Short-lived or
one-off → light or omitted everywhere, no sync mechanism. Long-lived →
realtime sync regardless of evolution mode, periodic entropy reclamation
encouraged. Multi-person → workflow constraints medium or more, decisions
recorded. Unattended operation → thick automated checks (the precondition
for self-evolving). Human review present → compromise mode by default.
Mature CI and conventions already in place → plan the gaps only.

## Workflow

1. Inspect the project before asking anything: stack, layout, lifecycle,
   error cost, team size, attended or unattended operation, existing
   checks, and the model class agents will run on. Ask the user only what
   inspection cannot answer.
2. If the project already has a harness in any form, read
   [existing-harness.md](references/existing-harness.md) and audit it
   before planning changes.
3. Rate every layer on axis 1 and note a reason per rating.
4. Choose the evolution mode. If the project runs unattended or the user
   asks for self-evolution, read
   [self-evolving-or-unattended.md](references/self-evolving-or-unattended.md)
   first.
5. If the user asks for, or the plan is considering, more than one agent,
   read [multi-agent.md](references/multi-agent.md) before deciding
   topology.
6. If the plan will touch README, LICENSE, SECURITY, CONTRIBUTING, or an
   architecture document, read
   [public-files.md](references/public-files.md) — those files follow
   public conventions and are exempt from agent-doc style.
7. Draft the plan from
   [harness-plan-template.md](assets/harness-plan-template.md). Copy it,
   then rework every section against this project's reality: delete
   inapplicable rows, replace examples with real values, add what the
   template did not foresee, and remove all fill-in guidance.
8. Present the draft to the user, iterate, and only then write the approved
   plan to `.agents/knowledge/harness-plan.md` (or the knowledge location
   the user names). It becomes the project's first knowledge document.

Done when: an approved plan file exists in the project recording a value
and a reason for every axis plus the ordered builder-skill list, and
nothing else was created or changed.

## Gotchas

- Planning creates or edits nothing except the plan file. Building is the
  builder skills' job — tell the user which ones to install and run.
- Never default to a self-evolving harness; it is a choice with
  preconditions, not an upgrade.
- Deploying the template verbatim is a failure: an unedited section means
  the decision was not actually made.
- Decisions the user has already made go into the plan as recorded facts;
  do not reopen them in later sessions.
- A project with mature checks and conventions gets a gap plan, never a
  rebuild.
