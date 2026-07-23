---
name: meta-ds-geospatial-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  geospatial-analysis project to authoritative documentation entry
  points — vector and raster stacks (GeoPandas, Shapely, pyproj, GDAL,
  Rasterio, rioxarray) and spatial engines (DuckDB Spatial, Apache
  Sedona, cuSpatial). Use when a harness build must record where the
  docs live for a project that processes geographic vector or raster
  data. Not for choosing between tools or recommending one, and not for
  general dataframes, visualization, or remote-sensing ML models.
---

# Geospatial Analysis Documentation Map

This skill produces the documentation entry points a harness build
records for a geospatial project. It expects a harness build in
progress and access to the target's dependency manifests. Per-tool
content is one line plus a URL — install commands (including GDAL's
system dependencies) are always fetched from the recorded entry point,
never recalled from memory — and nothing here is a recommendation: when
the target lacks a tool for a need, record the option list with URLs
and leave the choice to the user.

## Workflow

1. Detect the geospatial stack: dependency manifests and imports
   (`geopandas`, `shapely`, `pyproj`, `osgeo`, `rasterio`,
   `rioxarray`, `sedona`), spatial data files (GeoJSON, Shapefile,
   GeoTIFF, GeoParquet), and CRS references in code.
2. Read [geospatial.md](references/geospatial.md) for the vector,
   raster, and spatial-engine libraries in play.
3. For every entry point about to be recorded, prefer an agent-oriented
   rendition: a page's `.md` source, then `<docs-root>/llms.txt` (a
   compact index). Fall back to `llms-full.txt` only when neither
   exists, and never read it whole — it is the whole site as one
   file; search it programmatically.
4. Record each detected tool — name, one-line role, documentation entry
   point, and its llms.txt when present — wherever the harness keeps
   conventions.

Done when: every geospatial library the target actually uses has a
recorded, live documentation entry point, and nothing recorded ranks or
recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: stack selection is the user's
  decision.
- GDAL and its bindings need matching system libraries — fetch the
  current install guidance from the entry point rather than assuming
  pip suffices.
- The same tool may appear in another domain skill's tables (Rasterio,
  rioxarray, Sedona, cuSpatial); record it once per harness, not once
  per skill.
- Tools this skill does not list are out of scope: record only what its
  tables cover, and leave finding docs for anything else to the agent —
  it is not this skill's job.
