# data-science — Catalog Context

Read this before authoring or reviewing anything in
`skills/data-science/`. Repository-wide rules live in
[meta-skill-contract.md](../../.agents/knowledge/meta-skill-contract.md);
this file adds only what is specific to `data-science`. Neither this
file nor the catalog READMEs ship to targets — installers copy skill
directories only.

## Goal

`data-science` holds skills for data-analysis and scientific-computing
target projects. Domain-split `-docs` skills provide authoritative
documentation entry points; separate project skills scaffold opinionated
data-science repositories and declare their defaults in their descriptions. A
harness-building agent loads only the matching domains or project builder.
The catalog installs per project, on top of `core`, and only when the target
analyzes data, runs data pipelines, or does numerical and scientific
computing — it is not part of the default install.

## Constraints On What May Enter

- **DS-only usefulness.** A skill belongs here only if it is useless to
  a project that does no data analysis or scientific computing.
  Anything useful regardless of stack belongs in `core`; model training
  and ML-specific tooling belong in `machine-learning`.
- **Disposable only.** The marker admission test applies unchanged: if a
  skill should not carry it, it does not belong in this repository.
- **Docs inform; project skills may choose.** A `-docs` skill records what
  exists and where its docs live, never a default, ranking, or "prefer X".
  An opinionated scaffold or recommendation skill may choose defaults only
  when its description says so and its body preserves existing working
  choices.
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
documentation. Documentation skill names use the
`meta-ds-<domain>-docs` pattern; project builders use
`meta-ds-<domain>-project`. A documentation skill maps only the tools its
tables list; discovering docs for a package it does not cover is out of
scope — the agent reaches for a dedicated discovery skill on its own, so no
skill here carries or depends on that procedure.

## References

- llms.txt specification (agent-preferred plain-text doc indexes) —
  <https://llmstxt.org/>
- Agent Skills specification — reachable through the `agentskills` MCP
  server.

## Upstream Registry

Every doc URL the catalog's skills cite — a maintainer snapshot, last
verified live 2026-07-17. The URL is authoritative: when this table and
a tool's docs disagree, the docs win and this file updates in the same
change. Sites that publish an `llms.txt` plain-text index
(agent-preferred: fetch a page's `.md` source or the `llms.txt` index
rather than HTML; `llms-full.txt` is a whole-site dump to search
programmatically, never read whole) are marked; re-probe the others when
refreshing this table. PyPI
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

### meta-ds-pipelines-docs

#### orchestration.md

| Tool | Docs |
|---|---|
| Apache Airflow | <https://airflow.apache.org/docs/> |
| dbt | <https://docs.getdbt.com/> — llms.txt: <https://docs.getdbt.com/llms.txt> |
| Dagster | <https://docs.dagster.io/> — llms.txt: <https://docs.dagster.io/llms.txt> |
| Prefect | <https://docs.prefect.io/> — llms.txt: <https://docs.prefect.io/llms.txt> |

### meta-ds-geospatial-docs

#### geospatial.md

| Tool | Docs |
|---|---|
| GeoPandas | <https://geopandas.org/> |
| Shapely | <https://shapely.readthedocs.io/> |
| pyproj | <https://pyproj4.github.io/pyproj/> |
| GDAL | <https://gdal.org/> |
| Rasterio | <https://rasterio.readthedocs.io/> |
| rioxarray | <https://corteva.github.io/rioxarray/> |
| DuckDB Spatial | <https://duckdb.org/docs/> — llms.txt: <https://duckdb.org/llms.txt> |
| Apache Sedona | <https://sedona.apache.org/> |
| NVIDIA RAPIDS cuSpatial | <https://docs.rapids.ai/api/cuspatial/stable/> |

### meta-ds-numerics-docs

#### platforms.md

| Tool | Docs |
|---|---|
| SciPy | <https://docs.scipy.org/doc/scipy/> |
| SymPy | <https://docs.sympy.org/> |
| Julia | <https://docs.julialang.org/> |
| Julia SciML | <https://docs.sciml.ai/> |
| MATLAB | <https://www.mathworks.com/help/matlab/> |
| Wolfram Language | <https://reference.wolfram.com/language/> — llms.txt: <https://reference.wolfram.com/llms.txt> |

