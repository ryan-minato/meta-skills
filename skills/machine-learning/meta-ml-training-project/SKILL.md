---
name: meta-ml-training-project
description: >-
  Disposable meta-skill (delete after the harness is built): scaffolds a
  maintainable model-training project with opinionated defaults — uv plus
  pyproject.toml with hardware-matched torch wheel indexes, Hydra
  configs, a raw/interim/processed data split, a hand-built training loop
  on Hugging Face Accelerate — and writes a directory-map AGENTS.md plus
  a knowledge base depositing the outcome-first, let-it-crash coding
  rules. Use when the target is a train/eval codebase meant to be edited
  and upgraded over months. Not for one-shot idea-validation experiments,
  and not for migrating tooling that already works — existing choices
  stay.
---

# Maintainable Training Project Scaffold

This skill produces a train/eval codebase built to survive framework
upgrades and repeated edits. The product is still only a trained model,
so structure serves change-safety, never ceremony. It expects an empty or
early repository and a user who can state the training goal, hardware,
and data sources. The scaffold obeys — and deposits — three standing
rules: readability beats abstraction (extract shared code only when two
places must stay logically consistent, never because lines repeat);
errors crash early and precisely (catch only known-expected data
problems); and every default below yields to an existing working choice.

## Workflow

1. Ask what gets trained and evaluated, on what hardware (this decides
   the torch wheel index), where data comes from and roughly how much,
   and whether training runs beyond the local machine.
2. Framework: PyTorch — unless the user explicitly wants a frontier
   experiment with maximum freedom, which is the JAX-ecosystem branch:
   skip the torch-specific steps and fetch current JAX-stack docs
   instead.
3. Initialize a uv-managed `pyproject.toml` (dev tools in the dev
   dependency group; `uv.lock` committed). Read
   [uv-hardware-deps.md](references/uv-hardware-deps.md) when adding
   torch or any hardware-bound dependency — plain `uv add torch` fetches
   the wrong wheel on CUDA/ROCm machines.
4. Copy the tool tables from
   [pyproject-tool-config.toml](assets/pyproject-tool-config.toml) into
   `pyproject.toml` and rework them against the project: drop the
   per-file-ignores for directories it does not have yet, and verify the
   rule codes against the current Ruff docs.
5. Layout: a package named after the repository at the root (no `src/`
   layout); one entry script per workflow at the root (`train.py`,
   `eval.py`); `configs/` for the Hydra tree; `data/raw/` (immutable
   inputs), `data/interim/`, `data/processed/`; `outputs/` for
   everything produced; `scripts/`, `tests/`, `notebooks/`, `docs/` on
   need. Generate `.gitignore` (caches, `.venv/`, `data/`, `outputs/`;
   `uv.lock` stays tracked) and a minimal `.editorconfig`.
6. Configuration with Hydra: read
   [hydra-config.md](references/hydra-config.md) when creating or
   restructuring `configs/` — expose anticipatorily what planned
   experiments will vary, but values only, never class paths.
7. Training loop: when no working loop exists, copy
   [the Accelerate loop skeleton](assets/train.py) into `train.py` —
   fetch the current Accelerate API from its docs first, then rework
   every line against the real model and data, confirming the
   `@hydra.main` wiring against the current Hydra docs.
8. Commands and checks: copy [the justfile skeleton](assets/justfile) and
   rework it; Ruff as linter and formatter; pytest guarding custom
   components' contracts only, expensive tests behind the manual-only
   `slow` marker; Gitleaks for secrets. Generate `.pre-commit-config.yaml`
   from exactly the hooks chosen here, revs fetched fresh — never copy a
   canned config. No type checker.
9. Containers only on request: read
   [containers.md](references/containers.md) when the user asks for a
   containerized dev environment or server training; it guides copying
   [devcontainer.json](assets/devcontainer.json) or the
   [Dockerfile](assets/Dockerfile) and [compose.yaml](assets/compose.yaml).
10. Deposit: copy
    [agents-md-training-project.md](assets/agents-md-training-project.md)
    to the project's `AGENTS.md`, rework the directory map against
    reality, and create the knowledge-base files its when-to-read table
    names — with real initial content, not stubs.

Done when: a fresh clone on the stated hardware runs
`just setup && just train`, `data/raw/` is documented as immutable, every
AGENTS.md link resolves including the knowledge-base table, and
pre-commit passes with no slow test wired in.

## Gotchas

- Plain `uv add torch` silently installs the default wheel — on a
  CUDA/ROCm box that means no GPU; configure the index routing first.
- `data/raw/` is append-only ground truth: transformations write to
  `interim/` or `processed/`, never back.
- Hydra relocates each run's output directory by default — pin the
  behavior deliberately in the config and resolve data paths from the
  project root, or path handling breaks the first time someone runs from
  another directory.
- Anticipatory config exposure is not module assembly: expose values,
  never class paths to instantiate.
- Never wire `slow` tests or training smoke tests into pre-commit or CI;
  `just test-slow` is their only entry point.
- A placeholder left in a deployed asset is an unmade decision — rework
  every line or delete the file.
