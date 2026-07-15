# <project name>

<One or two sentences: what this project is, and what it is for. Written for
someone who has never seen it. If the project's purpose fits here, it does not
need a file of its own.>

## <The convention that gets broken most often>

<Start with what agents actually get wrong here, not with what is easiest to
write. If a correction has been typed into a chat more than once, it belongs at
the top of this file.>

## Conventions

<Every rule you want followed, including the ones the code already demonstrates.
A convention visible in the last forty commits still belongs here: inferring it
would take an agent two optional steps — go look, then generalise — and both
fail silently. If you would correct an agent for breaking it, it goes here.

What to leave out is facts an agent meets anyway ("this is a Django project"),
not rules it could in principle deduce.>

- **<Rule>.** <What to do, and the reason it exists. A rule whose reason is
  absent gets followed until it is inconvenient, then dropped.>

## Boundaries

<What an agent may do here, and what needs asking first. State the irreversible
and the outward-facing explicitly.>

- <Allowed without asking.>
- <Ask first.>
- <Never.>

## Checks

<The command that proves a change is sound, and when to run it. If there is no
such command, say so plainly — an honest gap is workable, a claimed check that
nobody runs is worse than nothing.>

```bash
<command>
```

## When To Read What

<The pointer table. This is the discovery mechanism for everything not on this
page: knowledge files do not announce themselves, so an unlisted one is
invisible. The wording of a condition decides whether it is ever followed —
"Changing the payment flow" beats "Payments".>

| Situation | Read |
|---|---|
| <A condition a reader can recognise they are in> | <path> |

## Keeping This Current

<One sentence, minimum: who updates this and when. Without it, this file is
accurate on the day it is written and decays from then on — and a stale rule is
worse than a missing one, because an agent that finds no rule asks, while an
agent that finds a wrong one proceeds.>
