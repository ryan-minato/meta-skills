# Sync Skill Skeleton

One durable sync skill per concern, for the skill family. Copy the block
into a new skill directory, then rework it: the real document, the real
artifacts, the real triggering changes. It stays after the meta-skills are
removed — its description must never begin with the marker those
disposable skills carry.

````markdown
---
name: sync-<document>
description: >-
  Keeps <document> true to <what it describes>. Use when a change
  touches <the concrete artifacts: commands, checks, structure,
  section headings>, or when asked to update <document> itself.
---

# Sync: <Document>

<Document> describes <artifacts>. This skill runs in both directions.

## When A Change Touches The Subject

1. <change kind> → update <the document part it invalidates>.
2. <change kind> → <document part>.
Apply the update in the same change, not as a follow-up.

## Before Editing The Document

Inspect first; fix or report every mismatch found, not only the one that
prompted the edit:

- <artifact check, e.g. run each listed command>
- <artifact check, e.g. confirm each pointer's heading still matches
  byte-exactly>

Done when: the document says nothing the code contradicts, and the
inspection list above ran clean.
````
