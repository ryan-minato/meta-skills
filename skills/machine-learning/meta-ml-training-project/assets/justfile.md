# Justfile Skeleton — Training Project

Copy the block below into the target project's `justfile`, then rework
it: keep one `train`/`eval` pair per real entry script and delete
recipes for workflows the project lacks. Container recipes are added
only through the containers branch, not by default.

````just
# Create the dev environment from the committed lockfile.
setup:
    uv sync
    uv run pre-commit install

train *args:
    uv run python train.py {{args}}

# Multi-GPU runs: swap the recipe body for
# `uv run accelerate launch train.py {{args}}`.

eval *args:
    uv run python eval.py {{args}}

lint:
    uv run ruff format .
    uv run ruff check --fix .

test:
    uv run pytest -m "not slow"

# GPU/long tests; run by hand, never from hooks or CI.
test-slow:
    uv run pytest -m slow
````
