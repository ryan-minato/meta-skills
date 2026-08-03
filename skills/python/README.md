# python

[中文](README.zh.md)

Meta-skills for Python target projects: trusted defaults and authoritative
doc URLs for documentation conventions, testing setup, and toolchain
choices, plus locating a package's documentation. Install on top of `core`,
per project, and only when the target is a Python project — this catalog is
not part of the default install.

These skills are **disposable**: once the harness is built and verified,
the `core` removal skill deletes them together with the rest.

```bash
claude plugin marketplace add ryan-minato/meta-skills   # once per machine
claude plugin install python@meta-skills --scope project
# or via the skills CLI (the catalog path scopes discovery):
npx skills add ryan-minato/meta-skills/skills/python
npx skills add ryan-minato/meta-skills/skills/python --skill <skill-name>
```

## Skills

| Skill | Description |
|---|---|
| [meta-python-docstyle](meta-python-docstyle/) | Defaults for docstring style (Google by default; NumPy and reST covered), docstring completeness per object kind, a self-documenting-code comment philosophy, and a marker-comment policy, with upstream doc URLs |
| [meta-python-pypi-lookup](meta-python-pypi-lookup/) | Locates a package's authoritative documentation entry point from PyPI/conda metadata, preferring an agent-oriented `.md` or `llms.txt` rendition, for packages no docs map already records |
| [meta-python-testing](meta-python-testing/) | Defaults for the test framework (pytest), plugin selection by named need, and a test-style doctrine: Arrange-Act-Assert, the classical school, real objects over mocks, state verification, error paths always tested |
| [meta-python-toolchain](meta-python-toolchain/) | Defaults and doc URLs for dependency management (uv), linting and formatting (Ruff), type checking (ty), task running (just), git hooks (pre-commit), and documentation (Zensical), with the established alternatives |
