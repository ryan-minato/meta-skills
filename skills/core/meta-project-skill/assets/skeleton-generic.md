# Generic Skill Skeleton

For procedures that fit none of the shaped skeletons. Copy the block into
a new skill directory, then rework it; if it starts growing branches or
gates, switch to the diagnosis or validation skeleton instead.

````markdown
---
name: <kebab-case-name>
description: >-
  <What this does in this project, one sentence.> Use when <the user
  request or project condition>. Not for <exclusion>.
---

# <Skill Title>

<One paragraph: what this produces and the state it expects to start
from.>

## Workflow

1. <step>
2. <step>

Done when: <observable completion criterion>.

## Gotchas

- <the failure mode worth preventing>

Update this skill in the same change that alters what the steps above
depend on.
````
