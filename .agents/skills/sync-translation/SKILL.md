---
name: sync-translation
description: >
  Mirrors an English README into its Chinese README.zh.md counterpart, keeping
  the pair content-identical. Use when any README.md changes, when a new README.md
  is added, or when `just validate-repo` reports a missing translation. Not for
  translating skill content, which ships in English only.
---

# Translation Sync

## Source Of Truth

`README.md` is authoritative. `README.zh.md` mirrors it. When the two disagree,
the English wins and the Chinese is corrected — never the reverse.

## Dependent Artifacts

- `README.zh.md` at the repository root
- `skills/<catalog>/README.zh.md` for every catalog

## Workflow

1. Identify every `README.md` that changed, and read its `README.zh.md` sibling.
2. Compare them section by section. The mirror must carry the same sections in
   the same order with the same meaning.
3. Update the Chinese file. Translate prose; keep commands, paths, code blocks,
   table structure, and the marker literal byte-identical.
4. Check the language-swap link at the top: `README.md` opens with a
   `[中文](README.zh.md)` link, and `README.zh.md` links back with
   `[English](README.md)`.
5. Run `just validate-repo`, which enforces that the pair exists.

## Gotchas

- The validator only checks that `README.zh.md` **exists**, not that it says the
  same thing. Content drift is invisible to tooling and is exactly what this
  skill is for.
- Never translate the marker, a `just` recipe name, or a path. A translated
  marker stops matching and silently un-marks the skill.
- Adding a `README.md` anywhere obliges a `README.zh.md` beside it, including for
  a brand-new catalog.
