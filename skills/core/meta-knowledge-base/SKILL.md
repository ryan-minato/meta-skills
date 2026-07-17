---
name: meta-knowledge-base
description: >-
  Disposable meta-skill (delete after the harness is built): creates,
  improves, or reorganizes the project's agent knowledge base, and
  deposits the authoring rules where agents can find them. Use when the
  harness plan or the user calls for a knowledge base, or when project
  knowledge is scattered, inconsistent, or unreachable from the
  entrypoint. Not for the entrypoint itself or for public README-class
  files.
---

# Knowledge Base

This skill produces the project's agent knowledge base: documents written
agent-first — terse, facts up front, a load condition at the top, one
concern per file, no pleasantries — in one consistent structure agents can
predict. It expects a harness plan (default
`.agents/knowledge/harness-plan.md`); without one, ask the user only where
knowledge should live and whether the team already maintains truth
somewhere else.

## Workflow

1. Choose the location. Default in-repo, commonly `.agents/knowledge/`,
   because knowledge then versions with the code. Choose an external
   backend (an issue tracker's documents, a wiki) only when the team
   already maintains truth there or the user asks — then read
   [external-backend.md](references/external-backend.md) first.
2. Fix exactly one structure and record it: flat files per concern
   (`references.md`, `plans.md`) or per-topic folders
   (`references/torch.md`). Never mix the two — agents must be able to
   infer where a fact lives without searching.
3. If knowledge already exists scattered or structure is mixed, read
   [reorganize.md](references/reorganize.md) and converge it before
   seeding anything new.
4. Seed only documents a current need justifies — no placeholders, no
   empty folders. Copy the matching type asset and rework it against the
   project (delete what does not apply, fill real content, drop the
   fill-in guidance):
   - facts about a dependency, system, or domain →
     [reference-doc.md](assets/reference-doc.md)
   - ongoing work with a goal and next steps →
     [plan-doc.md](assets/plan-doc.md)
   - a decision that binds future work →
     [decision-doc.md](assets/decision-doc.md)
   - an index, when the backend is external or documents number more than
     a handful → [index-doc.md](assets/index-doc.md)
5. Deposit the authoring rules where agents will find them, in the form
   matching the plan's sync-family decision: a durable project skill from
   [kb-authoring-skill.md](assets/kb-authoring-skill.md) when the project
   uses or will use skills, otherwise a section from
   [kb-conventions-section.md](assets/kb-conventions-section.md) embedded
   in the entrypoint's knowledge section or the knowledge index. Adapt
   either to the structure chosen in step 2.
6. Register every document in the entrypoint's when-to-read table.
   Knowledge files never announce themselves; an unregistered document is
   invisible.
7. If the plan marks a weak-model target, confirm the entrypoint teaches
   section lookup by line number; if it does not, instruct the user to
   install and run the AGENTS.md meta-skill.

Done when: one structure is fixed and recorded, every knowledge document
is registered in the entrypoint, and the authoring rules live in the
project in agent-reachable form.

## Gotchas

- One project, one structure. A mixed structure means every future lookup
  is a search.
- Agent-first means terse, not cryptic: short files of plain statements,
  not compressed jargon.
- Public-convention files are not knowledge documents. Never rewrite a
  README into agent style, and never count it toward the knowledge base.
- An external knowledge base agents cannot reach through a documented
  access path does not exist in practice.
- Seeding from a type asset without reworking it leaves template prose in
  the knowledge base — worse than no document.
