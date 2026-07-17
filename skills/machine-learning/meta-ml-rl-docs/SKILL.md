---
name: meta-ml-rl-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  reinforcement-learning project to authoritative documentation entry
  points — algorithm and training frameworks (Stable-Baselines3,
  TorchRL, CleanRL, Tianshou, Acme, d3rlpy) and environments and
  simulators (Gymnasium, PettingZoo, MuJoCo, Isaac Lab, CARLA, Unity
  ML-Agents) — plus the discovery procedure (llms.txt probing, PyPI
  metadata, official org repos) for tools not listed. Use when a harness
  build must record where the docs live for a project that trains or
  evaluates RL agents or builds simulation environments. Not for
  choosing between tools or recommending one, and not for RLHF-style LLM
  post-training or the Ray ecosystem's RLlib.
---

# Reinforcement Learning Documentation Map

This skill produces the documentation entry points a harness build
records for a reinforcement-learning project. It expects a harness build
in progress and access to the target's dependency manifests. Per-tool
content is one line plus a URL — install commands and API details are
always fetched from the recorded entry point, never recalled from
memory — and nothing here is a recommendation: when the target lacks a
tool for a need, record the option list with URLs and leave the choice
to the user.

## Workflow

1. Detect the RL stack: dependency manifests and imports
   (`stable_baselines3`, `torchrl`, `tianshou`, `gymnasium`,
   `pettingzoo`, `mujoco`, `pybullet`), environment registrations, and
   simulator assets or configs.
2. Read [algorithms.md](references/algorithms.md) when the target
   implements or trains RL algorithms.
3. Read [environments.md](references/environments.md) when the target
   defines, wraps, or runs environments and simulators.
4. For every entry point about to be recorded, probe
   `<docs-root>/llms.txt` (then `llms-full.txt`) and prefer the
   plain-text index when present.
5. For tools the tables miss, or any URL that no longer resolves, follow
   [doc-discovery.md](references/doc-discovery.md).
6. Record each detected tool — name, one-line role, documentation entry
   point, and its llms.txt when present — wherever the harness keeps
   conventions.

Done when: every RL framework and environment the target actually uses
has a recorded, live documentation entry point, and nothing recorded
ranks or recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: algorithm-framework and
  simulator selection is the user's decision.
- Ray RLlib belongs to the Ray ecosystem's own documentation map — do
  not duplicate its entry from here.
- Legacy `gym` imports usually mean Gymnasium today — record Gymnasium's
  entry point and note the migration status, without prescribing it.
