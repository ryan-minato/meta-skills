---
title: Tabular ML, AutoML & Interpretability
description: Classic ML and gradient boosting, model interpretability, and AutoML and hyperparameter-optimization libraries.
tags: [machine-learning, data-science, tabular]
---

# Tabular ML, AutoML & Interpretability

Fetch when the target trains classic models or boosted trees, explains model predictions, automates model selection, or tunes hyperparameters. Each entry is one line and a documentation entry point; fetch install commands and API details from the entry point, never from memory. No entry is a recommendation.

## Traditional ML, Boosting & Interpretability

| Tool | One line | Docs |
|---|---|---|
| scikit-learn | the standard classic-ML library | <https://scikit-learn.org/> |
| XGBoost | gradient-boosted trees | <https://xgboost.readthedocs.io/> |
| LightGBM | fast histogram-based boosting | <https://lightgbm.readthedocs.io/> |
| CatBoost | boosting with native categorical support | <https://catboost.ai/docs/> |
| NVIDIA RAPIDS cuML | scikit-learn-compatible ML on GPUs | <https://docs.rapids.ai/api/cuml/stable/> |
| River | online machine learning on streams | <https://riverml.xyz/> |
| Vowpal Wabbit | fast online and contextual-bandit learning | <https://vowpalwabbit.org/> |
| imbalanced-learn | resampling for imbalanced datasets | <https://imbalanced-learn.org/> |
| skrub | preparing messy tables for ML | <https://skrub-data.org/> |
| PyOD | outlier and anomaly detection | <https://pyod.readthedocs.io/> |
| SHAP | Shapley-value model explanations | <https://shap.readthedocs.io/> |
| LIME | local surrogate explanations | <https://github.com/marcotcr/lime> |
| InterpretML | glass-box models and explanation tools | <https://interpret.ml/> |

## AutoML & Hyperparameter Optimization

| Tool | One line | Docs |
|---|---|---|
| Optuna | define-by-run hyperparameter optimization | <https://optuna.readthedocs.io/> |
| AutoGluon | AutoML for tabular, multimodal, and time series | <https://auto.gluon.ai/> |
| FLAML | lightweight, cost-aware AutoML | <https://microsoft.github.io/FLAML/> |
| H2O AutoML | AutoML inside the H2O platform | <https://docs.h2o.ai/> |
| Ax | adaptive experimentation platform | <https://ax.dev/> |
| BoTorch | Bayesian optimization on PyTorch | <https://botorch.org/> |
| Hyperopt | distributed search over awkward spaces | <https://hyperopt.github.io/hyperopt/> |
| Microsoft NNI | neural architecture search and tuning toolkit | <https://nni.readthedocs.io/> |

## Gotchas

- Ray Tune documents under Ray's shared docs root — see the [distributed-compute](distributed-compute.md) page.
- KerasTuner documents with Keras — see the [deep-learning-frameworks](deep-learning-frameworks.md) page.
