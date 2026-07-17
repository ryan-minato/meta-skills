---
name: meta-ml-experiment
description: >-
  Disposable meta-skill (delete after the harness is built): scaffolds a
  quick ML experiment repository with opinionated defaults — uv-compiled
  pinned requirements, root-level entry scripts, a hand-built PyTorch
  training loop on Hugging Face Accelerate — and writes a concise
  AGENTS.md depositing the outcome-first, let-it-crash coding rules. Use
  when the target must validate an idea fast with exactly reproducible
  re-runs and has little or no harness yet. Not for long-lived training
  codebases meant to survive upgrades, and not for migrating tooling that
  already works — existing choices stay.
---

# Quick ML Experiment Scaffold

This skill produces a flat, immediately runnable experiment repository
whose two deliverables are a validated idea and an environment that
re-runs it exactly. It expects an empty or nearly empty repository and a
user who can state the experiment's goal and hardware. The scaffold obeys
— and deposits — three standing rules: the only product is a trained
model, so readability beats abstraction (extract shared code only when
two places must stay logically consistent, never because lines repeat);
errors crash early and precisely (catch only known-expected data
problems); and every default below yields to an existing working choice.

## Workflow

1. Ask what the experiment must demonstrate, on what hardware it trains
   (this decides the torch backend), where data comes from, and which
   workflows exist (train, eval, preprocessing).
2. Framework: PyTorch — unless the user explicitly wants a frontier
   experiment with maximum freedom, which is the JAX-ecosystem branch:
   skip the torch-specific steps and fetch current JAX-stack docs
   instead.
3. Dependencies: hand-edited `requirements.in` plus `requirements.dev.in`
   (which starts with `-r requirements.in`), compiled by uv into
   `requirements.txt` for the training box and `requirements.dev.txt`
   for the dev machine. Read [pinned-deps.md](references/pinned-deps.md)
   when creating or updating them.
4. Layout: one entry script per workflow at the repository root
   (`train.py`, `eval.py`); a root `config.yaml` loaded through one
   Pydantic Settings class — `configs/` only when variants multiply, and
   only values an experiment may change are exposed; optional directories
   (`data/`, `outputs/`, `scripts/`, `tests/`, `notebooks/`, `docs/`)
   created on need, docs as plain files under `docs/`. Generate
   `.gitignore` (caches, virtualenv, `data/`, `outputs/`; the compiled
   `requirements*.txt` stay tracked). Read
   [shared-module.md](references/shared-module.md) when two entry
   scripts need the same code.
5. Training loop: when the experiment trains a PyTorch model, copy
   [train-loop-accelerate.md](assets/train-loop-accelerate.md) into
   `train.py` — fetch the current Accelerate API from its docs first,
   then rework every line against the real model and data.
6. Commands: copy [justfile.md](assets/justfile.md) and rework the
   recipes so a stranger can run `just setup && just train`.
7. Checks: Ruff as both linter and formatter; pytest only where a custom
   component has a contract worth protecting, anything expensive behind
   the manual-only `slow` marker; Gitleaks for secret scanning. Generate
   `.pre-commit-config.yaml` from exactly the hooks chosen here, with
   revs fetched fresh from each hook's repository — never copy a canned
   config. Add pre-commit to `requirements.dev.in`. No type checker,
   even when a hook template offers one.
8. Containers only on request: read
   [containers.md](references/containers.md) when the user asks for a
   containerized dev environment or server training; it guides copying
   [devcontainer.md](assets/devcontainer.md) or
   [docker-training.md](assets/docker-training.md).
9. Deposit: copy [agents-md-experiment.md](assets/agents-md-experiment.md)
   to the project's `AGENTS.md` and rework every section — this file is
   what future agents keep after this skill is deleted.

Done when: a fresh clone runs `just setup && just train` from committed
files alone, both compiled requirements files are committed, pre-commit
passes, and AGENTS.md states the code, data, and reproducibility rules.

## Gotchas

- The compiled `requirements*.txt` are the reproducibility artifact:
  commit them and never edit them by hand — change the `.in` file and
  recompile, or the recorded environment silently diverges from the real
  one.
- The training box installs `requirements.txt`; the dev machine installs
  `requirements.dev.txt` — keep both paths present in the justfile.
- Never wire `slow` tests, training smoke tests, or anything GPU-bound
  into pre-commit or CI.
- A placeholder left in a deployed asset is an unmade decision — rework
  every line or delete the file.
- Config is not module assembly: expose values experiments change, never
  class paths to instantiate.
