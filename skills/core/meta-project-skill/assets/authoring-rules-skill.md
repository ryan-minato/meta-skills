---
name: skill-authoring
description: >-
  Applies this project's conventions when creating, improving, or
  retiring a project skill. Use when adding a skill under <skill root>,
  when an existing skill misfires or goes stale, or when deciding
  whether a procedure deserves a skill at all.
---

# Skill Authoring

Rules for skills in this project, at `<skill root>`.

## Whether

A skill needs a recurring, non-obvious procedure that is fragile,
order-sensitive, or branchy. A one-line rule goes in the entrypoint;
stable facts go in the knowledge base; one-off context goes nowhere.

## How

1. One concern per skill. Directory name equals the `name` field,
   kebab-case.
2. Description = the user requests that should trigger it + the project
   condition, with a "Not for" exclusion. Never internal file names.
3. Body: short; most-used path inline, rare branches in the skill's own
   references behind load conditions. Scripts run non-interactively.
4. End the body with its update trigger: what change obliges revising
   this skill.
5. <project-specific convention, e.g. review or validation step for new
   skills>

Done when: the skill loads on its trigger, every line is current, and
its update trigger is stated.
