---
name: meta-ml-tabular-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  tabular or classic machine-learning project to authoritative
  documentation entry points — traditional ML and gradient boosting
  (scikit-learn, XGBoost, LightGBM, CatBoost, cuML), interpretability
  (SHAP, LIME, InterpretML), and AutoML and hyperparameter optimization
  (Optuna, AutoGluon, FLAML, Ax/BoTorch). Use when a harness build must
  record where the docs live for a project that models tabular data or
  tunes model hyperparameters. Not for choosing between tools or
  recommending one, and not for deep learning frameworks, time-series
  forecasting, or general data analysis.
---

# Tabular ML & AutoML Documentation Map

This skill produces the documentation entry points a harness build
records for a project doing traditional machine learning on tabular
data or hyperparameter optimization. It expects a harness build in
progress and access to the target's dependency manifests. Per-tool
content is one line plus a URL — install commands and API details are
always fetched from the recorded entry point, never recalled from
memory — and nothing here is a recommendation: when the target lacks a
tool for a need, record the option list with URLs and leave the choice
to the user.

## Workflow

1. Detect the modeling stack: dependency manifests and imports
   (`sklearn`, `xgboost`, `lightgbm`, `catboost`, `cuml`, `shap`,
   `optuna`, `autogluon`, `flaml`), model artifacts, and tuning-study
   storage.
2. Read [tabular-ml.md](references/tabular-ml.md) when the target
   trains classic models or boosted trees, or explains model
   predictions.
3. Read [automl-and-tuning.md](references/automl-and-tuning.md) when
   the target automates model selection or tunes hyperparameters.
4. For every entry point about to be recorded, prefer an agent-oriented
   rendition: a page's `.md` source, then `<docs-root>/llms.txt` (a
   compact index). Fall back to `llms-full.txt` only when neither
   exists, and never read it whole — it is the whole site as one
   file; search it programmatically.
5. Record each detected tool the tables cover — name, one-line role,
   documentation entry point, and its llms.txt when present — wherever
   the harness keeps conventions.

Done when: every tabular-ML and tuning library the target actually uses
has a recorded, live documentation entry point, and nothing recorded
ranks or recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: model-family and tuner selection
  is the user's decision.
- Ray Tune and KerasTuner belong to their ecosystems' own documentation
  maps — do not duplicate their entries from here.
- The same tool may appear in another domain skill's tables
  (scikit-learn, SHAP, PyOD); record it once per harness, not once per
  skill.
- Tools this skill does not list are out of scope — leave finding their
  docs to the agent; it is not this skill's job.
