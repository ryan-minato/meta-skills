---
name: meta-ml-probabilistic-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  probabilistic-modeling project to authoritative documentation entry
  points — probabilistic programming and Bayesian inference (PyMC, Stan,
  Pyro, NumPyro, TensorFlow Probability, BlackJAX, ArviZ) and causal
  inference (DoWhy, causal-learn, EconML, CausalML, DoubleML,
  Tigramite) — plus the discovery procedure (llms.txt probing, PyPI
  metadata, official org repos) for tools not listed. Use when a harness
  build must record where the docs live for a project that does Bayesian
  modeling, MCMC, or causal inference. Not for choosing between tools or
  recommending one, and not for frequentist statistics or general ML.
---

# Probabilistic & Causal Documentation Map

This skill produces the documentation entry points a harness build
records for a project doing Bayesian modeling or causal inference. It
expects a harness build in progress and access to the target's
dependency manifests. Per-tool content is one line plus a URL — install
commands and API details are always fetched from the recorded entry
point, never recalled from memory — and nothing here is a
recommendation: when the target lacks a tool for a need, record the
option list with URLs and leave the choice to the user.

## Workflow

1. Detect the modeling stack: dependency manifests and imports (`pymc`,
   `cmdstanpy`, `pyro`, `numpyro`, `tensorflow_probability`,
   `blackjax`, `arviz`, `dowhy`, `econml`, `causalml`, `doubleml`),
   Stan model files (`.stan`), and inference outputs (trace files).
2. Read
   [probabilistic-programming.md](references/probabilistic-programming.md)
   when the target builds Bayesian models or runs MCMC/variational
   inference.
3. Read [causal-inference.md](references/causal-inference.md) when the
   target estimates causal effects or discovers causal structure.
4. For every entry point about to be recorded, probe
   `<docs-root>/llms.txt` (then `llms-full.txt`) and prefer the
   plain-text index when present.
5. For tools the tables miss, or any URL that no longer resolves, follow
   [doc-discovery.md](references/doc-discovery.md).
6. Record each detected tool — name, one-line role, documentation entry
   point, and its llms.txt when present — wherever the harness keeps
   conventions.

Done when: every probabilistic and causal library the target actually
uses has a recorded, live documentation entry point, and nothing
recorded ranks or recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: PPL and estimator selection is
  the user's decision.
- The same tool may appear in another domain skill's tables (PyMC and
  ArviZ also serve statistical analysis); record it once per harness,
  not once per skill.
