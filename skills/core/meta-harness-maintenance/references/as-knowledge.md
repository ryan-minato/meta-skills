# Maintenance as Entrypoint Rules

Load this when the project does not use skills and is not going to. The whole
mechanism is prose in files agents already read — no new machinery.

**Accept the trade honestly up front.** A rule written here **does not announce
itself**. It works only when an agent reads the entrypoint and remembers. That
is fine for a small number of obligations and hopeless for many, which is why
this mode is the right answer for a project with a couple of drift points and
the wrong one for a project with a dozen.

## Sync: a "Keeping X Current" section

It lives **next to what it governs**, not in a maintenance file of its own. A
rule about the README goes where README rules live; a rule about the schema goes
with the schema. A separate `maintenance.md` collects rules nobody reads,
because nothing takes them there.

Three parts, and it is short:

```markdown
## Keeping The Catalog Current

The directories under `packages/` are the truth. When one is added, renamed, or
removed, update: the table in README.md, the list in ARCHITECTURE.md, and the
`packages` key in release.yml. `npm run check` catches the last one; the first
two are on you.
```

- **The source of truth**, named. Everything else describes it and gets
  corrected to match — never the reverse.
- **The trigger**, as an event: "when a package is added, renamed, or removed".
  Not "keep these in sync", which is a wish rather than an instruction.
- **Every dependent**, listed. The list must be complete — nothing enforces it,
  and an artifact left off is one nobody will ever update.

**Say which parts a check catches and which it does not.** "The validator
catches the schema; the prose in README is on you" is worth more than the rest
of the section, because it tells the reader exactly where their attention is
load-bearing. A green check that never inspected a file is how a stale
reference survives forever.

### Where to put it

- **One or two drift points** → in the entrypoint. Always visible, costs a few
  lines.
- **More, or long** → its own knowledge file with a pointer whose condition is
  the trigger: *"Changing a package name"* → `knowledge/packages.md`. Never
  *"Maintenance"* — nobody is ever in a situation called "maintenance".

## Entropy: bounds, an event, and a bias

Same problem as in skill mode, and the same root cause: **entropy's trigger is
time passing, and nothing fires on time passing.** In prose the failure looks
different but is identical — a "keep this tidy" line that is true, agreeable,
and never acted on.

So attach it to something that already happens:

```markdown
## Keeping This Current

Update this file when the workflow it describes changes — the change and the doc
land together, or the doc is wrong by the next morning.

Before a release, re-read this file and delete what is no longer true. Aim to
keep it under ~100 lines: past that agents skim, and the rule that mattered gets
skimmed with the rest. When in doubt, cut. Everything looks load-bearing from
the inside, and a stale rule does more damage than a missing one — an agent that
finds no rule asks, while an agent that finds a wrong one proceeds.
```

Four things earn their place there:

- **The event** — "when the workflow changes", "before a release". Never "when
  it gets long", which is not something anyone notices.
- **A bound** — a line count, a scope. Checkable beats aspirational.
- **The bias toward deletion**, stated outright. Without it, nothing is ever
  cut.
- **Who owns it.** One name or one role. An unowned file is a file that rots.

**The single highest-value line is the "land together" rule**: the doc changes
in the same commit as the thing it describes. It converts maintenance from a
task somebody must remember into a property of how work already gets done — the
only version of this that actually holds.

## The minimum

If a project takes one line from all of this, it is this one, in the entrypoint:

```markdown
## Keeping This Current

Update this file in the same change as whatever it describes. <Name> owns it.
```

That is a real mechanism. It has an event, an owner, and no machinery.

## Before you finish

- Each rule names a source of truth, an event, and its dependents.
- No rule says "keep in sync" without saying **when** and **what**.
- The entrypoint has a keep-current line, even if nothing else was written.
- Where a check covers part of the work, the section says which part.
