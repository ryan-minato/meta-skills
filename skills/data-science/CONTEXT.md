# data-science — Catalog Context

Read this before authoring or reviewing anything in
`skills/data-science/`. Repository-wide rules live in
[meta-skill-contract.md](../../.agents/knowledge/meta-skill-contract.md);
this file adds only what is specific to `data-science`. Neither this
file nor the catalog READMEs ship to targets — installers copy skill
directories only.

## Goal

`data-science` holds information skills for data-analysis and
scientific-computing target projects: authoritative documentation entry
points for the libraries, engines, and tools such a project uses or is
likely to need, plus the discovery procedure for anything not listed. A
harness-building agent detects which domains the target belongs to
(from manifests, imports, and configs), loads only the matching skills,
and records where the docs live. It installs per project, on top of
`core`, and only when the target analyzes data, runs data pipelines, or
does numerical and scientific computing — it is not part of the default
install. Recommendations and guidance are future, separate skills in
this catalog; the skills here only inform.

## Constraints On What May Enter

- **DS-only usefulness.** A skill belongs here only if it is useless to
  a project that does no data analysis or scientific computing.
  Anything useful regardless of stack belongs in `core`; model training
  and ML-specific tooling belong in `machine-learning`.
- **Disposable only.** The marker admission test applies unchanged: if a
  skill should not carry it, it does not belong in this repository.
- **Information, not recommendation.** Unlike `python`, which records
  trusted defaults, no skill in this catalog may record a default, a
  ranking, or a "prefer X". Skills report what exists and where its docs
  live; every choice between tools stays with the user. A future
  recommendation skill that breaks this rule must say so in its own
  description, not hide inside a docs skill.
- **One domain per skill.** A skill's boundary is a project domain with
  a detectable trigger (dependencies, imports, config files), so an
  agent loads exactly the domains the target belongs to. Finer splits
  live behind per-reference load conditions; a skill that mixes
  unrelated domains gets split, not grown.
- **Doc-root fidelity.** Only stable entry points: a docs root, an org
  root, or a repository root. Volatile facts (versions, install
  commands, API pages, deep links) always defer to a fetch from the
  entry point. A dead or moved URL is a bug, fixed in the same change
  that finds it.
- **Registry completeness.** Every URL any reference cites appears in
  this file's Upstream Registry, in the section mirroring its reference
  table. A URL in a skill but not the registry is a bug.
- **Sibling-catalog overlap is intentional.** Tools shared with
  `machine-learning` (NumPy, scikit-learn, statsmodels, Dask, CUDA
  toolchains, …) are recorded independently in both catalogs, because
  skills are self-contained and never reference the sibling catalog.

## Authoring

Start from the authoring skill's template
(`.agents/skills/meta-skill-authoring/assets/skill-template.md`), which
ships with the marker pre-filled. The marker's exact bytes and YAML form
are defined in the contract; copy them from there, never from rendered
documentation. Skill names use the `meta-ds-<domain>-docs` pattern — the
`-docs` suffix reserves the domain name for future scaffolding or
recommendation skills. Every skill carries `references/doc-discovery.md`,
byte-identical across the catalog (and across `machine-learning`); the
canonical copy is
`skills/machine-learning/meta-ml-frameworks-docs/references/doc-discovery.md`,
and any change to it is copied to every sibling in the same change
(`sha256sum` across the copies is the review check).

## References

- llms.txt specification (agent-preferred plain-text doc indexes) —
  <https://llmstxt.org/>
- PyPI JSON API (package metadata → project homepage and doc URLs) —
  <https://docs.pypi.org/api/json/>
- Agent Skills specification — reachable through the `agentskills` MCP
  server.

## Upstream Registry

Every doc URL the catalog's skills cite — a maintainer snapshot, last
verified live 2026-07-17. The URL is authoritative: when this table and
a tool's docs disagree, the docs win and this file updates in the same
change. Sites that publish an `llms.txt` plain-text index
(agent-preferred; probe `<docs-root>/llms.txt`, then `llms-full.txt`)
are marked; re-probe the others when refreshing this table. PyPI
packages install with `pip install <package>` (or the project's own
manager); non-PyPI tools carry an install pointer in their skill's
reference table, with details always fetched from the doc URL.

Sections mirror the catalog's skills and their reference tables, in
order; each skill's rows land in the same change that adds the skill.

### meta-ds-analysis-docs

#### numerics-and-stats.md

| Tool | Docs |
|---|---|
| NumPy | <https://numpy.org/doc/> |
| SciPy | <https://docs.scipy.org/doc/scipy/> |
| Numba | <https://numba.readthedocs.io/> |
| CuPy | <https://docs.cupy.dev/> |
| statsmodels | <https://www.statsmodels.org/> |
| scikit-learn | <https://scikit-learn.org/> |
| PyMC | <https://www.pymc.io/> |
| ArviZ | <https://python.arviz.org/> |
| lifelines | <https://lifelines.readthedocs.io/> |

#### dataframes-and-sql.md

