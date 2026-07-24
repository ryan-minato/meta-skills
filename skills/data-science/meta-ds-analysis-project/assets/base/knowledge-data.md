# Data

Load before changing source acquisition, schemas, identities, storage
locations, transformations, or product publication.

## Contract

- Every source has a name, backend, URI, immutable identity, schema version,
  contract, and sensitivity classification.
- Local original inputs live directly at `data/<source>/`; there is no
  `data/raw/`.
- `data/` never contains derived, cached, temporary, or final data.
- Only download workflows may publish a new local source path, and they refuse
  overwrite.
- Every product has a stage, declared inputs, schema version, owner workflow,
  distinct location, and publication status.
- Critical contract and integration failures block publication. Identifiable
  row-level rejects go to the declared quarantine product with a reason and
  count; no stage silently drops records.

## Source registry

| Source | Backend | Location | Immutable identity | Schema version | Sensitivity | Contract and structure |
|---|---|---|---|---|---|---|
| __SOURCE_NAME__ | __BACKEND__ | __URI__ | __VERSION_OR_CHECKSUM__ | __SCHEMA_VERSION__ | __SENSITIVITY__ | __CONTRACT_AND_STRUCTURE__ |

## Product registry

| Product | Stage | Inputs | Schema version | Producer | Backend and location | Consumers | Retention |
|---|---|---|---|---|---|---|---|
| __PRODUCT_NAME__ | __STAGE__ | __INPUT_NAMES__ | __SCHEMA_VERSION__ | __WORKFLOW__ | __BACKEND_AND_URI__ | __CONSUMERS__ | __RETENTION__ |

## Data-quality rules

__CRITICAL_CONTRACTS_ROW_LEVEL_RULES_QUARANTINE_PRODUCT_AND_KNOWN_LIMITATIONS__

## Lineage and publication evidence

__PRODUCT_INPUTS_TRANSFORMATIONS_INTEGRATION_KEYS_COUNTS_QUALITY_RESULTS_AND_PUBLICATION_STATUS__

## Source-specific details

__APPEND_ONLY_THE_STORAGE_SECTIONS_FOR_BACKENDS_ACTUALLY_USED__
