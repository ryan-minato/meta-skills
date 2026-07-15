---
name: meta-agents-md
description: >
  [META-SKILL: remove after harness setup]
  Writes a project's agent entrypoint — what belongs on the always-loaded page
  versus behind a pointer, the when-to-read table that makes everything else
  discoverable, and the rule that keeps it from rotting. Use when creating or
  restructuring AGENTS.md, CLAUDE.md, or whatever file agents read first in a
  project. Not for deciding which file a given framework reads or where it goes,
  not for the shape of the knowledge files it points at, and not for ordinary
  product documentation aimed at humans.
---

# The Agent Entrypoint

The entrypoint is the one file agents always see. Everything else in the harness
is reachable only because this page points at it — so what is not here, and not
pointed at from here, does not exist.

**Write it for the agent that arrives knowing nothing.** Once the scaffolding is
gone, this tree is all that remains: there will be no meta-skill to re-derive a
convention that never got written down.

## What belongs here

The test is not "is this true?" — it is **"would an agent get this wrong?"**

Belongs:

- **What the project is**, in a sentence or two.
- **Conventions the code does not already show.** The ones that live in
  someone's head, or that look arbitrary until explained.
- **Boundaries** — what needs asking first, especially anything irreversible or
  outward-facing.
- **The check that proves a change is sound**, and when to run it.
- **Pointers** to everything else.
- **Who keeps this current.**

Does not belong:

- **Anything the code already demonstrates.** If the last forty commits are
  visibly Conventional Commits, saying so spends budget to tell an agent what it
  can see. Spend it on what it cannot.
- **General programming advice.** "Write tests", "handle errors", "keep
  functions small" — the model already knows. Every such line dilutes the lines
  that are actually about *this* project.
- **Aspirations.** A convention nobody follows is a lie that agents will follow,
  and it will produce work that looks wrong to the team.
- **Speculative sections.** An empty "Deployment" heading teaches an agent that
  this file is scenery.

**Start with what agents actually get wrong here.** If someone has typed the
same correction into a chat twice, that is the highest-value line in the file,
and it beats any principle.

## What stays, and what moves behind a pointer

Everything on this page loads in **every session, forever**. That is the budget.

- **Always-loaded** — needed on most tasks, or costly to get wrong: the
  purpose, the load-bearing conventions, the boundaries, the check command.
- **Behind a pointer** — needed sometimes: a procedure for one subsystem, the
  full workflow, domain reference material.

Aim for **around 100 lines**, up to roughly 200 for a genuinely complex project.
Past that, agents skim, and the rule that mattered gets skimmed with the rest.

The split rule: **would an agent need this on a typical task?** Yes → here. Only
when doing a particular kind of work → behind a pointer with that condition
written on it.

Moving something behind a pointer is not filing it away. **A pointer is a
promise that it will be found**, and that promise is only kept if the condition
is recognisable.

## The when-to-read table

Knowledge files are the one part of a harness with **no self-announcement**. A
skill has a description the agent always sees. A knowledge file has nothing —
if the pointer table does not list it, it is invisible, however good it is.

So the table is the discovery mechanism, and **the wording of each condition
decides whether the file is ever opened**:

| Instead of | Write |
|---|---|
| `Testing` | `Adding or changing a test` |
| `Payments` | `Touching the payment flow` |
| `Architecture` | `Adding a new service, or wondering why a thing is missing` |
| `Style guide` | `Writing user-facing copy` |

A topic label asks the agent to guess whether it is relevant. **A condition is
something an agent can notice it is in.** Write the situation, not the subject.

## The standalone check

Before you are done, verify — because these meta-skills are about to be deleted:

- **Every rule that matters is reachable from this page**, with no meta-skill
  present. Anything learned during the build that only exists in the
  conversation is about to be lost.
- **No file names a meta-skill.** Not this page, not a knowledge file, not a CI
  config. A durable file pointing at scaffolding becomes a dangling pointer the
  moment cleanup runs — and cleanup will stop rather than break it, which means
  the reference blocks the very step it is standing in front of.
- **No file this build generated carries the removal marker.** A generated file
  that inherits it gets deleted at cleanup, silently, right after the build
  reports success.
- **Every pointer resolves**, and points at something that exists.

## Keeping it current

The entrypoint needs a line saying **who updates it and when**. One sentence is
the minimum; without it the file is accurate the day it is written and decays
from there.

**Stale is worse than absent.** An agent that finds no rule asks. An agent that
finds a wrong rule follows it, confidently, and produces work the team has to
unpick.

How to build a real maintenance mechanism — a sync rule, a pruning trigger — is
a separate question with its own trade-offs. This is only the note that the file
must not go unowned.

[Start from the skeleton](assets/AGENTS.md), and delete every section the
project does not need. An empty heading is worse than a missing one.

## Gotchas

- **Behind a pointer is not "always seen".** Do not move something load-bearing
  out of the entrypoint to hit a line count. If an agent must know it on a
  typical task, it stays, even if the page gets long.
- **Do not restate an accurate document that already exists.** Point at the
  CONTRIBUTING.md; do not copy it. Two copies of a rule drift, and then agents
  follow whichever they read first.
- **Length is a symptom, never the target.** A 60-line file of real constraints
  beats a 100-line file padded to look thorough. Cut what the model already
  knows first — that is almost always where the bloat is.
- **The file's own tone teaches.** Hedged, vague rules get treated as
  suggestions. Write them as decisions.
