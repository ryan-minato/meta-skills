---
name: meta-ds-project
description: >-
  Disposable meta-skill (delete after the harness is built): scaffolds an
  opinionated, reproducible Python data-science project and its agent harness.
  Use when creating or hardening an empty or early repository that ingests
  datasets; validates, cleans, transforms, joins, or aggregates data; performs
  reproducible exploratory or production analysis; or publishes data products
  across local, S3, or Hugging Face storage. Not for notebook-only exploration,
  mature migrations, or model training; preserves working choices.
compatibility: Requires uv and Python 3.11+ for the bundled validator.
---

# Reproducible Data-Science Project

Build a Python data-science repository whose inputs are immutable, whose
production work runs from `src/`, and whose lockfile, configuration, source
identities, model revisions, and provenance make every product reproducible.
Keep existing working choices in an early repository; this is a scaffold, not
a migration mandate.

## Workflow

1. Inventory the project before writing: goal, package name, sources,
   products, input and output backends, data scale and media, report format,
   model use, and any working tools already present.
2. Initialize an absent package with `uv init --package`; keep an existing
   working `pyproject.toml`. Commit `uv.lock`. Put reusable logic in
   `src/<package>/`, thin launch modules in `src/<package>/workflows/`,
   source acquisition code in `src/<package>/sources/`, exploratory work in
   `notebooks/`, focused tests in `tests/`, and the paired report in
   `report/`.
3. Copy and rework every base asset; replace every `__UPPER_CASE__`
   placeholder and delete inapplicable rows:
   - [agents-md.md](assets/base/agents-md.md) to `AGENTS.md`
   - [architecture-md.md](assets/base/architecture-md.md) to
     `ARCHITECTURE.md`
   - [knowledge-project.md](assets/base/knowledge-project.md) to
     `.agents/knowledge/PROJECT.md`
   - [knowledge-data.md](assets/base/knowledge-data.md) to
     `.agents/knowledge/DATA.md`
   - [knowledge-references.md](assets/base/knowledge-references.md) to
     `.agents/knowledge/REFERENCES.md`
   - [justfile.md](assets/base/justfile.md) to `justfile`
   - merge [pyproject-tool-config.md](assets/base/pyproject-tool-config.md)
     into `pyproject.toml`
   - [settings.py](assets/base/settings.py) to
     `src/<package>/settings.py`
   - use [workflow-entry.py](assets/base/workflow-entry.py) for each real
     workflow entry
   - [project.toml](assets/base/project.toml) to `config/project.toml`
   - [env-example](assets/base/env-example) to `.env.example`
   - [editorconfig](assets/base/editorconfig) to `.editorconfig`
   - merge [gitignore](assets/base/gitignore) into `.gitignore`
   - [report.md](assets/base/report.md) to `report/report.md`
4. Select branches per source and product; mixed backends are valid:
   - Read [storage-local.md](references/storage-local.md) when any source or
     product is local.
   - Read [storage-s3.md](references/storage-s3.md) when any source or
     product uses S3.
   - Read
     [storage-huggingface.md](references/storage-huggingface.md) when any
     source, product, or model uses Hugging Face Hub.
   - Read
     [compute-structured.md](references/compute-structured.md) for
     structured or tabular data.
   - Read
     [compute-multimedia.md](references/compute-multimedia.md) for image,
     audio, video, or other multimedia data.
   - Read [model-inference.md](references/model-inference.md) when the
     pipeline loads a model.
   - Read
     [model-reimplementation.md](references/model-reimplementation.md)
     only when a model comes from an unstable experimental repository.
5. Before recording or updating a documentation URL, first check whether a
   configured documentation MCP exposes the component's official docs. If not,
   test the official `llms.txt` endpoint and prefer it when available; use
   regular official docs only as the fallback. Record the MCP server/tool or
   selected URL in `REFERENCES.md`. Use `llms-full.txt` only for scoped
   retrieval, never as a file to load wholesale.
6. Model configuration per source and product, not with one global storage
   switch. Keep adjustable non-secrets in `config/project.toml`; load TOML
   plus environment overrides with Pydantic Settings. Put credentials only
   in ignored `.env`; track only safe names and examples in `.env.example`.
7. Make every workflow observable with Loguru. Bind run, workflow, and step
   context; log identities, counts, timing, and failure state at useful
   levels. Never log credentials, full environments, PII, or raw records.
   Follow the current Loguru guidance for process-safe aggregation.
8. Generate `.pre-commit-config.yaml` from current upstream documentation,
   pin every hook revision, and install it through `just setup`. Use Ruff
   for lint and format, pytest for fast targeted tests, and Gitleaks for
   automated secret detection. Add no type checker and no coverage target.
9. Test only custom reusable logic whose mistakes would corrupt a result:
   transformations, invariants, boundary/error cases, and reimplemented
   model behavior. Do not test notebooks, declarative configuration,
   third-party libraries, or trivial workflow glue. Keep large-data, GPU,
   and model-equivalence tests manual under `slow`.
10. Deposit the Git rules in `AGENTS.md`: atomic commits, direct review of
    small staged diffs, programmatic sensitivity scanning with a recorded
    result for larger diffs, full checks before push, and no hook bypass. Try
    uncertain ideas in disposable worktrees; compare them with the same
    checks, remove them after the decision, then implement the selected
    approach on the formal branch in the canonical worktree.
11. Run
    [validate_scaffold.py](scripts/validate_scaffold.py) with
    `uv run scripts/validate_scaffold.py --project-root <target>`. Fix every
    issue, run the target's `just check`, inspect the generated harness with
    the user, and repeat until clean.

Done when: all selected storage, compute, and model branches are represented
without unused branch material; local source data cannot be overwritten by
the pipeline; every product carries provenance; all placeholders and links
are resolved; fast checks pass; and the user approves the scaffold.

## Invariants

- Local `data/` contains original inputs only, directly under
  `data/<source>/`.
- Only download workflows may write local source data. They download to a
  temporary sibling, verify identity, atomically publish a new path, and
  refuse overwrite. New upstream versions get new paths.
- Production steps read sources or earlier products and write only their
  own product locations. Local final products live under `output/final/`;
  local provenance lives under `output/_provenance/`.
- A run records source identities, resolved non-secret configuration, Git
  commit, `uv.lock` digest, model revision, random seeds, step state, and
  timing.
- Data-science projects may consume models; training, finetuning, optimizers,
  training loaders, and checkpoint management belong in another project.
- DVC, MLflow, LakeFS, containers, CI, and external orchestrators are
  opt-in, never scaffold defaults.

## Gotchas

- A branch name such as `main` or `latest` is not an immutable data or model
  identity. Record a revision, version ID, ETag plus checksum, or equivalent.
- A passing secret scanner does not prove a diff is free of PII. Review small
  staged diffs directly; route larger diffs through an appropriate programmatic
  scan and record its result. If sensitive content reached history, stop and
  report it rather than hiding it in a later commit.
- Do not copy a template unchanged. A remaining placeholder is an unmade
  project decision.
