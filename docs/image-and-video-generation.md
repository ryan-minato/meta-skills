---
title: Image & Video Generation
description: Diffusion-model generation UIs, LoRA trainers, conditioning adapters, and open video-generation projects.
tags: [machine-learning, generative, vision]
---

# Image & Video Generation

Fetch when the target generates images or video with diffusion-model tooling. Each entry is one line and a documentation entry point; most are cloned applications whose install procedure lives at the entry point — fetch it from there, never from memory. No entry is a recommendation.

## Tools

| Tool | One line | Docs |
|---|---|---|
| ComfyUI | node-graph diffusion workflows | <https://docs.comfy.org/> — llms.txt: <https://docs.comfy.org/llms.txt> |
| Stable Diffusion WebUI Forge | optimized fork of the A1111 web UI | <https://github.com/lllyasviel/stable-diffusion-webui-forge> |
| InvokeAI | studio-style generation app | <https://github.com/invoke-ai/InvokeAI> |
| kohya_ss | LoRA and finetune training GUI | <https://github.com/bmaltais/kohya_ss> |
| ControlNet | structural conditioning for diffusion models | <https://github.com/lllyasviel/ControlNet> |
| IP-Adapter | image-prompt conditioning adapter | <https://github.com/tencent-ailab/IP-Adapter> |
| LyCORIS | LoRA-family parameter-efficient methods for diffusion | <https://github.com/KohakuBlueleaf/LyCORIS> |
| Open-Sora | open video-generation training and inference | <https://github.com/hpcaitech/Open-Sora> |
| LTX-Video | real-time-capable video generation models | <https://github.com/Lightricks/LTX-Video> |

## Gotchas

- Most tools here are cloned applications, not pip packages — the repository root is the documentation entry point and the install procedure lives in its README.
- Diffusers documents under the Hugging Face docs root — see the [huggingface page](huggingface.md).
