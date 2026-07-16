# python — Catalog Context

Read this before authoring or reviewing anything in `skills/python/`.
Repository-wide rules live in
[meta-skill-contract.md](../../.agents/knowledge/meta-skill-contract.md);
this file adds only what is specific to `python`. Neither this file nor
the catalog READMEs ship to targets — installers copy skill directories
only.

## Goal

`python` holds information skills for Python target projects: trusted
defaults and authoritative doc URLs the harness-building agent consults
on demand when deciding documentation conventions, testing setup, and
toolchain. It installs per project, on top of `core`, and only when the
target is (predominantly) Python — it is not part of the default install.
These skills answer "which tool, which style, which default"; the
harness-build procedure itself belongs to `core` and is never restated
here.

## Constraints On What May Enter

- **Python-only usefulness.** A skill belongs here only if it is useless
  to a non-Python project. Anything useful regardless of stack belongs in
  `core`; anything tied to a different stack belongs in its own topic
  catalog.
- **Disposable only.** The marker admission test applies unchanged: if a
  skill should not carry it, it does not belong in this repository.
- **Defaults are defaults, not dogma.** Every default a skill records
  applies only when the user expressed no preference and the target shows
  no existing convention. No skill here may instruct migration away from
  a working existing choice; migration happens only when the user asks.
- **Upstream-URL fidelity.** Per-tool content is minimal — one line of
  positioning, an install pointer, and the authoritative doc URL. Volatile
  facts (versions, install commands, config syntax, plugin inventories)
  always defer to the URL with an instruction to fetch current details.
  A dead or moved URL is a bug, fixed in the same change that finds it.
- **Information, not procedure.** No step-by-step harness manual. Skills
  here produce recorded decisions; where those decisions get registered
  is `core`'s territory and is referenced only as "wherever the harness
  keeps conventions".

## Authoring

Start from the authoring skill's template
(`.agents/skills/meta-skill-authoring/assets/skill-template.md`), which
ships with the marker pre-filled. The marker's exact bytes and YAML form are
defined in the contract; copy them from there, never from rendered
documentation.

## References

- Astral docs hub (several category defaults live there) —
  <https://docs.astral.sh/>
- Agent Skills specification — reachable through the `agentskills` MCP
  server.

## Upstream Registry

Every doc URL the catalog's skills cite, with the standard install
command — a maintainer snapshot, last verified live 2026-07-16. The URL is
authoritative: when this table and a tool's docs disagree, the docs win
and this file updates in the same change. Sites that publish an `llms.txt`
plain-text index (agent-preferred; probe `<docs-root>/llms.txt`) are
marked — as of the verification date only the Astral sites do; re-probe
the others when refreshing this table. PyPI packages install with
`pip install <package>`; in a uv-managed project use
`uv add --dev <package>` (or `uv tool install` for standalone CLIs).

### Specs and stdlib (nothing to install)

| Doc | URL |
|---|---|
| PEP 257 (docstring conventions) | <https://peps.python.org/pep-0257/> |
| PEP 723 (inline script metadata) | <https://peps.python.org/pep-0723/> |
| Google Python Style Guide | <https://google.github.io/styleguide/pyguide.html> |
| numpydoc format | <https://numpydoc.readthedocs.io/en/latest/format.html> |
| Sphinx napoleon extension | <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html> |
| Sphinx Python domain (reST fields) | <https://www.sphinx-doc.org/en/master/usage/domains/python.html> |
| doctest | <https://docs.python.org/3/library/doctest.html> |
| unittest | <https://docs.python.org/3/library/unittest.html> |
| unittest.mock | <https://docs.python.org/3/library/unittest.mock.html> |

### Testing

