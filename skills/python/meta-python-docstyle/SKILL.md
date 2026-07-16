---
name: meta-python-docstyle
description: >-
  Disposable meta-skill (delete after the harness is built): supplies
  trustworthy defaults for a Python project's documentation conventions —
  docstring style (Google by default; NumPy or reST when the ecosystem
  calls for them), docstring completeness per object kind, a
  self-documenting-code comment philosophy, and a marker-comment policy
  (TODO, FIXME, NOTE by default) — recorded in the harness with upstream
  doc URLs. Use when a harness build needs Python docstring or comment
  conventions and the user has not fully specified them. Not for writing
  the docstrings themselves, and not for non-Python projects.
---

# Python Docstring & Comment Conventions

This skill produces a recorded documentation convention — docstring style,
docstring depth, comment philosophy, and marker-comment policy — for a
Python target project's harness. It expects a harness build in progress and
supplies defaults only where the user and the codebase are both silent; an
existing consistent convention always wins and is recorded, never restyled.

## Workflow

1. Detect what the project already does: sample existing docstrings across
   a few modules, check `pyproject.toml` and lint configuration for a
   docstring-convention setting, check a Sphinx `conf.py` for the napoleon
   extension, and read any CONTRIBUTING notes. A consistent existing style
   wins — record it with its upstream URL and stop choosing.
2. Choose the docstring style — default **Google style**. When no existing
   convention or explicit user preference decides it, or when writing the
   chosen style's rules into the harness, read
   [docstring-styles.md](references/docstring-styles.md): it carries the
   selection logic (NumPy style for scientific-stack projects, reST for
   projects already deep in plain Sphinx autodoc), the shared PEP 257
   baseline, and the upstream URL for each style.
3. Set docstring completeness. When the user did not specify how thorough
   docstrings must be, read
   [completeness-defaults.md](references/completeness-defaults.md) and
   record its per-object-kind table, adapted to whether the project is an
   application or a published library.
4. Record the comment philosophy. The default doctrine, verbatim:
   - Code should be self-documenting; a clear line needs no comment, and
     commenting it insults the reader.
   - Never comment line-by-line or at a granularity that restates the
     code.
   - When code is genuinely obscure or long, comment at the level of a
     logical block — one complete behavior per comment — so a reader can
     skim the flow without parsing every line.
   - Comments explain *why* (constraints, non-obvious causes); the code
     itself shows *what*.
5. Set the marker-comment policy — default vocabulary **TODO, FIXME, and
   NOTE only**, written as `TAG(owner-or-issue): text`. When the codebase
   already uses other tags or the user wants a richer vocabulary, read
   [comment-markers.md](references/comment-markers.md) for the full tag
   meanings and the closed-set rule.
6. Record the decisions — style with its upstream URL, the depth table, the
   comment doctrine, and the marker policy — wherever the harness keeps
   conventions. If the project lints docstrings, note the enforcement knob
   generically: most linters expose a docstring-convention setting; fetch
   its current syntax from the linter's own docs.

Done when: the harness records the docstring style (with upstream URL), the
per-object-kind depth requirements, the comment philosophy, and the marker
policy, and none of them contradict what the codebase already does.

## Gotchas

- Never mix docstring styles in one project — renderers and linters assume
  one convention, and mixed sections render as prose soup.
- Doctest examples in docstrings only run if something collects them;
  record the run mechanism alongside the convention, or do not promise
  executable examples.
- Recording requirements stricter than the existing code satisfies turns
  every future edit into a violation — flag the gap to the user instead of
  silently mandating a migration.
- A comment-density mandate ("every function gets a comment") contradicts
  the philosophy above; depth requirements apply to docstrings, never to
  comments.
