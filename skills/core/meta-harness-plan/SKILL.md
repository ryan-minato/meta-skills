---
name: meta-harness-plan
description: >
  [META-SKILL: remove after harness setup]
  Plans a project's agent harness before any file is written: records which
  meta-skills are installed, inventories the harness that already exists, asks
  the user for the decisions a codebase cannot show — how much rigour, how much
  agent autonomy, which agent frameworks to serve — and settles what gets built
  in what order. Use when a project has no agent harness and someone asks to set
  one up, bootstrap agent instructions, or make a repo work with coding agents;
  run it before anything else. Not for auditing a harness that already works,
  and not for writing the harness files themselves.
---

# Harness Planning

A harness is everything agent-visible that helps agents meet expectations here:
the entrypoint, the knowledge they can reach, the checks they can run, the
boundaries on what they may do. This decides **what this project needs** — and,
just as often, what it does not.

Nothing here is written down as a plan document. **The harness is the plan**,
materialised. A separate decision file would restate what the entrypoint and
knowledge files already say, drift from them, and need its own upkeep.

This skill writes exactly one file, and that file gets deleted at cleanup.

## Step 0 — Record the manifest, before anything else

**Do this first, before writing a single harness file.**

List the skill directories already installed, and record each one: its
directory name, whether its resolved `description` currently begins with the
removal marker, and that description's first line. Write it to
`META-SKILL-MANIFEST.md` in the skill root, following
[meta-skill-manifest.md](assets/meta-skill-manifest.md).

Right now is the only moment this list is unambiguous. Everything present is
scaffolding somebody installed for this job. The moment the build starts,
skills begin appearing that this project **owns and must keep**, and from then
on nothing on disk distinguishes them except the marker — which is exactly the
thing that can be wrong. A snapshot taken now turns cleanup from guesswork into
a comparison.

The file is scaffolding, not harness: it names meta-skills, so it is deleted at
cleanup along with them. Nothing durable may point at it.

## Step 1 — Read what the project already shows

Look before you ask. Inventory:

- **Entry files** — `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
  `GEMINI.md`, `.cursorrules`. Which exist, what they say, whether they agree.
- **Skill and agent directories** — is anything installed beyond the
  scaffolding?
- **MCP configuration** — any already wired.
- **Checks** — tests, linters, formatters, CI workflows, hook configs. Note
  the commands, and whether they actually pass right now.
- **Conventions in the git history** — commit style, branch names, whether pull
  requests are used.
- **Docs** — README, CONTRIBUTING, architecture notes. Whatever is already
  written is knowledge you do not have to ask for.

## Step 2 — Ask about what the project cannot show

The project shows it clearly → **do not ask.** Nobody wants to be quizzed on
facts written in their own README.

But **"I can read it" is not "I read it clearly."** When the evidence is thin,
stale, or self-contradictory, ask. Do not settle it by inference:

- A test directory with sparse coverage — do they value tests, or did they try
  once and give up?
- One CI job that only lints — a deliberate minimal gate, or an unfinished one?
- An entry file that reads like an unedited template — a live convention, or
  leftover?
- `AGENTS.md` **and** `CLAUDE.md` both present, disagreeing — **which one is
  authoritative?** Never guess this one. Frameworks genuinely differ in which
  file they read, so the wrong guess writes rules into a file the team's tool
  never opens.

**The cost is lopsided, which is why the bias is toward asking.** A question
costs one round trip. A wrong guess gets welded into the harness as a false
premise — and these meta-skills are deleted once the build is done, so nothing
survives that can re-derive it. The user just lives with it. When in doubt, ask.

Cover, at minimum:

1. **What this project is, and what a mistake costs.** A rerun, or something
   expensive?
2. **Who works here** — solo or team, and whether conventions are currently
   unwritten.
3. **How much agents do here**, and what they must never do without asking.
4. **Which agent frameworks the team actually uses.** Never infer this from a
   stray config directory; an empty `.claude/` proves somebody tried it once.
5. **What proves the project is healthy** — the command the cleanup step will
   gate on.

Ask **only** for what changes the plan. Carry a default into every question so
it can be skipped. Never invent automation nobody requested.

For a brownfield project, a team codebase, or anywhere the list above is not
enough, work through [the question bank](references/interview.md).

### Two ways to ask, depending on where you are running

- **You can ask the user** — interactively, or simply in conversation: ask in
  small batches, so their answers can steer what you ask next.
- **You cannot ask** — a batch job, a hook, a non-interactive run: put **every
  question in one block**, each with its default, and let the user answer in a
  single pass.

What you must never do is assume an answer because asking was inconvenient. If
you cannot ask and cannot proceed honestly, say so and stop.

## Step 3 — Choose how much harness to build

Match the depth to the answers, and **stop at the lowest rung that solves the
real problem**. Every layer costs context in every future session and has to be
kept true; a harness nobody maintains misleads faster than no harness at all.

| Build | When | Cost |
|---|---|---|
| **An entrypoint, and nothing else** | Solo, low stakes, few conventions | One file to keep true. Most projects start here, and many should stop here |
| **+ knowledge files** | The entrypoint would run past ~100 lines, or material is only relevant sometimes | Each file needs a load condition and a reason to exist |
| **+ documented checks** | Agents must be able to prove their own work | Only worth it if the checks actually run and pass |
| **+ project skills** | Procedures that repeat, are easy to get wrong, or must happen in order | Each is permanently in the skill listing |
| **+ maintenance mechanisms** | Facts duplicated across files that will drift, or a tree large enough to rot | Real upkeep; only pays once there is something to keep aligned |

Two failure modes, and the second is the common one:

- **Too thin**: agents keep missing conventions, and the same correction gets
  typed every session.
- **Too thick**: nobody maintains it, it goes stale, and agents follow stale
  rules confidently. **Stale is worse than absent** — an agent that finds no
  rule asks, while an agent that finds a wrong one proceeds.

Prefer one shared entry file over per-framework configuration whenever the team
uses more than one tool, or might.

## Step 4 — Agree the build with the user

Before anything gets written, say plainly:

- which artifacts you will create, in what order;
- which frameworks they serve;
- what will **not** be built, and why — this is the useful half, and the half
  that gets skipped;
- the command that will prove the harness works;
- who keeps it current.

Get agreement, then build. This is a conversation, not a document: what makes
these decisions durable is the harness you are about to write, not a record of
having decided them.

## Gotchas

- **No harness file may name a meta-skill.** Not the entrypoint, not a knowledge
  file, not a generated skill. Name artifacts and commands instead. A durable
  file pointing at scaffolding becomes a dangling pointer the moment cleanup
  runs — and cleanup will stop, correctly, rather than break it. The manifest is
  the sole exception, and it is deleted too.
- **Do not skip step 0 because the build feels urgent.** The manifest cannot be
  reconstructed later; that is the entire reason it is taken first.
- **A rule nobody asked for is a rule nobody follows.** The strongest material
  in any harness comes from the answer to "what has an agent already got wrong
  here?" — one concrete correction beats a page of principles.
- **A rule the project already demonstrates still gets written down.** The
  entrypoint is the only guaranteed-load position; inferring the same rule from
  the history needs the agent to go looking and then to generalise, and either
  step can silently not happen. Consistency in the history is the reason a rule
  is worth stating, not a reason to omit it. What to leave out is *facts* an
  agent meets on its own, never *rules* you would correct it for breaking.
