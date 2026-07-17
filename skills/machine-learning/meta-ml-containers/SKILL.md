---
name: meta-ml-containers
description: >-
  Disposable meta-skill (delete after the harness is built): helps find
  currently available GPU container images — bundled credential-free
  scripts list and filter NVIDIA NGC catalog images and NGC or Docker Hub
  tags, and a reference maps each image family's characteristics to the
  situations it fits. Use when a Dockerfile, compose file, or dev
  container needs its GPU base image chosen or its tag refreshed, or when
  checking which CUDA or ROCm builds currently exist. It supplies the
  verified image and tag; the container setup around that FROM line is
  the caller's. Not for CPU-only projects.
---

# GPU Container Image Discovery

This skill produces a verified, recorded choice-space of GPU container
images for a project that runs ML in containers: which image families fit
the situation, which images and tags exist right now, and the commands
that refresh those listings. It expects the container need to already be
established — a Dockerfile, a dev container, or a deployment target.
Tag inventories are volatile: always enumerate live with the bundled
scripts, never assert an image or tag from memory. This skill informs;
the image choice stays with the user.

## Workflow

1. Pin down what is being looked for: a new base image, a fresher tag for
   an image already in use, or a build matching specific hardware (CUDA
   generation, ROCm, multi-arch).
2. Read [gpu-image-catalog.md](references/gpu-image-catalog.md) to
   shortlist the image families whose characteristics fit, and note the
   preinstalled-framework-vs-lockfile either/or it explains.
3. Enumerate what exists right now with the bundled scripts (stdlib-only
   Python, public registries, no credentials):
   - `scripts/list_ngc_images.py --query <term>` — find NGC repositories
     matching a term.
   - `scripts/list_ngc_tags.py <org>/<repo> [--filter <regex>]` — live
     tags of one NGC image.
   - `scripts/list_dockerhub_tags.py <namespace>/<repo> [--filter <regex>]`
     — live tags of one Docker Hub repository, newest first.
4. If a script fails or the registry is not one they cover, follow
   [image-discovery.md](references/image-discovery.md) instead.
5. Verify the shortlisted tag before recording it: `docker manifest
   inspect <image>:<tag>` confirms existence and platforms; for NGC
   monthly tags, confirm the CUDA/driver pairing from NVIDIA's support
   matrix (entry point in the image-family reference).
6. Record wherever the harness keeps conventions: the chosen image and
   tag, why that family fits, and the exact enumeration command that
   refreshes the listing when the tag next needs updating.

Done when: the candidate image is confirmed against a live tag listing,
its driver compatibility is checked from the vendor's matrix, and the
image, tag, and refresh command are recorded in the harness.

## Gotchas

- Tags remembered from tutorials or training data are frequently gone or
  superseded — enumerate first, then pin what the listing actually shows.
- An NGC tag name does not state its minimum driver; that pairing lives
  only in the support matrix, and skipping the check surfaces later as
  cryptic CUDA initialization errors on the training box.
- The NGC search endpoint the script uses is the catalog UI's, not a
  documented API — if it breaks, fall back to the discovery reference
  rather than patching blind.
- The scripts read public registries anonymously and never send
  credentials; entitled or private images need the vendor's own
  authenticated tooling.
