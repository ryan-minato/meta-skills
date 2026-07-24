# References

Load before adding, upgrading, replacing, or using a dependency, service, data
source, or external model.

| Component | Role | Official documentation | Adopted because |
|---|---|---|---|
| uv | dependencies and lockfile | <https://docs.astral.sh/uv/> | reproducible Python environment |
| Ruff | lint and format | <https://docs.astral.sh/ruff/> | one fast quality tool |
| pytest | focused tests | <https://docs.pytest.org/> | tests for custom risky logic |
| Pydantic Settings | TOML and environment config | <https://pydantic.dev/docs/> | validated configuration |
| Just | workflow command surface | <https://just.systems/man/en/> | readable pipeline entrypoints |
| pre-commit | Git hooks | <https://pre-commit.com/> | repeatable commit gates |
| EditorConfig | editor basics | <https://editorconfig.org/> | consistent text files |
| Loguru | observable workflows | <https://loguru.readthedocs.io/> | contextual operational logs |
| Gitleaks | automated secret scanning | <https://github.com/gitleaks/gitleaks> | protect public Git history |
| Jupyter | notebook exploration | <https://docs.jupyter.org/> | statistics and visualization |

Add only selected storage, compute, and model tools. Record upstream repository
and exact commit for any reimplemented experimental model.
