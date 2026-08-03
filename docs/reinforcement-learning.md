---
title: Reinforcement Learning
description: RL algorithm and training frameworks, plus the environments and simulators agents train against.
tags: [machine-learning, rl, simulation]
---

# Reinforcement Learning

Fetch when the target implements or trains RL algorithms, or defines, wraps, or runs environments and simulators. Each entry is one line and a documentation entry point; fetch install commands and API details from the entry point, never from memory. No entry is a recommendation.

## Algorithm & Training Frameworks

| Tool | One line | Docs |
|---|---|---|
| Stable-Baselines3 | reliable PyTorch implementations of standard algorithms | <https://stable-baselines3.readthedocs.io/> |
| TorchRL | PyTorch-native RL primitives and training loops | <https://docs.pytorch.org/rl/> |
| CleanRL | single-file, reproducible algorithm implementations | <https://docs.cleanrl.dev/> |
| Tianshou | modular RL library on PyTorch | <https://tianshou.org/> |
| Acme | DeepMind's research agent components | <https://github.com/google-deepmind/acme> |
| Sample Factory | high-throughput asynchronous RL | <https://www.samplefactory.dev/> |
| d3rlpy | offline RL algorithms | <https://d3rlpy.readthedocs.io/> |

## Environments & Simulators

| Tool | One line | Docs |
|---|---|---|
| Gymnasium | the standard single-agent environment API | <https://gymnasium.farama.org/> |
| PettingZoo | multi-agent environment API | <https://pettingzoo.farama.org/> |
| Minari | offline-RL dataset standard | <https://minari.farama.org/> |
| MuJoCo | fast rigid-body physics for control | <https://mujoco.readthedocs.io/> |
| NVIDIA Isaac Lab | GPU-parallel robot learning on Isaac Sim | <https://isaac-sim.github.io/IsaacLab/> |
| Brax | differentiable physics in JAX | <https://github.com/google/brax> |
| DeepMind Control Suite | continuous-control benchmark tasks | <https://github.com/google-deepmind/dm_control> |
| PyBullet | Bullet-physics simulation for robotics RL | <https://pybullet.org/> |
| Habitat-Lab | embodied-AI simulation platform | <https://aihabitat.org/> |
| CARLA | autonomous-driving simulator | <https://carla.readthedocs.io/> |
| Unity ML-Agents | RL environments inside Unity | <https://github.com/Unity-Technologies/ml-agents> |
| ManiSkill | GPU-parallel robot manipulation benchmark | <https://maniskill.readthedocs.io/> |

## Gotchas

- Ray RLlib documents under Ray's shared docs root — see the [distributed-compute](distributed-compute.md) page.
- Legacy `gym` imports usually mean Gymnasium today — Gymnasium's entry point covers the migration status.
- CARLA and Isaac Lab install as applications, not pip packages — see their docs for setup.