| Tool | Docs |
|---|---|
| pandas | <https://pandas.pydata.org/docs/> |
| Polars | <https://docs.pola.rs/> |
| DuckDB | <https://duckdb.org/docs/> — llms.txt: <https://duckdb.org/llms.txt> |
| Ibis | <https://ibis-project.org/> |

#### storage-and-formats.md

| Tool | Docs |
|---|---|
| Apache Arrow | <https://arrow.apache.org/docs/> |
| Zarr | <https://zarr.readthedocs.io/> |
| h5py | <https://docs.h5py.org/> |
| HDF5 | <https://support.hdfgroup.org/documentation/> |
| fsspec | <https://filesystem-spec.readthedocs.io/> |

#### multidim-data.md

| Tool | Docs |
|---|---|
| xarray | <https://docs.xarray.dev/> — llms.txt: <https://docs.xarray.dev/llms.txt> |
| rioxarray | <https://corteva.github.io/rioxarray/> |
| Rasterio | <https://rasterio.readthedocs.io/> |
| netCDF4 | <https://unidata.github.io/netcdf4-python/> |

#### graph-analysis.md

| Tool | Docs |
|---|---|
| NetworkX | <https://networkx.org/> |
| igraph | <https://python.igraph.org/> |
| NVIDIA RAPIDS cuGraph | <https://docs.rapids.ai/api/cugraph/stable/> |
| GraphFrames | <https://graphframes.io/> — llms.txt: <https://graphframes.io/llms.txt> |

#### visualization.md

| Tool | Docs |
|---|---|
| Matplotlib | <https://matplotlib.org/> |
| Seaborn | <https://seaborn.pydata.org/> |
| Plotly | <https://plotly.com/python/> — llms.txt: <https://plotly.com/llms.txt> |
| Altair | <https://altair-viz.github.io/> |
| HoloViews | <https://holoviews.org/> |
| hvPlot | <https://hvplot.holoviz.org/> |
| Datashader | <https://datashader.org/> |
| Panel | <https://panel.holoviz.org/> |
| Streamlit | <https://docs.streamlit.io/> — llms.txt: <https://docs.streamlit.io/llms.txt> |
| Plotly Dash | <https://dash.plotly.com/> |
| Gradio | <https://gradio.app/docs> — llms.txt: <https://gradio.app/llms.txt> |

#### data-quality.md

| Tool | Docs |
|---|---|
| Pandera | <https://pandera.readthedocs.io/> |
| Great Expectations | <https://docs.greatexpectations.io/> |
| Evidently | <https://docs.evidentlyai.com/> — llms.txt: <https://docs.evidentlyai.com/llms.txt> |
| Cleanlab | <https://docs.cleanlab.ai/> |
| Pydantic | <https://pydantic.dev/docs/> — llms.txt: <https://pydantic.dev/llms.txt> |

#### notebooks-and-publishing.md

| Tool | Docs |
|---|---|
| IPython | <https://ipython.readthedocs.io/> |
| Jupyter | <https://docs.jupyter.org/> |
| JupyterLab | <https://jupyterlab.readthedocs.io/> |
| Jupyter Server | <https://jupyter-server.readthedocs.io/> |
| Quarto | <https://quarto.org/> — llms.txt: <https://quarto.org/llms.txt> |

### meta-ds-scale-docs

#### rapids.md

| Tool | Docs |
|---|---|
| RAPIDS | <https://docs.rapids.ai/> |
| cuDF | <https://docs.rapids.ai/api/cudf/stable/> |
| cuML | <https://docs.rapids.ai/api/cuml/stable/> |
| cuGraph | <https://docs.rapids.ai/api/cugraph/stable/> |
| cuSpatial | <https://docs.rapids.ai/api/cuspatial/stable/> |
| Dask-CUDA | <https://docs.rapids.ai/api/dask-cuda/stable/> |
| RMM | <https://docs.rapids.ai/api/rmm/stable/> |
| CuPy | <https://docs.cupy.dev/> |

#### dask.md

| Tool | Docs |
|---|---|
| Dask | <https://docs.dask.org/> — llms.txt: <https://docs.dask.org/llms.txt> |
| Dask Distributed | <https://distributed.dask.org/> |
| Dask-ML | <https://ml.dask.org/> |

#### cluster-engines.md

| Tool | Docs |
|---|---|
| Apache Spark | <https://spark.apache.org/docs/latest/> — llms.txt: <https://spark.apache.org/docs/llms.txt> |
| PySpark | <https://spark.apache.org/docs/latest/api/python/> — llms.txt: <https://spark.apache.org/docs/llms.txt> |
| Apache Flink | <https://nightlies.apache.org/flink/flink-docs-stable/> |
| Trino | <https://trino.io/docs/current/> |
| Apache Sedona | <https://sedona.apache.org/> |
| GraphFrames | <https://graphframes.io/> — llms.txt: <https://graphframes.io/llms.txt> |
| Ray | <https://docs.ray.io/> — llms.txt: <https://docs.ray.io/llms.txt> |
