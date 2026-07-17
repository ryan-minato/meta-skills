---
name: meta-ds-analysis-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  data-analysis project to authoritative documentation entry points —
  numerics and statistics (NumPy, SciPy, statsmodels), dataframes and
  SQL (pandas, Polars, DuckDB, Ibis), columnar and array storage
  (Arrow, Zarr, HDF5), multidimensional data (xarray), graph analysis,
  visualization (Matplotlib through Panel and Streamlit), data quality
  (Pandera, Great Expectations), and notebooks and publishing (Jupyter,
  Quarto) — plus the discovery procedure (llms.txt probing, PyPI
  metadata, official org repos) for tools not listed. Use when a
  harness build must record where the docs live for a project that
  analyzes data interactively or in scripts. Not for choosing between
  tools or recommending one, and not for distributed engines,
  orchestration, or model training.
---

# Data Analysis Documentation Map

This skill produces the documentation entry points a harness build
records for a data-analysis project: arrays and dataframes, statistics,
storage formats, visualization, data quality, and notebooks. It expects
a harness build in progress and access to the target's dependency
manifests. Per-tool content is one line plus a URL — install commands
and API details are always fetched from the recorded entry point, never
recalled from memory — and nothing here is a recommendation: when the
target lacks a tool for a need, record the option list with URLs and
leave the choice to the user.

## Workflow

1. Detect the analysis stack: dependency manifests and imports
   (`numpy`, `scipy`, `pandas`, `polars`, `duckdb`, `ibis`, `pyarrow`,
   `xarray`, `matplotlib`, `pandera`, `pydantic`), notebooks
   (`*.ipynb`), Quarto projects (`_quarto.yml`), and data files
   (Parquet, HDF5, Zarr, NetCDF).
2. Read [numerics-and-stats.md](references/numerics-and-stats.md) when
   the target computes on arrays or runs statistical models.
3. Read [dataframes-and-sql.md](references/dataframes-and-sql.md) when
   the target manipulates tables with dataframes or embedded SQL.
4. Read [storage-and-formats.md](references/storage-and-formats.md)
   when the target reads or writes columnar, chunked, or hierarchical
   data files.
5. Read [multidim-data.md](references/multidim-data.md) when the target
   works with labeled N-dimensional arrays (climate, imaging, sensor
   data).
6. Read [graph-analysis.md](references/graph-analysis.md) when the
   target analyzes networks without training graph models.
7. Read [visualization.md](references/visualization.md) when the target
   plots, builds dashboards, or ships small data apps.
8. Read [data-quality.md](references/data-quality.md) when the target
   validates schemas or monitors data quality.
9. Read
   [notebooks-and-publishing.md](references/notebooks-and-publishing.md)
   when the target uses notebooks or publishes computational documents.
10. For every entry point about to be recorded, probe
    `<docs-root>/llms.txt` (then `llms-full.txt`) and prefer the
    plain-text index when present.
11. For tools the tables miss, or any URL that no longer resolves,
    follow [doc-discovery.md](references/doc-discovery.md).
12. Record each detected tool — name, one-line role, documentation
    entry point, and its llms.txt when present — wherever the harness
    keeps conventions.

Done when: every analysis library the target actually uses has a
recorded, live documentation entry point, and nothing recorded ranks or
recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: dataframe and plotting library
  selection is the user's decision.
- The same tool may appear in another domain skill's tables (xarray,
  Arrow, and fsspec also serve HPC I/O); record it once per harness,
  not once per skill.
