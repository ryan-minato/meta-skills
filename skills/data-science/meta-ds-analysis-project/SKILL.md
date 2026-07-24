---
name: meta-ds-analysis-project
description: >-
  Disposable meta-skill (delete after the harness is built): builds or
  incrementally extends a reproducible Python batch data-product project.
  Use when a project must clean, standardize, integrate, validate, and publish
  data products from immutable inputs. Not for platform rewrites, model
  training, continuous operations, or notebook-only one-off exploration.
compatibility: Requires uv and Python 3.11+ for the bundled validator.
---

# Reproducible Data-Product Project

Build or extend a Python batch data-product repository whose inputs are
immutable and whose production work runs from `src/`. Deliver the first
working product pipeline as part of the harness: profile and contract inputs,
clean and standardize records, integrate sources when needed, publish derived
products, and persist quality results and provenance. Lockfiles,
configuration, source identities, model revisions, and lineage must make every
product reproducible. Preserve effective existing choices; this is incremental
delivery, not a migration mandate.

## Workflow

1. Inventory before writing: the goal and consumers, package name, sources,
   source contracts and sensitivity, intended products, cleaning and
   standardization rules, integration keys, quality policy, input and output
   backends, data scale and media, report format, model use, and working tools
   already present. For an existing repository, retain working conventions and
   identify the smallest missing path to its first governed data product.
2. Initialize an absent package with `uv init --package`; keep an existing
   working `pyproject.toml`. Commit `uv.lock`. Put reusable logic in
   `src/<package>/`, thin launch modules in `src/<package>/workflows/`,
   source acquisition code in `src/<package>/sources/`, reusable contracts,
   quality checks, and transformations in `src/<package>/processing/`, thin
   stage entries in `src/<package>/workflows/`, exploratory work in
   `notebooks/`, focused tests in `tests/`, and the paired product report in
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
4. Build the first product as an ordered, observable batch chain. A source is
   profiled against its contract before processing; clean stages normalize,
   deduplicate, and reject invalid records; integration stages join only on
   documented keys and cardinality; final stages publish a versioned product.
   Keep intermediate, quarantine, and final products distinct. Every product
   declares its stage, inputs, schema version, owner workflow, consumers, and
   retention. Multi-source products include an integration stage; a
   single-source product may omit it.
5. Apply the default quality policy. Critical schema, primary-key, critical
   completeness, and documented integration-invariant failures block
   publication. When a row-level problem is identifiable and safe to isolate,
   write rejected rows to the declared quarantine product with a reason and
   counts; never silently drop rows. Record profile findings, accepted and
   rejected counts, rule results, and the publication decision in provenance.
   Read [data-product-workflow.md](references/data-product-workflow.md) before
   implementing or extending a structured data-product chain.
6. Select branches per source and product; mixed backends are valid:
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
7. Before recording or updating a documentation URL, first check whether a
   configured documentation MCP exposes the component's official docs. If not,
   test the official `llms.txt` endpoint and prefer it when available; use
   regular official docs only as the fallback. Record the MCP server/tool or
   selected URL in `REFERENCES.md`. Use `llms-full.txt` only for scoped
   retrieval, never as a file to load wholesale.
8. Model configuration per source and product, not with one global storage
   switch. Keep adjustable non-secrets in `config/project.toml`; load TOML
   plus environment overrides with Pydantic Settings. Put credentials only
   in ignored `.env`; track only safe names and examples in `.env.example`.
9. Make every workflow observable with Loguru. Bind run, workflow, step, and
   product context; log identities, accepted/rejected counts, quality decision,
   timing, and failure state at useful levels. Never log credentials, full
   environments, PII, or raw records.
   Follow the current Loguru guidance for process-safe aggregation.
10. Generate `.pre-commit-config.yaml` from current upstream documentation,
   pin every hook revision, and install it through `just setup`. Use Ruff
   for lint and format, pytest for fast targeted tests, and Gitleaks for
   automated secret detection. Add no type checker and no coverage target.
11. Test only custom reusable logic whose mistakes would corrupt a result:
   parsing, transformations, quality rules, quarantine decisions, joins,
   aggregations, schema and integration invariants, boundary/error cases, and
   reimplemented model behavior. Do not test notebooks, declarative
   configuration, third-party libraries, or trivial workflow glue. Keep
   large-data, GPU, and model-equivalence tests manual under `slow`.
12. Deposit the Git rules in `AGENTS.md`: atomic commits, direct review of
    small staged diffs, programmatic sensitivity scanning with a recorded
    result for larger diffs, full checks before push, and no hook bypass. Try
    uncertain ideas in disposable worktrees; compare them with the same
    checks, remove them after the decision, then implement the selected
    approach on the formal branch in the canonical worktree.
13. Run
    [validate_scaffold.py](scripts/validate_scaffold.py) with
    `uv run scripts/validate_scaffold.py --project-root <target>`. Fix every
    issue, run the target's `just check`, inspect the generated harness with
    the user, and repeat until clean.

Done when: the first product chain profiles, validates, cleans, and publishes
its configured inputs; it integrates sources when applicable; critical quality
failures prevent publication; row-level rejects are quarantined and counted;
all selected storage, compute, and model branches are represented without
unused material; local source data cannot be overwritten; every product carries
lineage and provenance; all placeholders and links are resolved; fast checks
pass; and the user approves the result.

## Invariants

- Local `data/` contains original inputs only, directly under
  `data/<source>/`.
- Only download workflows may write local source data. They download to a
  temporary sibling, verify identity, atomically publish a new path, and
  refuse overwrite. New upstream versions get new paths.
- Production steps read sources or declared earlier products and write only
  their own product locations. Local intermediate products live under
  `output/<stage>/`, local final products under `output/final/`, quarantined
  rows under `output/quarantine/`, and provenance under `output/_provenance/`.
- A product's provenance records its declared inputs and schema version,
  source identities, resolved non-secret configuration, transformation and
  integration decisions, profile and quality results, accepted/rejected counts,
  Git commit, `uv.lock` digest, model revision, random seeds, step state, and
  timing.
- Analysis projects consume models; training, finetuning, optimizers,
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
