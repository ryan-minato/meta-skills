---
name: meta-ml-science-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  scientific machine-learning project to authoritative documentation
  entry points — medical imaging (MONAI, TorchIO), chemistry and drug
  discovery (RDKit, DeepChem), biology and omics (Biopython, Scanpy,
  scvi-tools), molecular simulation and materials (OpenMM, ASE,
  pymatgen), and physics-informed ML (PhysicsNeMo, DeepXDE, e3nn) —
  plus the discovery procedure (llms.txt probing, PyPI metadata,
  official org repos) for tools not listed. Use when a harness build
  must record where the docs live for a project applying ML in
  medicine, biology, chemistry, or the physical sciences. Not for
  choosing between tools or recommending one, and not for general
  scientific computing without ML.
---

# Scientific ML Documentation Map

This skill produces the documentation entry points a harness build
records for a project applying machine learning in the sciences. It
expects a harness build in progress and access to the target's
dependency manifests. Per-tool content is one line plus a URL — install
commands and API details are always fetched from the recorded entry
point, never recalled from memory — and nothing here is a
recommendation: when the target lacks a tool for a need, record the
option list with URLs and leave the choice to the user.

## Workflow

1. Detect the science-ML stack: dependency manifests and imports
   (`monai`, `torchio`, `rdkit`, `deepchem`, `Bio`, `scanpy`, `scvi`,
   `openmm`, `deepxde`, `e3nn`, `ase`, `pymatgen`), domain data formats
   (DICOM/NIfTI, SMILES/SDF, FASTA, AnnData, CIF), and simulation
   configs.
2. Read [science-ml.md](references/science-ml.md) for the medical,
   biological, chemical, and physics-informed libraries in play.
3. For every entry point about to be recorded, probe
   `<docs-root>/llms.txt` (then `llms-full.txt`) and prefer the
   plain-text index when present.
4. For tools the tables miss, or any URL that no longer resolves, follow
   [doc-discovery.md](references/doc-discovery.md).
5. Record each detected tool — name, one-line role, documentation entry
   point, and its llms.txt when present — wherever the harness keeps
   conventions.

Done when: every scientific-ML library the target actually uses has a
recorded, live documentation entry point, and nothing recorded ranks or
recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: domain-library selection is the
  user's decision.
- Several tools here (RDKit, OpenMM, ASE) install from conda-forge
  rather than PyPI — fetch the current channel from the entry point.
- General numerical solvers and PDE frameworks without ML belong to a
  scientific-computing stack, not here.
