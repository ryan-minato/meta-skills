---
title: Visualization, Data Apps & Notebooks
description: Plotting libraries, dashboards and small data apps, scientific 3D rendering, and notebook or publishing tooling.
tags: [data-science, scientific-computing, visualization]
---

# Visualization, Data Apps & Notebooks

Fetch when the target plots, builds dashboards, or ships small data apps; renders meshes, volumes, or large scientific data; or uses notebooks and publishes computational documents. Each entry is one line and a documentation entry point; fetch install commands and API details from the entry point, never from memory. No entry is a recommendation.

## Plotting & Data Apps

| Tool | One line | Docs |
|---|---|---|
| Matplotlib | the foundational plotting library | <https://matplotlib.org/> |
| Seaborn | statistical graphics on Matplotlib | <https://seaborn.pydata.org/> |
| Plotly | interactive charts | <https://plotly.com/python/> — llms.txt: <https://plotly.com/llms.txt> |
| Altair | declarative charts on Vega-Lite | <https://altair-viz.github.io/> |
| HoloViz | the HoloViews/Panel/Datashader family hub | <https://holoviz.org/> |
| HoloViews | data-driven plotting in the HoloViz family | <https://holoviews.org/> |
| hvPlot | one plotting API over pandas/xarray/Dask | <https://hvplot.holoviz.org/> |
| Datashader | server-side rendering of very large datasets | <https://datashader.org/> |
| Panel | dashboards and apps in the HoloViz family | <https://panel.holoviz.org/> |
| Streamlit | data apps from Python scripts | <https://docs.streamlit.io/> — llms.txt: <https://docs.streamlit.io/llms.txt> |
| Plotly Dash | analytical web apps on Plotly | <https://dash.plotly.com/> |

## Scientific 3D Visualization

| Tool | One line | Docs |
|---|---|---|
| VTK | the visualization toolkit for 3D data | <https://vtk.org/> |
| PyVista | Pythonic 3D plotting on VTK | <https://docs.pyvista.org/> |
| ParaView | large-scale visualization application | <https://www.paraview.org/> |
| Makie.jl | high-performance plotting for Julia | <https://docs.makie.org/> |

## Notebooks & Publishing

| Tool | One line | Docs |
|---|---|---|
| IPython | the interactive Python shell and kernel | <https://ipython.readthedocs.io/> |
| Jupyter | the notebook ecosystem's documentation hub | <https://docs.jupyter.org/> |
| JupyterLab | the Jupyter IDE | <https://jupyterlab.readthedocs.io/> |
| Jupyter Server | the backend serving Jupyter clients | <https://jupyter-server.readthedocs.io/> |
| Quarto | scientific publishing from notebooks and markdown (CLI install) | <https://quarto.org/> — llms.txt: <https://quarto.org/llms.txt> |

## Gotchas

- Quarto ships as a CLI, not a Python package — fetch the install method from its docs.
- Gradio is Hugging Face-owned and documents under the Hugging Face docs root — see the [huggingface](huggingface.md) page.
