---
title: Computer Vision
description: Core vision libraries, pretrained-model zoos, augmentation, and detection/segmentation/tracking tooling.
tags: [machine-learning, vision]
---

# Computer Vision

Fetch when the target uses any general-purpose vision library, pretrained-model zoo, or augmentation library, or when it detects, segments, or tracks objects or curates detection datasets. Each entry is one line and a documentation entry point; fetch install commands and API details from the entry point, never from memory. No entry is a recommendation.

## Core Libraries

| Tool | One line | Docs |
|---|---|---|
| OpenCV | the general-purpose vision library | <https://docs.opencv.org/> |
| torchvision | PyTorch's datasets, transforms, and vision models | <https://docs.pytorch.org/vision/> |
| MMEngine | OpenMMLab's training-loop foundation | <https://mmengine.readthedocs.io/> |
| MMPreTrain | OpenMMLab pretraining and classification | <https://mmpretrain.readthedocs.io/> |
| MMDetection | OpenMMLab object detection | <https://mmdetection.readthedocs.io/> |
| MMSegmentation | OpenMMLab semantic segmentation | <https://mmsegmentation.readthedocs.io/> |
| MMPose | OpenMMLab pose estimation | <https://mmpose.readthedocs.io/> |
| MMDetection3D | OpenMMLab 3D detection | <https://mmdetection3d.readthedocs.io/> |
| MMAction2 | OpenMMLab video understanding | <https://mmaction2.readthedocs.io/> |
| Detectron2 | Meta's detection and segmentation platform | <https://detectron2.readthedocs.io/> |
| Ultralytics YOLO | YOLO training, validation, and deployment | <https://docs.ultralytics.com/> — llms.txt: <https://docs.ultralytics.com/llms.txt> |
| Albumentations | fast image augmentation | <https://albumentations.ai/docs/> — llms.txt: <https://albumentations.ai/llms.txt> |
| Kornia | differentiable vision ops on PyTorch tensors | <https://kornia.readthedocs.io/> |
| scikit-image | image processing on NumPy arrays | <https://scikit-image.org/> |
| Pillow | Python image loading and manipulation | <https://pillow.readthedocs.io/> |
| NVIDIA DALI | GPU-accelerated data loading pipelines | <https://docs.nvidia.com/deeplearning/dali/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| MediaPipe | on-device perception pipelines | <https://developers.google.com/edge/mediapipe> |

## Detection, Segmentation & Tracking

| Tool | One line | Docs |
|---|---|---|
| Segment Anything | promptable segmentation foundation model | <https://github.com/facebookresearch/segment-anything> |
| SAM 2 | segmentation across images and video | <https://github.com/facebookresearch/sam2> |
| Grounding DINO | open-vocabulary detection from text prompts | <https://github.com/IDEA-Research/GroundingDINO> |
| RT-DETR | real-time detection transformer | <https://github.com/lyuwenyu/RT-DETR> |
| ByteTrack | multi-object tracking by associating every box | <https://github.com/FoundationVision/ByteTrack> |
| Deep SORT | appearance-based multi-object tracking | <https://github.com/nwojke/deep_sort> |
| FiftyOne | dataset curation and model-result exploration | <https://docs.voxel51.com/> — llms.txt: <https://docs.voxel51.com/llms.txt> |
| Roboflow Supervision | reusable detection/segmentation utilities | <https://supervision.roboflow.com/> — llms.txt: <https://supervision.roboflow.com/llms.txt> |

## Gotchas

- OpenCV's docs root serves version directories rather than a landing index — record the root and let the fetch pick the current version.
- timm documents under the Hugging Face docs root — see the [huggingface page](huggingface.md).
