---
name: meta-harness-maintenance
description: >
  [META-SKILL: remove after harness setup]
  Builds the mechanisms that keep a harness true after the scaffolding is gone:
  realigning facts that are duplicated across files when the source changes, and
  pruning rules that go stale, pointers that die, and sections that pile up. Use
  when a harness has facts repeated in several places, when deciding how agent
  docs stay current, or when asked how to stop them rotting. Not for writing the
  rules themselves, and not for a one-off tidy-up of files that already drifted.
---

# Keeping a Harness True

A harness is written once and wrong forever after, unless something keeps it
honest. This builds that something — and then the scaffolding leaves, so it has
to work without anyone here to run it.

**Stale is worse than absent.** An agent that finds no rule asks. An agent that
finds a wrong rule follows it, confidently, and produces work the team has to
unpick. Every decision below is downstream of that.

## Two concerns, and they fail differently

**Sync — coherence.** A fact lives in more than one place. The source changes;
the copies do not. Now the harness contradicts itself and agents follow whichever
they read first.

- Trigger: **crisp.** The source changed. You can name the moment.
- Needs: the source of truth named, every dependent listed, a procedure.

**Entropy — accretion and decay.** Rules go stale. Pointers die. Speculative
sections pile up. Nothing broke; the whole thing just quietly stopped being true.

- Trigger: **diffuse.** Time passing.
- Needs: bounds, an event to hang on, a pruning procedure, a bias toward
  deletion.

**The asymmetry between those triggers decides everything below.** Do not treat
the two as one job with one mechanism.

## Which mode: skills, or entrypoint rules?

**The gate is whether this project uses skills at all — not whether it is small,
and not whether it is empty today.**

1. **The project will not create or use skills** — none now, none planned →
   **entrypoint rules.** A lone maintenance skill in a project with no other
   skills is a permanent description for a mechanism nobody looks at, standing
   on its own with no convention to attach to.
2. **The project uses skills, or has decided to** → **skills.** Including a
   brand-new empty project that plans to. Start in the right shape; do not build
   it in prose and migrate later.
3. **Skills, but only one or two trivial drift points** → just write the rule in
   the entrypoint. This is a tiebreak *within* case 2, not the main gate — a
   simple structure is a reason to keep a mechanism small, never a reason to
   decide the project has no skills.

**Read the answer off the project**: a skill directory with non-scaffolding
skills in it means yes. If all you find is the scaffolding itself, or nothing at
all, **ask** — "does this project plan to use skills?" Do not infer from
emptiness.

### Why the gate is what it is

**A skill announces itself.** Its description sits in the listing, and it fires
when the trigger matches — **even if nobody read the entrypoint.** That is the
only real advantage skills have here, and it is a large one.

**An entrypoint rule does not announce itself.** It works when an agent reads
the entrypoint and remembers. For a couple of obligations that is enough and
costs nothing.

So the trade is: a skill buys self-announcement at the price of a permanent
description. Worth it where skills already exist and the convention has somewhere
to attach. Not worth it in a project that will never have another one.

Then read the mode you chose:

- [as-skill.md](references/as-skill.md) — both concerns, as durable project
  skills.
- [as-knowledge.md](references/as-knowledge.md) — both concerns, as rules in the
  entrypoint or a knowledge file.

## The trap on the entropy side

**A skill fires when its description matches. "Time passed" matches nothing.**

Sync is fine — the source changed, that is an event. But entropy's real trigger
is the calendar, and no calendar talks to a skill listing. An entropy skill
waiting to be triggered by time waits forever, while costing a description the
whole time.

So entropy must attach to **an event someone actually does**: before a release,
while reviewing the docs, while adding a rule to a file you are already in, or a
scheduled job that invokes it by name.

**If you cannot name that event, do not build the mechanism.** Put the rule
where it is at least always visible, and say plainly that it depends on someone
remembering. That is more honest than machinery that never runs.

This is also why the two concerns share one skill: the contrast is only visible
side by side, and it is the thing most likely to be got wrong.

## The rule that beats all of this

Whatever mode you choose, the strongest mechanism is one sentence:

> Update the doc in the same change as the thing it describes.

It has an event, needs no machinery, and turns maintenance from a task somebody
must remember into a property of how work already happens. Everything else in
this skill is for the drift that rule cannot catch.

## Before you finish

- Every mechanism names **an event**, not an aspiration. "Keep these in sync" is
  not a trigger.
- Every sync mechanism names its **source of truth** and lists **every**
  dependent. Nothing enforces that list; an artifact left off is one nobody
  updates.
- Where a check covers part of the work, say **which part** — and which part is
  still on a person.
- The entropy mechanism has a real event, or it does not exist.
- **Anything you generated is durable**: no removal marker, never named `meta-*`,
  and pointing at nothing in the scaffolding. A generated skill that inherits the
  marker deletes itself at cleanup, right after the build reports success.

## Gotchas

- **Do not build a mechanism for drift that has not happened.** Two files that
  restate one fact are a drift point. Two files that might one day restate one
  are not. The mechanism is itself something to maintain.
- **Duplication is sometimes correct.** An always-loaded copy of a rule earns
  its place precisely because pointer-loaded content only loads when its
  condition fires. Do not refactor away a duplicate that is paying for itself —
  write down *why* it is duplicated instead, next to it.
- **A count in prose drifts.** If a mechanism lists N places, keep the list in
  exactly one place and have everything else point at it. A number restated
  elsewhere is wrong the moment a copy is added, and it will be added.
- **Nothing enforces any of this.** A checker validates what it was taught to
  look for; a stale sentence in a doc passes every check ever written. Say so,
  so nobody mistakes a green run for a true harness.
