---
name: meta-project-skill
description: >
  [META-SKILL: remove after harness setup]
  Scaffolds the durable skills a project keeps — choosing which procedures earn
  one, writing the frontmatter and triggers that make them fire, and keeping
  them from inheriting the removal marker that would delete them at cleanup. Use
  when turning a repeated, fragile, or order-sensitive project procedure into a
  project skill during harness setup. Not for skills published to other
  projects, and not for one-off instructions that belong in the entrypoint.
---

# Project Skills

These are skills the project **keeps** — written by scaffolding the project is
about to **throw away**. Everything below follows from that asymmetry: the job
is not just to write a good skill, it is to write one that survives the cleanup
that deletes its author.

## Never inherit the marker

**This is the loudest rule here, and the one with the worst failure.**

You are running inside skills whose descriptions begin with a removal marker.
If you copy a skill's shape while working — and copying the shape is the natural
thing to do — that marker comes with it.

A project skill carrying the marker **deletes itself at cleanup**. Silently.
Moments after the build reports success. The user is told their harness is
ready, agrees to remove the scaffolding, and loses the skills the build just
wrote for them.

So: **the skills you write here carry no marker.** If you copied structure from
the scaffolding you are running, strip it. [The skeleton](assets/SKILL.md) is
already clean — start from it rather than from a meta-skill.

## Never name a project skill `meta-*`

Cleanup surfaces unmarked `meta-*` directories as *"possible meta-skill, marker
missing — confirm?"*. A durable project skill named `meta-anything` becomes a
permanent false positive: it shows up in the deletion prompt every single time,
and every time someone has to decide not to delete it.

Name it for what it does.

## Which procedures earn a skill

A skill costs a description in the listing for as long as the project lives.
That is the price. It is worth paying when a procedure is:

- **Repeated** — it happens often enough that getting it right once pays off.
- **Fragile** — there is a known way to get it wrong, and someone has.
- **Order-sensitive** — steps must happen in sequence, and the sequence is not
  obvious from the code.
- **Branchy** — the right move depends on conditions worth writing down.
- **Clearly triggerable** — you can name the moment it applies. If you cannot,
  nothing will ever fire it, however good the content is.

Not a skill:

- **A one-off.** Do the thing; do not write a skill about doing the thing.
- **Background knowledge.** That is a knowledge file, loaded by a pointer.
- **A rule that fits in a sentence.** That belongs in the entrypoint, where it
  is always visible, rather than behind a trigger that may not fire.
- **Something the model already knows.** A skill restating general practice adds
  a description to the listing and nothing else.

Take candidates from what the project actually does — and from what agents have
already got wrong here. A procedure someone has corrected twice is the strongest
candidate in the project.

## Writing one

**The frontmatter is the whole interface.** Two keys, both load-bearing:

- **`name`** — kebab-case, and it **must equal the directory name**. Not `meta-*`.
- **`description`** — the only thing an agent sees when deciding whether to load
  this. It is not a summary; it is a trigger.

A description that works has three parts:

1. **What it does**, opening with a distinctive verb. Never "This skill…",
   "Helps with…", "A tool for…" — those words are shared with every other skill
   and discriminate nothing.
2. **`Use when …`**, with **the words a person would actually say.** Not the
   topic. `Use when releasing, cutting a version, or publishing to npm` fires.
   `Use for release management` does not.
3. **`Not for …`** — the nearest thing it should *not* catch. Without a boundary
   a skill either fires on everything or gets ignored.

**The body is a procedure, not an essay.** State the steps. Give the reason
wherever the reason is not obvious, because a step whose purpose is unclear gets
skipped the first time it is inconvenient.

**Write the gotchas.** The mistakes people actually made. This is the section
that earns the skill's keep, and it is the section that gets left out.

**Keep it short.** Long material goes in `references/`, loaded only when its
condition fires. A skill body loads in full, every time it triggers.

## Layout

```text
<skill-root>/<name>/
├── SKILL.md          <- required; frontmatter + body
├── references/       <- optional; loaded on a condition
├── scripts/          <- optional
└── assets/           <- optional
```

Put it in the skill root the project's framework actually reads. That location
differs per framework, and getting it wrong means the skill is never seen.

Never nest a project skill inside a meta-skill's directory. It would be deleted
along with its host.

## Give each one an update trigger

Write down, in a project-visible file, **when this skill needs revisiting** —
"update when the release process changes". One line.

Without it the skill is accurate the day it is written and rots from there, and
a stale skill is worse than none: an agent that finds no skill asks, while an
agent that finds a wrong one follows it.

## Before you finish

- **No marker** in any skill you wrote. Check the description, not your memory.
- **No `meta-*` name.**
- `name` matches the directory.
- The description names concrete triggers and a boundary.
- Nothing in the skill points at a meta-skill or at the scaffolding — those
  files are about to stop existing.
- Each skill has an update trigger somewhere the project can see.

## Gotchas

- **A skill that never triggers is a skill that does not exist.** The most
  common failure is not bad content, it is a description written as a topic
  label. Spend the effort on the trigger.
- **Do not write a skill for something the entrypoint already says.** Two
  sources for one rule drift, and then agents follow whichever they read first.
- **Do not batch-create skills because the project looks like it deserves them.**
  Each one is permanent context. Write the ones with a real trigger and a real
  failure behind them; leave the rest.
