---
name: meta-ml-vision-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  computer-vision project to authoritative documentation entry points —
  core vision libraries and pretrained models (OpenCV, torchvision,
  timm, OpenMMLab, Ultralytics), detection/segmentation/tracking (SAM,
  Grounding DINO, supervision tooling), OCR and document AI (PaddleOCR,
  Tesseract, Docling, Unstructured), and 3D vision and neural rendering
  (Open3D, PyTorch3D, Nerfstudio). Use when a harness build must record
  where the docs live for a project that processes images, video, point
  clouds, or documents as images. Not for choosing between tools or
  recommending one, and not for image/video generation or non-vision
  modalities.
---

# Computer Vision Documentation Map

This skill produces the documentation entry points a harness build
records for a computer-vision project. It expects a harness build in
progress and access to the target's dependency manifests. Per-tool
content is one line plus a URL — install commands and API details are
always fetched from the recorded entry point, never recalled from
memory — and nothing here is a recommendation: when the target lacks a
tool for a need, record the option list with URLs and leave the choice
to the user.

## Workflow

1. Detect the vision stack: dependency manifests and imports (`cv2`,
   `torchvision`, `timm`, `mmdet`, `ultralytics`, `albumentations`,
   `kornia`, `skimage`, `PIL`), model weights and dataset layouts
   (COCO/YOLO annotations), and media directories.
2. Read [core-vision.md](references/core-vision.md) when any
   general-purpose vision library, pretrained-model zoo, or augmentation
   library is in play.
3. Read
   [detection-segmentation-tracking.md](references/detection-segmentation-tracking.md)
   when the target detects, segments, or tracks objects, or curates
   detection datasets.
4. Read [ocr-and-document-ai.md](references/ocr-and-document-ai.md)
   when the target reads text from images or parses document layouts.
5. Read [3d-vision.md](references/3d-vision.md) when the target works
   with point clouds, meshes, or neural rendering.
6. For every entry point about to be recorded, prefer an agent-oriented
   rendition: a page's `.md` source, then `<docs-root>/llms.txt` (a
   compact index). Fall back to `llms-full.txt` only when neither
   exists, and never read it whole — it is the whole site as one
   file; search it programmatically.
7. Record each detected tool the tables cover — name, one-line role,
   documentation entry point, and its llms.txt when present — wherever
   the harness keeps conventions.

Done when: every vision library the target actually uses has a recorded,
live documentation entry point, and nothing recorded ranks or recommends
between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: detector and OCR selection is
  the user's decision.
- OpenCV's docs root serves version directories rather than a landing
  index — record the root and let the fetch pick the current version.
- The same tool may appear in another domain skill's tables (timm also
  lives in the Hugging Face map); record it once per harness, not once
  per skill.
- Tools this skill does not list are out of scope — leave finding their
  docs to the agent; it is not this skill's job.
