---
name: meta-ml-timeseries-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  time-series project to authoritative documentation entry points —
  forecasting and analysis libraries (statsmodels, Nixtla's
  StatsForecast/MLForecast/NeuralForecast, Prophet, sktime, tsfresh)
  and change-point and anomaly detection (ruptures, PyOD) — plus the
  discovery procedure (llms.txt probing, PyPI metadata, official org
  repos) for tools not listed. Use when a harness build must record
  where the docs live for a project that forecasts, decomposes, or
  detects anomalies in time series. Not for choosing between tools or
  recommending one, and not for general tabular ML or statistical
  analysis outside time series.
---

# Time Series Documentation Map

This skill produces the documentation entry points a harness build
records for a time-series project. It expects a harness build in
progress and access to the target's dependency manifests. Per-tool
content is one line plus a URL — install commands and API details are
always fetched from the recorded entry point, never recalled from
memory — and nothing here is a recommendation: when the target lacks a
tool for a need, record the option list with URLs and leave the choice
to the user.

## Workflow

1. Detect the time-series stack: dependency manifests and imports
   (`statsmodels`, `statsforecast`, `mlforecast`, `neuralforecast`,
   `prophet`, `sktime`, `tsfresh`, `ruptures`, `pyod`), datetime-indexed
   data pipelines, and forecasting configs.
2. Read [time-series.md](references/time-series.md) for the
   forecasting, feature-extraction, and anomaly-detection libraries in
   play.
3. For every entry point about to be recorded, probe
   `<docs-root>/llms.txt` (then `llms-full.txt`) and prefer the
   plain-text index when present.
4. For tools the tables miss, or any URL that no longer resolves, follow
   [doc-discovery.md](references/doc-discovery.md).
5. Record each detected tool — name, one-line role, documentation entry
   point, and its llms.txt when present — wherever the harness keeps
   conventions.

Done when: every time-series library the target actually uses has a
recorded, live documentation entry point, and nothing recorded ranks or
recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: forecaster selection is the
  user's decision.
- pandas's own time-series interface documents inside pandas — a
  pandas-only target needs the pandas entry point, not a forecasting
  library's.
- The same tool may appear in another domain skill's tables
  (statsmodels, PyOD); record it once per harness, not once per skill.
