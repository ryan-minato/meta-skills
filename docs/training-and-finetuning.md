---
title: Distributed Training & Finetuning
description: Distributed-training stacks and finetuning frameworks — DeepSpeed, Megatron, Lightning, NeMo, torchtune, Axolotl — for multi-GPU, multi-node, and post-training work.
tags: [machine-learning, training, hpc, gpu]
---

# Distributed Training & Finetuning

Fetch when the target trains across multiple GPUs or nodes, finetunes or post-trains existing models with a dedicated framework, or depends on a distributed-training stack. Each entry is one line and a documentation entry point; fetch launcher commands, recipe, and config syntax from the entry point, never from memory. No entry is a recommendation.

## Distributed Training

| Tool | One line | Docs |
|---|---|---|
| TorchTitan | PyTorch-native LLM pretraining at scale | <https://github.com/pytorch/torchtitan> |
| DeepSpeed | ZeRO sharding, pipeline parallelism, and training optimizations | <https://www.deepspeed.ai/> |
| Megatron-LM | NVIDIA's large-scale transformer training reference | <https://github.com/NVIDIA/Megatron-LM> |
| Megatron-Core | the composable library under Megatron-LM | <https://docs.nvidia.com/megatron-core/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| PyTorch Lightning | structured training loops with built-in multi-device strategies | <https://lightning.ai/docs/pytorch/> — llms.txt: <https://lightning.ai/llms.txt> |
| NVIDIA NeMo Framework | end-to-end generative-AI training platform | <https://docs.nvidia.com/nemo-framework/> — llms.txt: <https://docs.nvidia.com/nemo-framework/llms.txt> |
| Colossal-AI | parallelism strategies for large-model training | <https://colossalai.org/> |

## Finetuning & Post-Training

| Tool | One line | Docs |
|---|---|---|
| torchtune | PyTorch-native LLM finetuning recipes | <https://meta-pytorch.org/torchtune/> |
| LLaMA-Factory | config-driven finetuning across many model families | <https://llamafactory.readthedocs.io/> |
| Axolotl | YAML-driven finetuning (SFT, LoRA, preference tuning) | <https://docs.axolotl.ai/> |
| Unsloth | memory-efficient single-GPU finetuning kernels | <https://unsloth.ai/docs> — llms.txt: <https://unsloth.ai/docs/llms.txt> |
| OpenRLHF | RLHF training built on Ray, vLLM, and DeepSpeed | <https://github.com/OpenRLHF/OpenRLHF> |

## Gotchas

- PyTorch Distributed (DDP, FSDP, and collective APIs) documents inside PyTorch's own docs root — see the [deep-learning-frameworks](deep-learning-frameworks.md) page rather than a separate entry here.
- The Hugging Face training stack (Accelerate, PEFT, TRL) documents under the Hugging Face docs root — see the [huggingface](huggingface.md) page; Ray Train likewise lives with its ecosystem on the distributed-compute page.
