---
title: Scientific & Domain ML
description: ML libraries for medicine, biology, chemistry, materials, and physics-informed modeling.
tags: [machine-learning, scientific-computing, simulation]
---

# Scientific & Domain ML

Fetch when the target applies ML in medicine, biology, chemistry, materials, or the physical sciences — medical imaging, cheminformatics, omics, molecular simulation, or physics-informed networks. Each entry is one line and a documentation entry point; fetch install commands and API details from the entry point, never from memory. No entry is a recommendation.

## Tools

| Tool | One line | Docs |
|---|---|---|
| MONAI | medical-imaging deep learning on PyTorch | <https://monai.readthedocs.io/> |
| TorchIO | 3D medical image loading and augmentation | <https://docs.torchio.org/> |
| RDKit | cheminformatics toolkit (conda-forge install) | <https://www.rdkit.org/docs/> |
| DeepChem | ML for chemistry and materials | <https://deepchem.readthedocs.io/> |
| Biopython | sequence handling and bioinformatics tooling | <https://biopython.org/> |
| Scanpy | single-cell omics analysis | <https://scanpy.scverse.org/> |
| scvi-tools | probabilistic models for single-cell data | <https://docs.scvi-tools.org/> |
| OpenMM | GPU molecular dynamics (conda-forge install) | <https://openmm.org/> |
| NVIDIA BioNeMo | biomolecular foundation-model framework | <https://docs.nvidia.com/bionemo-framework/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| NVIDIA PhysicsNeMo | physics-informed ML framework | <https://docs.nvidia.com/physicsnemo/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| DeepXDE | physics-informed neural networks | <https://deepxde.readthedocs.io/> |
| e3nn | equivariant neural networks | <https://docs.e3nn.org/> |
| ASE | atomistic simulation environment | <https://ase-lib.org/> |
| pymatgen | materials analysis and structure handling | <https://pymatgen.org/> |

## Gotchas

- Several tools here (RDKit, OpenMM, ASE) install from conda-forge rather than PyPI — fetch the current channel guidance from the entry point.
