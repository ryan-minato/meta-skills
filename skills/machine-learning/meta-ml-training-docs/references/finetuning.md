# Finetuning & Post-Training Frameworks

Read when the target finetunes or post-trains existing models with a
dedicated framework. One line and an entry point per tool; fetch recipe
and config details from the entry point. No entry is a recommendation.

## Frameworks

| Tool | One line | Docs |
|---|---|---|
| torchtune | PyTorch-native LLM finetuning recipes | <https://meta-pytorch.org/torchtune/> |
| LLaMA-Factory | config-driven finetuning across many model families | <https://llamafactory.readthedocs.io/> |
| Axolotl | YAML-driven finetuning (SFT, LoRA, preference tuning) | <https://docs.axolotl.ai/> |
| Unsloth | memory-efficient single-GPU finetuning kernels | <https://unsloth.ai/docs> — llms.txt: <https://unsloth.ai/docs/llms.txt> |
| OpenRLHF | RLHF training built on Ray, vLLM, and DeepSpeed | <https://github.com/OpenRLHF/OpenRLHF> |
