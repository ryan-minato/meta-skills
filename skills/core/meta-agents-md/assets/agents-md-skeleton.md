# <project name>

<Two or three sentences: what this project is and what agents are expected
to do in it. No welcome prose.>

## Conventions

- <language / style rule agents must follow>
- <naming or structure rule>
- <commit / branch rule, if the team has one>

## Commands

| Command | Does |
|---|---|
| `<build command>` | <what it builds> |
| `<test command>` | <what it verifies> |
| `<lint / check command>` | <what it enforces> |

## Checks Before Proposing Changes

1. <the gate that must pass>
2. <what to self-review in the diff>

## Architecture

<One paragraph at most. Offload detail to the architecture document and
leave a section-locating pointer: a link to the file plus the target
heading in inline code, byte-exact, hashes included.>

## When To Read What

| Situation | Read |
|---|---|
| <working on X> | `<knowledge file path>` |

## Safety Limits

- <what agents must never do without asking>
- <files or directories agents must not touch>
