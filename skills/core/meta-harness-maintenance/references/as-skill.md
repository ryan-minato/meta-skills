# Maintenance as Skills

Load this when the project uses skills, or has decided to. Otherwise the
knowledge-base mode is the right shape and this is overhead.

**Everything you create here is a durable project skill.** Two rules before
anything else:

- **No removal marker.** You are running inside marked scaffolding; if you copy
  its shape, the marker comes with it, and the skill you just wrote deletes
  itself at cleanup — silently, right after the build reports success.
- **Never name it `meta-*`.** Cleanup surfaces unmarked `meta-*` directories as
  "possible meta-skill, confirm?" forever.

## Sync: one skill per concern

Name them **`sync-<concern>`** — `sync-catalog`, `sync-schema`, `sync-docs`.

The prefix is the point: it groups them in the file tree and in the skill
listing. A suffix (`catalog-sync`) scatters them across the alphabet, interleaved
with unrelated skills, which is exactly what you do not want from a family of
skills that share a job.

**One concern per skill.** The temptation is one `sync-everything` that realigns
whatever drifted. Resist it: its trigger becomes "something changed somewhere",
which matches nothing, so it never fires.

### The shape

Four sections, in this order:

```markdown
## Source Of Truth
<Which artifact is authoritative. Everything else describes it and gets
corrected to match — never the reverse. Say this explicitly; without it,
someone will eventually "fix" the source to match a derivative.>

## Dependent Artifacts
<Every place the fact is repeated. A table, and it must be complete: nothing
enforces this list, and an artifact missing from it is one nobody will update.
This table is the inventory — do not restate a count of it in prose anywhere,
because a number drifts the moment a copy is added.>

## Workflow
<Numbered. Change the source first, then each dependent, then verify.>

## Gotchas
<What goes wrong. Whether the duplication is deliberate, so nobody refactors
away the thing that pays for it.>
```

### The description

The trigger is the source changing:

> `Use when <the source> changes — a <thing> is added, renamed, or removed — or
> when <the check> reports a mismatch. Not for <the adjacent thing it should not
> catch>.`

Name the **event**, not the topic. "Use when the API schema changes" fires. "Use
for schema management" does not.

## Entropy: find the event, or do not build it

**A skill only fires when its description matches something.** Sync has a crisp
trigger, so it fits a skill well.

**Entropy does not.** Its real trigger is time passing — rules going stale,
pointers dying, sections accumulating. **"Time passed" never matches a
description.** A skill that waits to be triggered by the calendar waits forever.

So an entropy skill must attach to a **real event someone actually does**:

- "before cutting a release"
- "reviewing the agent docs"
- "adding a rule to the entrypoint" — prune while you are already in the file
- a scheduled job or CI check that invokes it explicitly

**If you cannot name that event, do not build the skill.** Put the rule in the
entrypoint instead, where it is at least always visible. An entropy skill with
no event is a skill that never runs, and it costs a description forever to do
nothing.

### The shape, when there is an event

```markdown
## When This Runs
<The event. If this section is hard to write, stop — that is the signal.>

## Bounds
<What is allowed to grow, and what is not. "The entrypoint stays under ~100
lines." A bound nobody can check is a wish.>

## What To Cut
<Stale rules, dead pointers, speculative sections, duplication, anything the
model already knows.>

## The Bias
<Toward deletion. Say so outright. The default is to keep, everything looks
load-bearing from inside, and without an explicit bias nothing ever gets cut.>
```

## Before you finish

- Every skill you created: **no marker**, not named `meta-*`, `name` matches its
  directory.
- Each sync skill names its source of truth and lists **every** dependent.
- The entropy skill names a real event, or does not exist.
- Nothing points at the scaffolding.
