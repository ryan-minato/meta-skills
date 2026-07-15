---
name: meta-disposal
description: >
  [META-SKILL: remove after harness setup]
  Removes the meta-skills from a project once its harness is built and verified:
  reconciles the pre-build manifest against the removal marker in each parsed
  description, dry-runs the result for a human to approve, checks that no
  surviving file still points at them, then deletes each directory and itself
  last. Use when a harness build is finished and verified, or when asked to
  clean up, dispose of, or remove the meta-skills or the scaffolding. Not for
  deleting a project's own durable skills, and not for uninstalling ordinary
  skills a user wants to keep.
---

# Meta-Skill Disposal

Meta-skills are scaffolding. Once the harness stands on its own, they are pure
context cost in every future session, and removing them is the last step of the
job they were installed for.

**This procedure must never be scary.** One over-broad deletion and people stop
running cleanup at all — after which meta-skills live forever in every project
that ever installed them, which is the exact waste this exists to prevent. When
in doubt, show the human and ask. A cleanup that stops to ask is working; a
cleanup that deletes something it shouldn't have is unrecoverable.

## Gate: is the harness actually verified?

Do not start until the harness has passed **the project's own verification** —
the commands or checks the project documents for itself.

- The project documents checks → run them. They pass → proceed. They fail →
  stop and report. The scaffolding stays; it is what fixes the harness.
- The project documents no checks → **stop and ask the user.** Do not substitute
  your own judgment that the harness looks finished. "It looks done to me" is
  not verification, and you are about to delete the thing that could rebuild it.

## Step 1 — Read the pre-build manifest

Look for `META-SKILL-MANIFEST.md` in each skill root. It is a snapshot of the
meta-skills that were installed **before the build began**, and it is the first
authority here.

It matters because the build *creates* skills. By the time you are deleting,
a skill root can hold both meta-skills and durable skills the build just wrote,
and the only thing separating them is the marker — which is exactly the thing
that can be wrong. The manifest was taken when the answer was still unambiguous.

**No manifest?** Fall back to marker-only discovery and **say so plainly**:

> No pre-build manifest found, so I am going by the marker alone. A meta-skill
> whose description was rewritten at install time will be missed, and a
> generated skill that wrongly inherited the marker will look like a meta-skill.

Then be correspondingly more careful in the dry-run. The manifest is a
strengthener, not a precondition.

## Step 2 — Enumerate the skill roots

Scope to **the project's own skill roots**. Never a global or user-level root
(`~/.claude/skills`, `~/.agents/skills`, `/etc/...`): the user installed those
for every project, and this build has no mandate over them.

Enumerate `<skill-root>/<name>/SKILL.md` at **depth 2 exactly**, parse each
file's frontmatter, and test whether the resolved `description` starts with:

```text
[META-SKILL: remove after harness setup]
```

**Never discover by recursive grep.** Documentation quotes that marker — this
very file does, right above. Prose has no `description` field, so parsing cannot
match it, while a grep matches everything and would put a README on the deletion
list. Parsing is what makes discovery safe, not caution.

Parse, then test the *resolved* value. The description is a folded YAML scalar,
so the marker may legally be re-wrapped across lines; a regex over raw text
would reject a conformant skill.

If the environment has `uv`, or Python with PyYAML, running
[find_meta_skills.py](scripts/find_meta_skills.py) does this enumeration for
you:

```bash
uv run scripts/find_meta_skills.py --skill-root .claude/skills
uv run scripts/find_meta_skills.py --skill-root .claude/skills --json
```

`--skill-root` is repeatable and required. The script only reports — it has no
delete flag, deliberately, so that the dry-run gate cannot be skipped by running
it. **It is an accelerator, not the path.** With no Python available, enumerate
by hand: same roots, same depth-2 rule, same parse-then-test. Reading the files
yourself is not a degraded fallback, only a slower one.

## Step 3 — Reconcile the manifest against what is there

