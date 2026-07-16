---
name: meta-agents-md
description: >-
  Disposable meta-skill (delete after the harness is built): creates,
  improves, or edits the project's AGENTS.md entrypoint and its framework
  pointer files, including offloading long architecture and stack material
  into an architecture document behind section-locating pointers. Use when
  the harness plan or the user calls for writing, restructuring, or
  slimming the agent entrypoint or the architecture document it points to.
  Not for knowledge documents, project skills, or public README-class
  files.
---

# AGENTS.md

This skill produces the project's agent entrypoint: an `AGENTS.md` that
every harness rule is either stated in or reachable from, plus the pointer
files agent frameworks look for. AGENTS.md is agent-only — terse, facts
first, no pleasantries, no human-readability duty. It expects a harness
plan (default `.agents/knowledge/harness-plan.md`); without one, collect
just these decisions from the user: model class, and which conventions and
checks already exist.

## Workflow

1. Read the harness plan if present. Inventory what the entrypoint must
   route to: conventions, commands, checks, knowledge documents, skills.
2. If no `AGENTS.md` exists, start from
   [agents-md-skeleton.md](assets/agents-md-skeleton.md): copy it, then
   rework every section against this project — delete inapplicable
   sections, replace placeholders with real commands and paths, and add
   sections the skeleton did not foresee. If one exists, edit in place and
   keep its working structure.
3. Hold the length budget: about 100 lines, up to about 200 only when the
   entrypoint is the whole harness. Every line loads into every session.
4. Point framework entry files at AGENTS.md instead of duplicating it —
   for example `CLAUDE.md` containing only a reference to `AGENTS.md`.
   Duplicate content in two entry files always diverges.
5. When architecture, stack, or layout material pushes past the budget —
   or an architecture document is being created or edited — read
   [offload.md](references/offload.md) and move that material out behind a
   section-locating pointer, starting the document from
   [architecture-md-skeleton.md](assets/architecture-md-skeleton.md).
6. Build the when-to-read table: one row per knowledge or reference
   document — name, one-line hook, when to read it. Knowledge files are
   the one harness component with no self-announcement; this table is how
   agents find them.
7. If the plan marks a weak or local model target, copy the section-lookup
   block from [section-lookup.md](assets/section-lookup.md) into
   AGENTS.md and adapt its example paths.
8. Verify: every link resolves; the budget holds; every harness rule is
   stated or reachable; no rule appears in two files; the user approves.

Done when: AGENTS.md exists within budget, framework entry files point to
it, every offloaded topic has a resolving section-locating pointer, and the
when-to-read table covers every knowledge document.

## Gotchas

- The pointer's inline-code heading must reproduce the target heading line
  byte-exactly, `##` included — one changed character and line lookup
  breaks.
- Never state the same rule in AGENTS.md and the architecture document;
  one owns it, the other points.
- Write direct instructions under plain headings; do not coin names for
  principles. Name tool categories, not products, except concrete entry
  filenames.
- The architecture document is a public-convention file: human-readable
  prose, not agent-terse style.
- Deploying the skeleton with placeholders intact is a failure — every
  placeholder is a decision this project still owes.
