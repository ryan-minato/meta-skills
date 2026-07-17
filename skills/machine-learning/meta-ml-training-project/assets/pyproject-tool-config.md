# pyproject.toml Tool Tables

Copy the block below into the target's `pyproject.toml`, then rework it:
drop the per-file-ignores for directories the project does not have yet
(restore them when the directory appears), and verify the rule codes
against the current Ruff docs before committing. No type-checker table
belongs here — this scaffold does not add one.

````toml
[tool.ruff]
line-length = 120

[tool.ruff.format]
docstring-code-format = true
docstring-code-line-length = 80

[tool.ruff.lint]
extend-select = [
    "I",    # isort: Import sorting
    "N",    # pep8-naming: Check PEP 8 naming conventions
    "TID",  # flake8-tidy-imports: Import policy checks
    "W",    # pycodestyle warning: PEP 8 styling warnings
]
unfixable = [
    "F401", # unused-import: Unused import
]

[tool.ruff.lint.per-file-ignores]
"scripts/*" = [
    "TID",  # flake8-tidy-imports: Tidy up imports
]
"tests/**/*" = [
    "TID252",   # relative-imports: Relative imports ban
]

[tool.ruff.lint.flake8-tidy-imports]
ban-relative-imports = "all"

[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ra -q"
testpaths = ["tests"]
markers = [
    "slow: manual-only tests that may require GPU, model downloads, or long runs",
]
````

What the choices buy:

- 120-char lines fit tensor-shape-heavy code without wrapping every
  call; the 80-char docstring-code limit keeps examples readable in
  hovers.
- `I`/`N`/`W` catch the mechanical style drift reviews waste time on;
  `TID` with `ban-relative-imports` keeps every import absolute, so
  moving a file never silently breaks siblings — `scripts/` and `tests/`
  relax exactly the parts that don't apply to them.
- `F401` unfixable stops the formatter from deleting an import someone
  just added for the next edit.
- The `slow` marker is the load-bearing line: `just test` runs
  `-m "not slow"`, and nothing GPU-bound or long ever enters hooks or CI.
