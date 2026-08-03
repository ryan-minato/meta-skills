---
title: Privacy, Robustness & Federated Learning
description: Differential privacy, adversarial robustness, fairness auditing, PII redaction, interpretability, and federated-learning frameworks.
tags: [machine-learning, trustworthy]
---

# Privacy, Robustness & Federated Learning

Fetch when the target trains with differential privacy, tests adversarial robustness, audits fairness, redacts PII, explains models, or trains across parties without centralizing data. Each entry is one line and a documentation entry point; fetch install commands and API details from the entry point, never from memory. No entry is a recommendation.

## Privacy, Robustness, Fairness & Interpretability

| Tool | One line | Docs |
|---|---|---|
| Opacus | differentially private training for PyTorch | <https://opacus.ai/> |
| TensorFlow Privacy | DP-SGD for TensorFlow | <https://github.com/tensorflow/privacy> |
| Adversarial Robustness Toolbox | attacks and defenses across frameworks | <https://adversarial-robustness-toolbox.readthedocs.io/> |
| CleverHans | adversarial-example reference implementations | <https://github.com/cleverhans-lab/cleverhans> |
| Foolbox | fast adversarial attacks on PyTorch/JAX/TF | <https://foolbox.readthedocs.io/> |
| TextAttack | adversarial attacks and augmentation for NLP | <https://textattack.readthedocs.io/> |
| Fairlearn | fairness metrics and mitigation | <https://fairlearn.org/> |
| AIF360 | IBM's fairness metrics and algorithms | <https://github.com/Trusted-AI/AIF360> |
| Microsoft Presidio | PII detection and de-identification | <https://microsoft.github.io/presidio/> |
| Garak | LLM vulnerability scanner | <https://github.com/NVIDIA/garak> |
| Captum | model interpretability for PyTorch | <https://captum.ai/> |

## Federated Learning

| Tool | One line | Docs |
|---|---|---|
| Flower | framework-agnostic federated learning | <https://flower.ai/docs/> |
| TensorFlow Federated | federated computations on TensorFlow | <https://www.tensorflow.org/federated> |
| NVIDIA FLARE | enterprise federated learning runtime | <https://nvflare.readthedocs.io/> — llms.txt: <https://nvflare.readthedocs.io/llms.txt> |
| FATE | industrial federated-learning platform | <https://github.com/FederatedAI/FATE> |
| FedML | federated and distributed ML platform | <https://github.com/FedML-AI/FedML> |
| OpenFL | Intel's federated-learning framework | <https://openfl.readthedocs.io/> |
| PySyft | remote and private data science | <https://github.com/OpenMined/PySyft> |
| SecretFlow | privacy-preserving computation and FL stack | <https://www.secretflow.org.cn/> |

## Gotchas

- SHAP covers Shapley-value model explanations — its row lives on the [tabular-and-automl](tabular-and-automl.md) page.
- LLM-app guardrails (Guardrails AI, NeMo Guardrails) are recorded with the LLM-application stack — see the [llm-applications](llm-applications.md) page; this page covers training- and audit-time concerns.
