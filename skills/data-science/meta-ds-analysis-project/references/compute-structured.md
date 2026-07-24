# Structured Data Compute

Use this branch when the project processes tables, records, or dataframe-like
data.

## Selection

1. Prefer Polars when the workload fits one machine, including workloads its
   lazy and streaming execution can handle.
2. Prefer Dask only when the workload genuinely needs distributed memory or
   distributed execution.
3. Record the scale evidence and chosen engine in `ARCHITECTURE.md` or
   `.agents/knowledge/PROJECT.md`.
4. Install only the chosen engine. Do not add Polars, Dask, pandas, and Spark
   as speculative alternatives.

Keep transformations as functions in `src/<package>/processing/`. Test
project-owned parsers, normalizations, filters, deduplication, joins,
aggregations, schema invariants, boundary conditions, and error paths where a
plausible mistake would corrupt a product. Do not repeat the engine's own
tests.

For each source, make the input schema, key, nullability, accepted value
domain, and schema version explicit before cleaning. Cleaning stages must
return accepted records and identifiable rejected records separately; attach a
stable rejection reason and publish the latter only to the declared quarantine
product. A critical contract failure stops the workflow before a downstream
product is published.

For integration, document source-to-source key mappings, key normalization,
join type, expected cardinality, and unmatched-record policy. Test duplicate
keys, missing keys, key-format changes, nulls, one-to-many expansion, and
unmatched records using representative small fixtures. A violated documented
cardinality or integration invariant is critical and blocks publication.

## Documentation entry points

| Tool | Docs |
|---|---|
| Polars | <https://docs.pola.rs/> |
| Dask | <https://docs.dask.org/en/stable/llms.txt> |