| On the manifest | Marker present now | What it means |
|:---:|:---:|---|
| yes | yes | A meta-skill, as expected. Delete it. |
| yes | no | The description was rewritten after installation. **Still delete it** — the manifest is the evidence — but tell the human why the marker is missing. |
| no | yes | **Stop. Never delete this one automatically.** |
| no | no | Not ours. Do not touch it. |

The third row is why the manifest exists. A skill carrying the marker that was
*not* installed as scaffolding is one of two things:

1. **A skill the build generated that wrongly inherited the marker.** This is a
   bug in the harness, and the fix is to *strip the marker from it*, not to
   delete it. Deleting would destroy the project's own new skill moments after
   the build reported success — silently, which is precisely what the manifest
   turns into a visible discrepancy.
2. Something installed part-way through the build.

Either way: surface it, explain both possibilities, and let the human choose.

## Step 4 — Dry run

Show the human, before deleting anything:

- every **resolved path** slated for deletion,
- each skill's **first description line**, so the listing can be judged rather
  than trusted,
- the **reconciliation verdict** from step 3,
- any directory named `meta-*` that carries **no** marker, as *"possible
  meta-skill, marker missing — confirm?"*. The name is a hint for a human and
  nothing more; installers rename skills, so it carries no contract and may be
  pure coincidence,
- any **near-miss**: a description that almost matches the marker. Report the
  differing codepoint, never the string. A `U+00A0` renders identically to a
  space, so a listing that shows both and invites a human to compare them is
  worse than useless — it looks like the tool is broken,
- any **symlink** among the candidates, flagged for manual confirmation.

This listing is the thing being approved. It is not a status report.

## Step 5 — Get fresh confirmation

**Ask now, for this deletion, in these words.** An earlier "build me a harness"
is not consent to delete, and neither is approval of the build plan. The user
agreed to gain a harness; nobody has yet agreed to lose these files.

Proceed only on an unambiguous yes to the dry-run you just showed.

## Step 6 — Check for dangling pointers

Before deleting, scan the surviving harness — `AGENTS.md`, `CLAUDE.md`,
knowledge files, project skills, CI config — for references to any skill you are
about to remove.

A harness that points into a deleted directory is **worse than no cleanup**:
every future agent follows the pointer, finds nothing, and has no way to know
what was supposed to be there.

Found one? Stop and fix the pointer first. The reference is a real defect — a
durable file was never supposed to depend on scaffolding — and deleting around
it just hides the defect behind a broken link.

## Step 7 — Delete

- Delete the **whole skill directory**, not just `SKILL.md`. A leftover
  `scripts/` or `references/` is orphaned garbage nothing will ever claim.
- **A symlink candidate is unlinked, never followed.** Remove the link itself.
  Recursing through it would leave the project and delete from a shared or
  global install that other projects depend on.
- Delete `META-SKILL-MANIFEST.md` too, once the skills it lists are gone. It
  names the meta-skills, so leaving it behind creates exactly the dangling
  pointer step 6 forbids.
- **Delete this skill last.** That is safe: this file is already in your context
  by the time you get here, so removing it does not interrupt the run.

## Step 8 — Verify

Confirm that no marked skill and no manifest remain in the project's skill
roots. Then report what was removed.

**Finding nothing is success.** Zero markers means the job is already done —
report "nothing to remove" and stop. Running this twice must be safe and boring.

## Gotchas

- **The description channel is best-effort, not a guarantee.** An installer that
  rewrites descriptions breaks it exactly the way renaming broke the name
  channel. This is why the manifest is the first authority and the marker the
  second. Say this honestly rather than implying the contract is airtight.
- **A near-miss marker is invisible.** A description carrying a `U+00A0`, a
  smart quote, or `[Meta-Skill:` does not match, so cleanup silently skips that
  skill while its author believes it is marked. If a `meta-*` directory looks
  like scaffolding but is not matching, compare the description codepoint by
  codepoint before concluding it is durable.
- **Never widen the search when you find nothing.** The temptation is to grep
  harder, or to reach into a global root. Both are how this procedure starts
  deleting things nobody asked it to.
