# core — Catalog Context

Rules, notes, and references that apply only to skills in this catalog.
Repository-wide standards live in
[meta-skill-contract.md](../../.agents/knowledge/meta-skill-contract.md).

Read this before adding or changing anything in `skills/core/`.

## Goal

`core` is the required set. A user installs every `core` skill before asking an
agent to build a target project's harness, then adds topic catalogs as the
project needs them. Together, `core` must be enough to take any project from no
harness to a working one.

## Constraints

- **Disposable only.** A skill belongs here only if it is one-time scaffolding a
  target project discards after harness setup. A durable, general design aid
  belongs in the sibling repository `ryan-minato/skills` instead — that is the
  product boundary, and the marker is the admission test. If a skill should not
  carry the marker, it does not belong in this repository.
- **Stack-agnostic.** `core` loads for every harness build, so a skill here must
  be useful regardless of the target's language, framework, or platform. If it
  only helps certain kinds of projects, it belongs in a topic catalog.
- **Tightly scoped descriptions.** Every `core` skill loads into every harness
  build at once. A description that triggers on unrelated work pollutes every
  target project simultaneously.
- **Cheap to carry.** Keep `SKILL.md` bodies short and push long material into
  `references/`, which loads only when its condition fires.
- **Self-contained.** Installed skills lose everything outside their own
  directory. No relative link may escape the skill root, and no skill may depend
  on a sibling's behavior. To build on another skill, instruct the user to
  install it rather than linking to it.

## The Marker

Every skill in this catalog carries the marker. Copy this authoring form verbatim
and edit only the text after it:

```yaml
description: >
  [META-SKILL: remove after harness setup]
  Designs ... Use when ... Not for ...
```

Copy from the fenced block above, never from rendered documentation — rendered
text introduces U+00A0 and smart quotes, which are invisible on screen and fatal
to a byte-exact match.

The YAML fold turns the line break into the required trailing space. Never type
that space, and never leave a blank line after the marker. A plain scalar
(`description: [META-SKILL: ...`) is invalid YAML, because `[` opens a flow
sequence.

## References

- Agent Skills specification — reachable through the `agentskills` MCP server.
- Sibling repository, the durable side of the product boundary —
  <https://github.com/ryan-minato/skills>