#### numerics-and-math-kernels.md

| Tool | Docs |
|---|---|
| NumPy | <https://numpy.org/doc/> |
| Numba | <https://numba.readthedocs.io/> |
| Cython | <https://cython.readthedocs.io/> |
| Eigen | <https://libeigen.gitlab.io/> |
| Armadillo | <https://arma.sourceforge.net/> |
| Boost.Math | <https://www.boost.org/doc/libs/release/libs/math/> |
| GNU Scientific Library | <https://www.gnu.org/software/gsl/> |
| OpenBLAS | <https://www.openblas.net/> |
| LAPACK | <https://www.netlib.org/lapack/> |
| ScaLAPACK | <https://www.netlib.org/scalapack/> |
| Intel oneMKL | <https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl.html> |
| FFTW | <https://www.fftw.org/> |
| SuiteSparse | <https://github.com/DrTimothyAldenDavis/SuiteSparse> |
| CUDA math libraries | <https://docs.nvidia.com/cuda/> — llms.txt: <https://docs.nvidia.com/cuda/llms.txt> |
| ROCm math libraries | <https://rocm.docs.amd.com/> |
| PETSc | <https://petsc.org/> |
| Trilinos | <https://trilinos.github.io/> |
| hypre | <https://hypre.readthedocs.io/> |
| SLEPc | <https://slepc.upv.es/> |
| MUMPS | <https://mumps-solver.org/> |
| SuperLU | <https://github.com/xiaoyeli/superlu> |
| ARPACK-NG | <https://github.com/opencollab/arpack-ng> |
| StaticArrays.jl | <https://juliaarrays.github.io/StaticArrays.jl/> |
| SpecialFunctions.jl | <https://specialfunctions.juliamath.org/> |

#### compilers-and-autodiff.md

| Tool | Docs |
|---|---|
| LLVM | <https://llvm.org/docs/> |
| MLIR | <https://mlir.llvm.org/> |
| JAX | <https://docs.jax.dev/> |
| Triton | <https://triton-lang.org/> |
| CUDA | <https://docs.nvidia.com/cuda/> — llms.txt: <https://docs.nvidia.com/cuda/llms.txt> |
| ROCm | <https://rocm.docs.amd.com/> |
| SYCL | <https://www.khronos.org/sycl/> |
| Kokkos | <https://kokkos.org/> |
| OpenMP | <https://www.openmp.org/> |
| CUDA.jl | <https://cuda.juliagpu.org/> |
| AMDGPU.jl | <https://amdgpu.juliagpu.org/> |
| KernelAbstractions.jl | <https://juliagpu.github.io/KernelAbstractions.jl/> |
| CasADi | <https://web.casadi.org/> |
| Enzyme | <https://enzyme.mit.edu/> |
| ForwardDiff.jl | <https://juliadiff.org/ForwardDiff.jl/> |
| Zygote.jl | <https://fluxml.ai/Zygote.jl/> |
| SciMLSensitivity.jl | <https://docs.sciml.ai/SciMLSensitivity/> |
| Diffrax | <https://docs.kidger.site/diffrax/> |
| torchdiffeq | <https://github.com/rtqichen/torchdiffeq> |

### meta-ds-simulation-docs

#### optimization-and-solvers.md

| Tool | Docs |
|---|---|
| SciPy | <https://docs.scipy.org/doc/scipy/> |
| NLopt | <https://nlopt.readthedocs.io/> |
| Ipopt | <https://coin-or.github.io/Ipopt/> |
| Ceres Solver | <http://ceres-solver.org/> |
| Optimization.jl | <https://docs.sciml.ai/Optimization/> |
| CVXPY | <https://www.cvxpy.org/> |
| Pyomo | <https://pyomo.readthedocs.io/> |
| JuMP.jl | <https://jump.dev/> |
| CasADi | <https://web.casadi.org/> |
| Google OR-Tools | <https://developers.google.com/optimization> |
| HiGHS | <https://highs.dev/> |
| OSQP | <https://osqp.org/> |
| SCS | <https://www.cvxgrp.org/scs/> |
| Gurobi | <https://docs.gurobi.com/> |
| CPLEX | <https://www.ibm.com/docs/en/icos> |

