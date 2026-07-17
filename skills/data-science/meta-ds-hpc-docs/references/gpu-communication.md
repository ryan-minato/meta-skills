# GPU & Multi-Node Communication

Read when the target communicates across GPUs or nodes, including
framework distributed backends. One line and an entry point per tool;
fetch build and topology details from the entry point. No entry is a
recommendation.

## Tools

| Tool | One line | Docs |
|---|---|---|
| NVIDIA NCCL | GPU collective communication | <https://docs.nvidia.com/deeplearning/nccl/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| AMD RCCL | ROCm collective communication | <https://rocm.docs.amd.com/projects/rccl/> |
| Intel oneCCL | oneAPI collective communication | <https://oneapi-src.github.io/oneCCL/> |
| Gloo | CPU collective library behind PyTorch | <https://github.com/pytorch/gloo> |
| UCX | unified communication framework (RDMA, shared memory) | <https://openucx.org/> |
| NVSHMEM | GPU-initiated partitioned global memory | <https://docs.nvidia.com/nvshmem/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| libfabric | the OpenFabrics interface layer | <https://ofiwg.github.io/libfabric/> |
| PyTorch Distributed | DDP, FSDP, DTensor, and elastic launch inside PyTorch docs | <https://docs.pytorch.org/> |
| TensorFlow Distributed | tf.distribute strategies inside TensorFlow docs | <https://www.tensorflow.org/> |
| JAX | sharding and multi-host execution inside JAX docs | <https://docs.jax.dev/> |
| DeepSpeed | large-model distributed training | <https://www.deepspeed.ai/> |
| Megatron-LM | NVIDIA's large-scale transformer training | <https://github.com/NVIDIA/Megatron-LM> |
| NVIDIA NeMo Framework | end-to-end generative-AI training platform | <https://docs.nvidia.com/nemo-framework/> — llms.txt: <https://docs.nvidia.com/nemo-framework/llms.txt> |
