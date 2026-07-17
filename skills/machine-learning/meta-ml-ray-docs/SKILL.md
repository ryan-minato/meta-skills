---
name: meta-ml-ray-docs
description: >-
  Disposable meta-skill (delete after the harness is built): maps a
  Ray-based project to authoritative documentation entry points — the
  Ray libraries under one docs root (Core, Data, Train, Tune, Serve,
  Serve LLM, RLlib) and the cluster layer (KubeRay, Anyscale) — plus a
  discovery procedure for tools not listed. Use when a harness build
  must record where the docs live for a project that depends on ray or
  deploys Ray clusters. Not for choosing between tools or recommending
  one, and not for non-Ray distributed training or serving stacks.
---

# Ray Ecosystem Documentation Map

This skill produces the documentation entry points a harness build
records for a project built on Ray. It expects a harness build in
progress and access to the target's dependency manifests and cluster
configs. Per-component content is one line plus a URL — install commands
and API details are always fetched from the recorded entry point, never
recalled from memory — and nothing here is a recommendation: when the
target lacks a component for a need, record the option list with URLs
and leave the choice to the user.

## Workflow

1. Detect the Ray footprint: the `ray` dependency and its extras
   (`ray[data]`, `ray[train]`, `ray[tune]`, `ray[serve]`,
   `ray[rllib]`), imports, `@ray.remote` in code, and cluster configs
   (RayCluster/RayJob/RayService manifests, `ray up` YAML, Anyscale
   configs).
2. Read [ray-libraries.md](references/ray-libraries.md) for the Ray
   libraries — one docs root covers Core, Data, Train, Tune, Serve,
   Serve LLM, and RLlib; record which components the target uses.
3. Read
   [kuberay-and-clusters.md](references/kuberay-and-clusters.md) when
   the target deploys Ray on Kubernetes or a managed platform.
4. For every entry point about to be recorded, probe
   `<docs-root>/llms.txt` (then `llms-full.txt`) and prefer the
   plain-text index when present.
5. For tools the tables miss, or any URL that no longer resolves, follow
   [doc-discovery.md](references/doc-discovery.md).
6. Record each detected component — name, one-line role, documentation
   entry point, and its llms.txt when present — wherever the harness
   keeps conventions.

Done when: every Ray component and cluster layer the target actually
uses has a recorded, live documentation entry point, and nothing
recorded ranks or recommends between tools.

## Gotchas

- Entry points only: never record versioned, deep, or `latest`-pinned
  URLs — details are fetched from the entry point at use time.
- This skill informs, it never chooses: whether the target should use
  Ray for a new need is the user's decision.
- "Ray AIR" is a retired umbrella name for the libraries, not a separate
  component — record the individual libraries the target uses.
- The same tool may appear in another domain skill's tables; record it
  once per harness, not once per skill.
