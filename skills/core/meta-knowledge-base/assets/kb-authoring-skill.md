---
name: knowledge-authoring
description: >-
  Applies this project's knowledge-base conventions when creating,
  editing, or relocating a knowledge document. Use when adding or
  changing any document under <knowledge location>, or when recording a
  new fact, plan, or decision for future agents.
---

# Knowledge Authoring

Rules for this project's knowledge base at `<knowledge location>`.

## Rules

1. Structure is <flat files per concern | per-topic folders>: put a new
   document at `<pattern, e.g. .agents/knowledge/<topic>.md>`. Never
   introduce the other structure.
2. Write agent-first: load condition in the first line ("Read when …"),
   facts before narrative, one concern per file, no pleasantries.
3. Use absolute dates. Delete or fix anything you find that contradicts
   the code — a stale fact is worse than none.
4. Register every new or moved document in the entrypoint's when-to-read
   table in the same change.
5. Do not create a document for what the code already shows, for one-off
   session context, or for public README-class files.

Done when: the document reads correctly on its own, its when-to-read row
exists, and no duplicate of its facts remains elsewhere.
