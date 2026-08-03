# machine-learning

[中文](README.zh.md)

Meta-skills for machine-learning target projects: harness scaffolds and
live-registry discovery, each carrying opinionated defaults declared in
its own description. Documentation entry points for ML domains live in
the published docs index, consumed on demand by `core`'s docs-map
skill. Install on top of `core`, per project, and only when the target
trains, finetunes, serves, or builds on ML models — this catalog is not
part of the default install.

These skills are **disposable**: once the harness is built and verified,
the `core` removal skill deletes them together with the rest.

```bash
claude plugin marketplace add ryan-minato/meta-skills   # once per machine
claude plugin install machine-learning@meta-skills --scope project
# or via the skills CLI (the catalog path scopes discovery):
npx skills add ryan-minato/meta-skills/skills/machine-learning
npx skills add ryan-minato/meta-skills/skills/machine-learning --skill <skill-name>
```

## Skills

| Skill | Description |
|---|---|
| [meta-ml-containers](meta-ml-containers/) | Scripts that list and filter the currently available NVIDIA NGC and Docker Hub GPU images and tags, plus a guide to each image family's characteristics and fit |
| [meta-ml-experiment](meta-ml-experiment/) | Scaffolds a quick ML experiment repository (opinionated defaults): uv-compiled pinned requirements, root-level entry scripts, Pydantic Settings config, justfile, Ruff/pytest/Gitleaks, an Accelerate training-loop template, and a concise AGENTS.md |
| [meta-ml-training-project](meta-ml-training-project/) | Scaffolds a maintainable train/eval project (opinionated defaults): uv + pyproject with hardware-matched torch indexes, Hydra configs, raw/interim/processed data split, an Accelerate training-loop template, and a directory-map AGENTS.md with a knowledge base |
