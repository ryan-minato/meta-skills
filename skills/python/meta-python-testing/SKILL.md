---
name: meta-python-testing
description: >-
  Disposable meta-skill (delete after the harness is built): supplies
  trustworthy defaults for a Python project's testing setup — pytest as
  the default framework (unittest and doctest when constraints call for
  them), plugin selection by named need (coverage, mocking, async,
  parallel, timeouts, randomization, property-based) with doc URLs, and a
  test-style doctrine: Arrange-Act-Assert, the classical school over the
  mockist school, real objects over mocks, state verification,
  parametrized tests, and error paths always tested. Use when a harness
  build must choose or record how a Python project is tested and the user
  has not fully specified it. Not for writing the tests themselves, and
  not for non-Python projects.
---

# Python Testing Conventions

This skill produces the framework choice, plugin selection, and test-style
doctrine a harness build records for a Python target project. It is
deliberately thin on tool details — current install commands and
configuration are fetched from each cited doc URL, never recalled from
memory — and its defaults apply only where the user and the existing test
suite are both silent.

## Workflow

1. Detect the existing testing reality: a `tests/` layout, framework
   imports in test files, configuration (`[tool.pytest.ini_options]` in
   `pyproject.toml`, `pytest.ini`, `tox.ini`, `setup.cfg`), and CI test
   jobs. Existing consistent choices win — record them with their doc
   URLs instead of replacing them.
2. Choose the framework — default **pytest**. When no framework is present
   yet, the user questions the default, or a constraint applies
   (stdlib-only environment, executable docstring examples), read
   [frameworks.md](references/frameworks.md) for the selection logic and
   each framework's doc URL, then fetch current install and configuration
   from the chosen framework's docs.
3. Select plugins against concrete needs — read
   [pytest-plugins.md](references/pytest-plugins.md) when a need exists
   (coverage, mocking, async code, a slow suite, hangs, order coupling,
   property-based rigor). Install only what a named need justifies;
   coverage is the one near-universal addition.
4. Record the test-style doctrine. The defaults, each recordable as-is:
   - Tests read as Arrange-Act-Assert: set up, do the one thing, verify.
   - Classical school: exercise real behavior; use test doubles only at
     boundaries the project does not own (network, clock, external
     services).
   - Double preference ladder: real object > fake > stub > mock.
   - Verify state (what the system ended up as), not interactions —
     unless the interaction itself is the contract.
   - Parametrize families of cases instead of copy-pasting test bodies.
   - Example-based tests by default; property-based where rigor pays
     (algorithms, parsers, invariant-rich code).
   - Expected exceptions and error paths are always tested, not just the
     happy path.
5. When the user or the codebase pulls against one of those defaults, read
   [test-doctrine.md](references/test-doctrine.md) before deviating — it
   carries the vocabulary (Given-When-Then, the full double taxonomy,
   behavior verification) and the trade-offs, so the deviation is
   deliberate and recorded with its reason.
6. Record it all wherever the harness keeps conventions: the framework and
   plugins with their doc URLs and the need each plugin serves, the
   doctrine bullets, and the exact command that runs the suite. Put runner
   configuration wherever the project already keeps tool configuration —
   commonly `pyproject.toml` — rather than introducing a new file.

Done when: the harness records the framework, a plugin list where every
entry names its need, the doctrine, and the command that runs the suite,
each tool with its doc URL.

## Gotchas

- Speculative plugin installs rot; a plugin recorded without a need is a
  future dependency problem, not a capability.
- Test-order randomization changes reproducibility — record how to re-run
  with a fixed seed before enabling it.
- Async tests silently pass or skip when the async plugin's mode is not
  configured — fetch the current mode settings from its docs before
  recording the convention.
- Doctests do not run unless collection is switched on; promising
  executable examples without recording the collection mechanism promises
  nothing.
- Do not invent a coverage threshold during harness setup — record
  "measured, threshold set once a baseline exists" instead.
- Mocking code the project owns calcifies its current design; when a test
  needs a double for an owned class, that is design feedback, not a
  mocking task.
