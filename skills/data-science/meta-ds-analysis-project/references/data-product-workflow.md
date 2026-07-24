# Batch Data-Product Workflow

Read this before implementing or extending a structured batch data-product
chain. It describes the minimum delivery path; adapt names and implementation
to the target project rather than copying generic business rules.

## Decide the contract before transformation

For every source, record its immutable identity, owner, sensitivity,
schema/version, primary or business key, nullability, allowed values,
freshness expectation when relevant, and known limitations. For every product,
record its stage, declared inputs, output schema/version, owner workflow,
consumers, retention, and publication location.

Use the configured source and product names as the lineage vocabulary. A
product may depend on sources or earlier products, never on an undocumented
path. Keep the sequence acyclic and make the final product depend on the
governed chain rather than reading source files ad hoc.

## Implement the chain

1. Acquire each source immutably, then profile its schema, counts, key
   uniqueness, nulls, and value distributions sufficient to establish the
   recorded contract.
2. Validate critical source contracts before transformation. Critical schema,
   key, required-field, and documented integration failures stop publication.
3. Clean and standardize in reusable processing functions: parse values,
   normalize names and keys, deduplicate according to a documented survivor
   rule, and preserve the reason for every rejected row.
4. If the product has more than one source, integrate only on documented
   normalized keys. Check the specified join cardinality and unmatched-record
   policy before writing the next product.
5. Write accepted stage products and a separate quarantine product
   atomically. The quarantine records a rejection reason and enough safe
   lineage to investigate without logging sensitive raw records.
6. Publish the final product only after its critical gates pass. Persist a
   quality report and provenance containing inputs, schema versions, rule
   results, accepted and rejected counts, transformations, integration
   decisions, configuration, code revision, and publication decision.

## Quality policy

Use `row_rejection_policy = "quarantine"`. This permits handling an
identifiable row-level defect, not downgrading a broken contract. A stage may
quarantine a row only when the rule, reason, and expected downstream effect
are documented. Unexpected schema changes, missing keys, failed required
completeness, and violated join cardinality are critical: fail the run and do
not publish a new final product.

## Tests

Use small, deterministic fixtures. Test normal and failure paths for parsing,
normalization, deduplication, row rejection, join cardinality, unmatched rows,
schema checks, and the fact that a critical failure does not publish a final
product. Assert both accepted output and quarantine reasons/counts. Test
custom project logic, not dataframe-engine behavior or thin workflow glue.
