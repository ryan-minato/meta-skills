# Linters, Formatters, Type Checkers

Read when choosing the linter, formatter, or type checker, when the user
names an alternative to the Ruff/ty defaults, or when maturity
requirements rule out a young tool.

## Linters

| Tool | One line | Docs |
|---|---|---|
| Ruff (default) | Fast linter reimplementing the Flake8/isort/pyupgrade rule families under one config | <https://docs.astral.sh/ruff/> |
| Pylint | Deepest analysis and opinions, at a real speed cost | <https://pylint.readthedocs.io/> |
| Flake8 | The classic pluggable linter | <https://flake8.pycqa.org/> |
| Pyflakes | Error-only checking, no style opinions | <https://github.com/PyCQA/pyflakes> |

## Type Checkers

| Tool | One line | Docs |
|---|---|---|
| ty (default) | Fast checker and language server from the Ruff/uv team | <https://docs.astral.sh/ty/> |
| mypy | The reference implementation, most mature | <https://mypy.readthedocs.io/> |
| Pyright | Fast, strict, powers VS Code's Pylance | <https://microsoft.github.io/pyright/> |
| Pyre | Meta's checker for very large codebases | <https://pyre-check.org/> |

**ty maturity caveat:** ty is young. Before recording it, fetch its docs
and confirm it supports the project's Python version and the typing
features the codebase uses; when the user needs a settled checker, record
mypy or Pyright instead.

## Formatters

| Tool | One line | Docs |
|---|---|---|
| Ruff formatter (default) | Black-compatible formatter in the same binary as the linter | <https://docs.astral.sh/ruff/formatter/> |
| Black | The uncompromising formatter Ruff's is modeled on | <https://black.readthedocs.io/> |
| isort | Import sorting only | <https://pycqa.github.io/isort/> |
| autopep8 | Minimal fixer that only corrects PEP 8 violations | <https://github.com/hhatto/autopep8> |
| docformatter | Formats docstrings to PEP 257 | <https://docformatter.readthedocs.io/> |

Fetch current install commands and rule configuration from the docs above
before writing them into the target. The Astral sites publish plain-text
indexes — <https://docs.astral.sh/ruff/llms.txt> and
<https://docs.astral.sh/ty/llms.txt> — fetch those first to locate the
right page.

## Selection Rules

- Exactly one linter and one formatter; overlapping tools disagree at the
  margins and contributors lose.
- Import sorting goes through the linter's rules when it offers them
  (Ruff does); a separate isort next to Ruff is redundant.
- Pylint's depth is a deliberate speed trade for projects that want its
  extra analysis — a valid preference, not a default.
- Type-checking strictness is a recorded dial, not a virtue: start
  permissive on legacy code and strict on new code, and record where the
  dial sits and why. Never max it by default on an untyped codebase.