#### differential-equations.md

| Tool | Docs |
|---|---|
| SUNDIALS | <https://sundials.readthedocs.io/> |
| DifferentialEquations.jl | <https://docs.sciml.ai/DiffEqDocs/> |
| Diffrax | <https://docs.kidger.site/diffrax/> |
| torchdiffeq | <https://github.com/rtqichen/torchdiffeq> |
| ModelingToolkit.jl | <https://docs.sciml.ai/ModelingToolkit/> |
| OpenModelica | <https://openmodelica.org/> |
| Simulink | <https://www.mathworks.com/help/simulink/> |

#### pde-and-fem.md

| Tool | Docs |
|---|---|
| FEniCSx | <https://docs.fenicsproject.org/> |
| Firedrake | <https://www.firedrakeproject.org/> |
| deal.II | <https://dealii.org/> |
| MFEM | <https://mfem.org/> |
| MOOSE Framework | <https://mooseframework.inl.gov/> |
| OpenFOAM | <https://www.openfoam.com/> |
| FreeFEM | <https://freefem.org/> |
| Gmsh | <https://gmsh.info/> |
| meshio | <https://github.com/nschloe/meshio> |
| CGAL | <https://www.cgal.org/> |
| Open CASCADE | <https://dev.opencascade.org/> |

#### scientific-visualization.md

| Tool | Docs |
|---|---|
| Matplotlib | <https://matplotlib.org/> |
| Plotly | <https://plotly.com/python/> — llms.txt: <https://plotly.com/llms.txt> |
| VTK | <https://vtk.org/> |
| PyVista | <https://docs.pyvista.org/> |
| ParaView | <https://www.paraview.org/> |
| Makie.jl | <https://docs.makie.org/> |
| HoloViz | <https://holoviz.org/> |

### meta-ds-hpc-docs

#### mpi-and-scheduling.md

| Tool | Docs |
|---|---|
| MPI Forum | <https://www.mpi-forum.org/> |
| Open MPI | <https://docs.open-mpi.org/> — llms.txt: <https://docs.open-mpi.org/llms.txt> |
| MPICH | <https://www.mpich.org/> |
| mpi4py | <https://mpi4py.readthedocs.io/> |
| MPI.jl | <https://juliaparallel.org/MPI.jl/> |
| OpenMP | <https://www.openmp.org/> |
| Dask | <https://docs.dask.org/> — llms.txt: <https://docs.dask.org/llms.txt> |
| Dask-Jobqueue | <https://jobqueue.dask.org/> |
| Ray | <https://docs.ray.io/> — llms.txt: <https://docs.ray.io/llms.txt> |
| Distributed.jl | <https://docs.julialang.org/> |
| Dagger.jl | <https://juliaparallel.org/Dagger.jl/> |
| Parsl | <https://parsl.readthedocs.io/> |
| Snakemake | <https://snakemake.readthedocs.io/> |
| Nextflow | <https://docs.seqera.io/nextflow> — llms.txt: <https://docs.seqera.io/llms.txt> |
| Flyte | <https://docs.flyte.org/> — llms.txt: <https://www.union.ai/llms.txt> |
| Slurm | <https://slurm.schedmd.com/> |
| OpenPBS | <https://openpbs.org/> |
| IBM Spectrum LSF | <https://www.ibm.com/docs/en/spectrum-lsf> |
| HTCondor | <https://htcondor.readthedocs.io/> |
| Kubernetes | <https://kubernetes.io/docs/> |

#### gpu-communication.md

