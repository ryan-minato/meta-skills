---
name: sync-translation
description: >-
  Mirrors an English README into its Chinese README.zh.md counterpart,
  keeping the pair content-identical. Use when any README.md is created or
  edited, or when the validator reports a missing README.zh.md. Not for
  skill content, which ships in English only.
metadata:
  internal: true
---

# Sync: README Translation

`README.md` is authoritative; `README.zh.md` mirrors it.

## Workflow

1. Mirror section by section: same heading order, same tables, same rows.
2. Translate prose only. Keep verbatim: commands, paths, file and skill
   names, code blocks, and the marker — byte-identical, including its fence
   info string.
3. Keep the language-swap links (`[中文]` / `[English]`) working in both
   directions.
4. Update the pair in the same commit as the English change.
5. Run `just validate`; check C1 confirms existence, but content parity is
   on you — the validator cannot judge it.

## Gotchas

- Never translate the marker or a fence info string; check D1 compares
  bytes.
