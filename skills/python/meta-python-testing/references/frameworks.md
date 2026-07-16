# Test Frameworks

Read when choosing the test framework: none is installed yet, the user
questions the pytest default, or an environment constraint (stdlib-only,
executable docstring examples) applies.

## Selection Logic

- **pytest (default).** Plain `assert` statements, fixtures,
  parametrization, and the ecosystem's plugin surface. Choose it unless a
  constraint below overrides.
- **unittest** wins only under two conditions: the environment must stay
  stdlib-only (no third-party installs), or a large existing unittest
  suite is entrenched — pytest can *run* unittest suites, so even then
  pytest often layers on top rather than being ruled out.
- **doctest** is a complement, never the main suite: it turns docstring
  examples into executable documentation. Run it through its own runner
  or through pytest's doctest collection; either way, record which
  mechanism collects the examples or they will never execute.

## Frameworks

| Framework | Package | Docs |
|---|---|---|
| pytest | `pytest` | <https://docs.pytest.org/> |
| unittest | stdlib | <https://docs.python.org/3/library/unittest.html> |
| unittest.mock | stdlib | <https://docs.python.org/3/library/unittest.mock.html> |
| doctest | stdlib | <https://docs.python.org/3/library/doctest.html> |

Fetch current install commands and configuration from the docs above
before writing them into the target — versions and config syntax change;
the selection logic does not.