| Tool | Install | Docs |
|---|---|---|
| pytest | `pip install pytest` | <https://docs.pytest.org/> |
| pytest-cov | `pip install pytest-cov` | <https://pytest-cov.readthedocs.io/> |
| coverage.py | `pip install coverage` | <https://coverage.readthedocs.io/> |
| pytest-mock | `pip install pytest-mock` | <https://pytest-mock.readthedocs.io/> |
| pytest-asyncio | `pip install pytest-asyncio` | <https://pytest-asyncio.readthedocs.io/> |
| anyio | `pip install anyio` | <https://anyio.readthedocs.io/> |
| pytest-xdist | `pip install pytest-xdist` | <https://pytest-xdist.readthedocs.io/> |
| pytest-timeout | `pip install pytest-timeout` | <https://github.com/pytest-dev/pytest-timeout> |
| pytest-randomly | `pip install pytest-randomly` | <https://github.com/pytest-dev/pytest-randomly> |
| Hypothesis | `pip install hypothesis` | <https://hypothesis.readthedocs.io/> |

### Dependency managers

| Tool | Install | Docs |
|---|---|---|
| uv | `curl -LsSf https://astral.sh/uv/install.sh \| sh` | <https://docs.astral.sh/uv/> — llms.txt: <https://docs.astral.sh/uv/llms.txt> |
| Poetry | `pipx install poetry` | <https://python-poetry.org/docs/> |
| PDM | `pipx install pdm` | <https://pdm-project.org/> |
| Hatch | `pipx install hatch` | <https://hatch.pypa.io/> |
| pip | bundled with Python (`python -m ensurepip`) | <https://pip.pypa.io/> |
| pip-tools | `pip install pip-tools` | <https://pip-tools.readthedocs.io/> |
| micromamba | `"${SHELL}" <(curl -L micro.mamba.pm/install.sh)` | <https://mamba.readthedocs.io/> |

### Lint, format, types

| Tool | Install | Docs |
|---|---|---|
| Ruff | `pip install ruff` | <https://docs.astral.sh/ruff/> — llms.txt: <https://docs.astral.sh/ruff/llms.txt> |
| Pylint | `pip install pylint` | <https://pylint.readthedocs.io/> |
| Flake8 | `pip install flake8` | <https://flake8.pycqa.org/> |
| Pyflakes | `pip install pyflakes` | <https://github.com/PyCQA/pyflakes> |
| ty | `pip install ty` | <https://docs.astral.sh/ty/> — llms.txt: <https://docs.astral.sh/ty/llms.txt> |
| mypy | `pip install mypy` | <https://mypy.readthedocs.io/> |
| Pyright | `pip install pyright` | <https://microsoft.github.io/pyright/> |
| Pyre | `pip install pyre-check` | <https://pyre-check.org/> |
| Black | `pip install black` | <https://black.readthedocs.io/> |
| isort | `pip install isort` | <https://pycqa.github.io/isort/> |
| autopep8 | `pip install autopep8` | <https://github.com/hhatto/autopep8> |
| docformatter | `pip install docformatter` | <https://docformatter.readthedocs.io/> |

### Tasks, hooks, docs

| Tool | Install | Docs |
|---|---|---|
| just | prebuilt binaries / system package manager (see docs); `cargo install just` | <https://just.systems/man/en/> |
| Poe the Poet | `pipx install poethepoet` | <https://poethepoet.natn.io/> |
| Invoke | `pip install invoke` | <https://www.pyinvoke.org/> |
| Nox | `pipx install nox` | <https://nox.thea.codes/> |
| tox | `pip install tox` | <https://tox.wiki/> |
| Make | system package manager | <https://www.gnu.org/software/make/manual/> |
| pre-commit | `pip install pre-commit` | <https://pre-commit.com/> |
| Zensical | `pip install zensical` | <https://zensical.org/docs/> |
| MkDocs | `pip install mkdocs` | <https://www.mkdocs.org/> |
| Material for MkDocs | `pip install mkdocs-material` | <https://squidfunk.github.io/mkdocs-material/> |
| Sphinx | `pip install sphinx` | <https://www.sphinx-doc.org/> |
| mkdocstrings | `pip install mkdocstrings` | <https://mkdocstrings.github.io/> |
