---
title: DataFrames, Storage & Data Quality
description: Dataframe and embedded-SQL libraries, columnar and scientific storage formats, parallel and object-storage I/O, and schema/quality validation.
tags: [data-science, data-engineering, storage, tabular]
---

# DataFrames, Storage & Data Quality

Fetch when the target manipulates tables with dataframes or embedded SQL; reads or writes columnar, chunked, or hierarchical data files — including labeled N-dimensional arrays, parallel I/O, or object storage; or validates schemas and monitors data quality. Each entry is one line and a documentation entry point; fetch install commands and API details from the entry point, never from memory. No entry is a recommendation.

## Dataframes & Embedded SQL

| Tool | One line | Docs |
|---|---|---|
| pandas | the standard dataframe library | <https://pandas.pydata.org/docs/> |
| Polars | fast dataframes with lazy execution and SQL | <https://docs.pola.rs/> |
| DuckDB | embedded OLAP SQL over files and dataframes | <https://duckdb.org/docs/> — llms.txt: <https://duckdb.org/llms.txt> |
| Ibis | one expression API over many query backends | <https://ibis-project.org/> |
| cuDF | pandas-compatible dataframes on GPUs | <https://docs.rapids.ai/api/cudf/stable/> |

## Storage Formats & Parallel I/O

| Tool | One line | Docs |
|---|---|---|
| Apache Arrow | in-memory columnar format, Parquet and Feather I/O | <https://arrow.apache.org/docs/> |
| Apache Parquet | the columnar file format | <https://parquet.apache.org/> |
| Zarr | chunked, compressed, cloud-native N-D arrays | <https://zarr.readthedocs.io/> |
| xarray | labeled N-D arrays with NetCDF/Zarr/Dask integration | <https://docs.xarray.dev/> — llms.txt: <https://docs.xarray.dev/llms.txt> |
| Awkward Array | ragged, nested arrays at scale | <https://awkward-array.org/> |
| h5py | Python bindings for HDF5 (incl. parallel builds) | <https://docs.h5py.org/> |
| HDF5 | the hierarchical scientific data format | <https://support.hdfgroup.org/documentation/> |
| netCDF4 | Python interface to NetCDF files | <https://unidata.github.io/netcdf4-python/> |
| PnetCDF | parallel NetCDF I/O | <https://parallel-netcdf.github.io/> |
| ADIOS2 | adaptable I/O for extreme-scale simulation output | <https://adios2.readthedocs.io/> |
| Astropy | astronomy tooling including FITS I/O | <https://docs.astropy.org/> |
| fsspec | one filesystem API over local and object storage | <https://filesystem-spec.readthedocs.io/> |
| s3fs | S3 through fsspec | <https://s3fs.readthedocs.io/> |
| gcsfs | Google Cloud Storage through fsspec | <https://gcsfs.readthedocs.io/> |
| kerchunk | cloud-optimized indexing of archival formats | <https://fsspec.github.io/kerchunk/> |

## Data Quality & Validation

| Tool | One line | Docs |
|---|---|---|
| Pandera | dataframe schema validation | <https://pandera.readthedocs.io/> |
| Great Expectations | data quality expectations and checkpoints | <https://docs.greatexpectations.io/> |
| Cleanlab | label-error detection in datasets | <https://docs.cleanlab.ai/> |
| Pydantic | typed data validation for records and configs | <https://pydantic.dev/docs/> — llms.txt: <https://pydantic.dev/llms.txt> |

## Gotchas

- Cluster-provided modules (HDF5, MPI-enabled NetCDF) often differ from pip-installed builds — record both the entry point and the site's module convention when one exists, and fetch parallel-build details (MPI-enabled HDF5/NetCDF) from the entry point.
- Geospatial raster I/O on xarray (Rasterio, rioxarray) lives on the [geospatial](geospatial.md) page.
- Data and model quality *monitoring* (Evidently) lives on the pipelines-and-mlops page.