| Tool | Docs |
|---|---|
| NVIDIA NCCL | <https://docs.nvidia.com/deeplearning/nccl/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| AMD RCCL | <https://rocm.docs.amd.com/projects/rccl/> |
| Intel oneCCL | <https://oneapi-src.github.io/oneCCL/> |
| Gloo | <https://github.com/pytorch/gloo> |
| UCX | <https://openucx.org/> |
| NVSHMEM | <https://docs.nvidia.com/nvshmem/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| libfabric | <https://ofiwg.github.io/libfabric/> |
| PyTorch Distributed | <https://docs.pytorch.org/> |
| TensorFlow Distributed | <https://www.tensorflow.org/> |
| JAX | <https://docs.jax.dev/> |
| DeepSpeed | <https://www.deepspeed.ai/> |
| Megatron-LM | <https://github.com/NVIDIA/Megatron-LM> |
| NVIDIA NeMo Framework | <https://docs.nvidia.com/nemo-framework/> — llms.txt: <https://docs.nvidia.com/nemo-framework/llms.txt> |

#### parallel-io.md

| Tool | Docs |
|---|---|
| xarray | <https://docs.xarray.dev/> — llms.txt: <https://docs.xarray.dev/llms.txt> |
| Zarr | <https://zarr.readthedocs.io/> |
| Awkward Array | <https://awkward-array.org/> |
| HDF5 | <https://support.hdfgroup.org/documentation/> |
| h5py | <https://docs.h5py.org/> |
| netCDF4 | <https://unidata.github.io/netcdf4-python/> |
| PnetCDF | <https://parallel-netcdf.github.io/> |
| ADIOS2 | <https://adios2.readthedocs.io/> |
| Apache Arrow | <https://arrow.apache.org/docs/> |
| Apache Parquet | <https://parquet.apache.org/> |
| Astropy | <https://docs.astropy.org/> |
| fsspec | <https://filesystem-spec.readthedocs.io/> |
| s3fs | <https://s3fs.readthedocs.io/> |
| gcsfs | <https://gcsfs.readthedocs.io/> |
| kerchunk | <https://fsspec.github.io/kerchunk/> |

### meta-ds-project

New entry points below were verified live 2026-07-24. Agent-oriented official
endpoints were checked first; documentation MCP availability is runtime-specific
and must be rechecked in the target environment.

#### assets/base/knowledge-references.md

| Tool | Docs |
|---|---|
| uv | <https://docs.astral.sh/uv/llms.txt> |
| Ruff | <https://docs.astral.sh/ruff/llms.txt> |
| pytest | <https://docs.pytest.org/> |
| Pydantic Settings | <https://pydantic.dev/llms.txt> |
| Just | <https://just.systems/man/en/> |
| pre-commit | <https://pre-commit.com/> |
| EditorConfig | <https://editorconfig.org/> |
| Loguru | <https://loguru.readthedocs.io/> |
| Gitleaks | <https://github.com/gitleaks/gitleaks> |
| Jupyter | <https://docs.jupyter.org/> |

#### storage-local.md

| Tool | Docs |
|---|---|
| Python | <https://docs.python.org/3/> |
| fsspec | <https://filesystem-spec.readthedocs.io/> |

#### storage-s3.md

| Tool | Docs |
|---|---|
| Amazon S3 | <https://docs.aws.amazon.com/s3/> |
| fsspec | <https://filesystem-spec.readthedocs.io/> |
| s3fs | <https://s3fs.readthedocs.io/> |

#### storage-huggingface.md

| Tool | Docs |
|---|---|
| Hugging Face Hub client | <https://huggingface.co/docs/huggingface_hub/llms.txt> |
| Datasets | <https://huggingface.co/docs/datasets/llms.txt> |

#### compute-structured.md

| Tool | Docs |
|---|---|
| Polars | <https://docs.pola.rs/> |
| Dask | <https://docs.dask.org/en/stable/llms.txt> |

#### compute-multimedia.md

| Tool | Docs |
|---|---|
| Ray Data | <https://docs.ray.io/en/latest/llms.txt> |
| Datasets | <https://huggingface.co/docs/datasets/llms.txt> |

#### model-inference.md

| Tool | Docs |
|---|---|
| Transformers | <https://huggingface.co/docs/transformers/llms.txt> |
| vLLM | <https://docs.vllm.ai/> |
| Hugging Face Hub client | <https://huggingface.co/docs/huggingface_hub/llms.txt> |
