# Scientific Data & Parallel I/O

Read when the target reads or writes scientific data in parallel or
from object storage. One line and an entry point per tool; fetch
parallel-build details (MPI-enabled HDF5/NetCDF) from the entry point.
No entry is a recommendation.

## Tools

| Tool | One line | Docs |
|---|---|---|
| xarray | labeled N-D arrays over NetCDF/Zarr/Dask | <https://docs.xarray.dev/> — llms.txt: <https://docs.xarray.dev/llms.txt> |
| Zarr | chunked, compressed, cloud-native N-D arrays | <https://zarr.readthedocs.io/> |
| Awkward Array | ragged, nested arrays at scale | <https://awkward-array.org/> |
| h5py | Python bindings for HDF5 (incl. parallel builds) | <https://docs.h5py.org/> |
| HDF5 | the hierarchical scientific data format | <https://support.hdfgroup.org/documentation/> |
| netCDF4 | Python interface to NetCDF | <https://unidata.github.io/netcdf4-python/> |
| PnetCDF | parallel NetCDF I/O | <https://parallel-netcdf.github.io/> |
| ADIOS2 | adaptable I/O for extreme-scale simulation output | <https://adios2.readthedocs.io/> |
| Apache Arrow | in-memory columnar format and Parquet I/O | <https://arrow.apache.org/docs/> |
| Apache Parquet | the columnar file format | <https://parquet.apache.org/> |
| Astropy | astronomy tooling including FITS I/O | <https://docs.astropy.org/> |
| fsspec | one filesystem API over local and object storage | <https://filesystem-spec.readthedocs.io/> |
| s3fs | S3 through fsspec | <https://s3fs.readthedocs.io/> |
| gcsfs | Google Cloud Storage through fsspec | <https://gcsfs.readthedocs.io/> |
| kerchunk | cloud-optimized indexing of archival formats | <https://fsspec.github.io/kerchunk/> |
