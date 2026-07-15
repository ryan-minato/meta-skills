---
name: meta-knowledge-file
description: >
  [META-SKILL: remove after harness setup]
  Creates the knowledge files an entrypoint points at — goal, plan, quality,
  workflow, and reference material — deciding for each whether it is one file or
  a folder, and shaping it so the pointer that loads it stays honest. Use when
  building out a project's agent knowledge base during harness setup, or when
  deciding whether some material deserves its own file. Not for the entrypoint
  itself, not for framework-specific file locations, and not for documentation
  written for human readers.
---

# Knowledge Files

A knowledge file is material an agent loads **only when a condition fires**.
That is its whole nature, and every rule here follows from it.

The entrypoint decides *what gets promoted onto the always-loaded page*. This
decides *what the pointed-at files look like* once something has been left off
it.

## The rule that governs everything

**One file per load condition.**

One condition covers the material → one file. The conditions are genuinely
separate → one file each.

Split on anything else — length, tidiness, a topic that feels like it deserves
its own page — and **the pointer table starts lying**. The table promises "read
this when X". If the file also contains Y, an agent that is doing Y never opens
it, and an agent doing X reads Y for nothing.

### The anti-pattern: splitting because a file got long

Length is not a condition. A long file with one condition is **a long file with
one condition**, and cutting it in half produces two pointers that both mean
"read this when X" — which is not a pointer table, it is a filing cabinet.

If it is genuinely long *and* genuinely unitary, use a folder with an index (see
below). Do not manufacture conditions that do not exist.

## The five kinds

| Kind | One file, or a folder? | The condition that loads it |
|---|---|---|
| **Goal** | **Always one file** | None — it is always relevant |
| **Plan** | Either | "starting new work", "what is next" |
| **Quality** | Either | "before proposing a change", "adding a test" |
| **Workflow** | Either | "starting or landing a change" |
| **Reference** | Either, **usually a folder** | Varies by topic — this is the point |

### Goal is not like the others

**A project has one purpose.** Split it and you get competing goals, and an
agent reading half of one — a failure worse than any amount of length.

It is also the only kind with **no load condition**: it is always relevant. That
is precisely why it usually should not be a file at all. At low harness
maturity, **the goal belongs in the entrypoint**, in the sentence or two at the
top. Promote it to its own file only when it genuinely needs room — a real
domain model, a bounded scope worth arguing.

### Reference is usually a folder

Reference material is the natural folder case, because it is the one kind whose
material has **genuinely independent topics**. Nobody reads "the reference" —
they read the bit about the thing they are touching, and the bit about the other
thing has no bearing on it. Those are separate conditions, so they are separate
files. That is the rule working, not an exception to it.

### The middle three

Plan, quality, and workflow start as one file each and become folders when the
conditions actually diverge:

- One release process → `workflow.md`. A release process, a hotfix process, and
  a review process that fire on different triggers → `workflow/` with a file
  each.
- One "run this before committing" rule → `quality.md`. Separate rules for
  tests, for performance work, and for security-sensitive changes → a folder.

**Wait for the divergence.** Do not build a folder for one file on the theory
that more will come. An empty-ish folder is a promise nobody kept.

## Folder shape: index, or point straight in?

| Shape | Use when | Cost |
|---|---|---|
| **Point straight in** — the entrypoint's table lists `dir/a.md`, `dir/b.md` | The conditions are distinguishable **from the entrypoint**. The default for a small number of files | The entrypoint's table grows |
| **Index file** — the entrypoint points at the folder's index, which dispatches | The conditions only separate **once you are already in the topic**, or the files need shared context first | One more hop before the material |

Small number of files → point straight in. One hop, no index, nothing to keep in
sync. Reach for an index when the entrypoint's table would need to carry
distinctions a reader cannot yet make.

## Writing one

- **Load condition at the top.** The file should open by confirming the reader
  is in the right place. An agent that opened it by mistake should learn that in
  one line.
- **One concern.** If you cannot state the condition in a phrase, the file is
  doing two jobs.
- **Written for an agent**, not a newcomer. Skip the orientation; state the
  constraint and the reason it exists.
- **The reason, always.** A rule without its reason survives until it is
  inconvenient, then gets dropped — usually at exactly the moment it mattered.
- **No file may name a meta-skill.** These files are the deliverable and must
  outlive the scaffolding; a reference to it becomes a dangling pointer that
  blocks cleanup.

## Do not write these

- **What is already written down.** Point at the existing CONTRIBUTING.md rather
  than restating it. Two copies of a rule drift, and then agents follow whichever
  they open first.
- **What the model already knows.** General language and tooling knowledge is
  not project knowledge.
- **What the code shows.** If the pattern is visible in the code, the file
  should explain *why it is that way*, not *that it is*.
- **A file with no pointer.** Unreachable, by construction. Either give it a
  condition and list it, or do not write it.

## Gotchas

- **A file is only as findable as its pointer's wording.** The best knowledge
  file in the project is invisible if its condition reads `Testing` instead of
  `Adding or changing a test`. Getting the file right and the pointer vague
  wastes the whole effort.
- **Every file is a maintenance obligation.** It will be wrong eventually. Write
  the ones that will still be worth fixing then.
- **A folder invites filling.** Once `reference/` exists, there is a pull to put
  things in it that no pointer will ever name. Every file earns its place by
  having a condition, not by being on-topic.
