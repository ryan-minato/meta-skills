---
name: meta-ml-trustworthy-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  trustworthy-ML project to authoritative documentation entry points —
  privacy, adversarial robustness, fairness, and interpretability
  (Opacus, Adversarial Robustness Toolbox, Fairlearn, Presidio, Garak,
  Captum, SHAP) and federated learning (Flower, TensorFlow Federated,
  NVIDIA FLARE, FATE, OpenFL, SecretFlow). Use when a harness build must
  record where the docs live for a project that handles differential
  privacy, adversarial testing, fairness auditing, PII redaction, or
  federated training. Not for choosing between tools or recommending
  one, and not for general model evaluation or security outside ML.
---

# Trustworthy & Federated ML Documentation Map

This skill produces the documentation entry points a harness build
records for a project working on privacy, robustness, fairness, or
federated learning. It expects a harness build in progress and access to
the target's dependency manifests. Per-tool content is one line plus a
URL — install commands and API details are always fetched from the
recorded entry point, never recalled from memory — and nothing here is a
recommendation: when the target lacks a tool for a need, record the
option list with URLs and leave the choice to the user.

## Workflow

1. Detect the trustworthy-ML stack: dependency manifests and imports
   (`opacus`, `art`, `foolbox`, `textattack`, `fairlearn`, `aif360`,
   `presidio`, `garak`, `captum`, `shap`, `flwr`, `nvflare`, `openfl`,
   `secretflow`), privacy budgets in configs, and federated deployment
   manifests.
2. Read
   [privacy-and-robustness.md](references/privacy-and-robustness.md)
   when the target trains with differential privacy, tests adversarial
   robustness, audits fairness, redacts PII, or explains models.
3. Read [federated-learning.md](references/federated-learning.md) when
   the target trains across parties without centralizing data.
4. For every entry point about to be recorded, prefer an agent-oriented
   rendition: a page's `.md` source, then `<docs-root>/llms.txt` (a
   compact index). Fall back to `llms-full.txt` only when neither
   exists, and never read it whole — it is the whole site as one
   file; search it programmatically.
5. Record each detected tool the tables cover — name, one-line role,
   documentation entry point, and its llms.txt when present — wherever
   the harness keeps conventions.

Done when: every privacy, robustness, fairness, and federated tool the
target actually uses has a recorded, live documentation entry point, and
nothing recorded ranks or recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: privacy-mechanism and framework
  selection is the user's decision.
- These are training-time and audit-time libraries — LLM-app guardrails
  live with the application stack, not here.
- The same tool may appear in another domain skill's tables (SHAP also
  serves tabular interpretability); record it once per harness, not
  once per skill.
- Tools this skill does not list are out of scope — leave finding their
  docs to the agent; it is not this skill's job.
