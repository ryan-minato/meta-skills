# Distributed Training Stacks

Read when the target trains across multiple GPUs or nodes, or depends on
a distributed-training framework. One line and an entry point per tool;
fetch launcher commands and config syntax from the entry point. No entry
is a recommendation.

## Frameworks

| Tool | One line | Docs |
|---|---|---|
| PyTorch Distributed | DDP, FSDP, and collective APIs inside PyTorch's own docs | <https://docs.pytorch.org/> |
| TorchTitan | PyTorch-native LLM pretraining at scale | <https://github.com/pytorch/torchtitan> |
| DeepSpeed | ZeRO sharding, pipeline parallelism, and training optimizations | <https://www.deepspeed.ai/> |
| Megatron-LM | NVIDIA's large-scale transformer training reference | <https://github.com/NVIDIA/Megatron-LM> |
| Megatron-Core | the composable library under Megatron-LM | <https://docs.nvidia.com/megatron-core/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| PyTorch Lightning | structured training loops with built-in multi-device strategies | <https://lightning.ai/docs/pytorch/> — llms.txt: <https://lightning.ai/llms.txt> |
| NVIDIA NeMo Framework | end-to-end generative-AI training platform | <https://docs.nvidia.com/nemo-framework/> — llms.txt: <https://docs.nvidia.com/nemo-framework/llms.txt> |
| Colossal-AI | parallelism strategies for large-model training | <https://colossalai.org/> |
