---
title: Geospatial Analysis
description: Vector and raster stacks, CRS handling, and spatial engines for geographic data.
tags: [data-science, geospatial]
---

# Geospatial Analysis

Fetch when the target processes geographic vector or raster data — geographic dataframes, geometry operations, coordinate reference systems, raster I/O, or spatial SQL and cluster engines. Each entry is one line and a documentation entry point; fetch install commands (and system-library requirements) from the entry point, never from memory. No entry is a recommendation.

## Tools

| Tool | One line | Docs |
|---|---|---|
| GeoPandas | geographic dataframes on pandas | <https://geopandas.org/> |
| Shapely | planar geometry objects and operations | <https://shapely.readthedocs.io/> |
| pyproj | coordinate reference systems and transformations | <https://pyproj4.github.io/pyproj/> |
| GDAL | the raster/vector translation foundation | <https://gdal.org/> |
| Rasterio | raster I/O on GDAL | <https://rasterio.readthedocs.io/> |
| rioxarray | rasterio-backed geospatial extension for xarray | <https://corteva.github.io/rioxarray/> |
| DuckDB Spatial | spatial SQL inside DuckDB | <https://duckdb.org/docs/> — llms.txt: <https://duckdb.org/llms.txt> |
| Apache Sedona | spatial analytics on Spark and Flink | <https://sedona.apache.org/> |
| NVIDIA RAPIDS cuSpatial | GPU geospatial operations | <https://docs.rapids.ai/api/cuspatial/stable/> |

## Gotchas

- GDAL and its bindings need matching system libraries — fetch the current install guidance from the entry point rather than assuming pip suffices.
- DuckDB Spatial documents inside DuckDB's docs root; DuckDB itself lives on the [dataframes-and-storage](dataframes-and-storage.md) page.
