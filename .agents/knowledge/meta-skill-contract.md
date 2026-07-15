# Meta-Skill Contract

Load this when authoring, reviewing, renaming, or removing any skill under
`skills/`, or when changing how meta-skills are identified or removed.

## Source Of Truth

This file is the source of truth for the marker contract. Other places repeat
the marker literal and must be updated with it: the Core Conventions line in
[AGENTS.md](../../AGENTS.md), the `MARKER` constant in
[check_skill.py](../../scripts/check_skill.py) and
[validate_repo.py](../../scripts/validate_repo.py), each catalog's `CONTEXT.md`,
and the public READMEs. The `sync-contract` skill owns that alignment and
carries the authoritative inventory. Do not restate that inventory as a count
here: a number drifts the moment a copy is added, which is how `validate_repo.py`
went unlisted for as long as it did.

## What A Meta-Skill Is

A meta-skill is **one-time scaffolding**. Its lifecycle:

1. A user copies a catalog into a target project's skill directory.
2. The user hands the target project's requirements to an agent.
3. The agent invokes the meta-skills to build that project's harness.
4. Once the harness is verified, the agent **deletes the meta-skills**.

This inverts the usual assumption that a skill is durable. Everything below
follows from step 4: a meta-skill must be findable in order to be removed, and
must leave nothing behind that depends on it.

## The Marker

Every published skill's resolved `description` begins with exactly this
41-character, pure-ASCII string — note the **trailing space**:

```text
[META-SKILL: remove after harness setup]·
```

The `·` above stands for that trailing space; it is written as a visible
placeholder because a real trailing space cannot survive in this file (the
`trailing-whitespace` hook strips it). Authors never type the space anyway — see
the YAML form below, where the fold supplies it. Copy the **authoring form**,
not this line.

### Identification is by description, never by name

Installers rename skills to avoid collisions in target projects, so the name
channel cannot be trusted. The `description` is what agents always see in the
skill listing, and it survives installation. The `meta-` name prefix only groups
skills in the file tree and carries **no contract**.

The name may still serve as an *advisory* hint: a cleanup dry-run may surface
`meta-*` directories that lack the marker as "possible meta-skill, marker
missing — confirm?". Name is a hint for a human; description is authority for
the machine.

### The YAML form is mandatory, not stylistic

`[` opens a YAML flow sequence, so the natural-looking plain scalar is **invalid
YAML**:

```yaml
description: [META-SKILL: remove after harness setup] Designs ...
```

That raises `ParserError: while parsing a block mapping`, which does not mention
the real cause. Use a folded scalar:

```yaml
description: >
  [META-SKILL: remove after harness setup]
  Designs ... Use when ... Not for ...
```

Three rules that follow, each verified against the YAML parser:

- **Never type the trailing space.** The fold turns the line break into exactly
  one space. A literal trailing space is also unstable here: the
  `trailing-whitespace` hook strips it.
- **Never leave a blank line after the marker.** It folds to `\n`, not a space,
  and the value no longer starts with the marker.
- **A folded scalar re-wraps lines**, so the marker may legally span a line
  break and still resolve correctly. Conformance is therefore **parse the YAML,
  then test the resolved value** — never a regex over raw file text.

### Copy the marker from a fenced block

Copy it from the fenced block in the catalog's `CONTEXT.md`, never from rendered
documentation. Rendered text is how U+00A0, smart quotes, and en-dashes get in.
They are invisible on screen, fatal to a byte-exact match, and leave the author
believing the skill is marked.

## Who Carries The Marker

The test is **destination, not location**: will this description ship into a
target project as a disposable meta-skill?

| Path | Marker | Why |
|---|---|---|
| `skills/<catalog>/<skill>/SKILL.md` | **Required** | Published; must be findable for removal |
| `.agents/skills/**` | **Forbidden** | This repo's own durable skills |
| Harness files a meta-skill generates into a target | **Forbidden** | The deliverable must survive |
| `assets/` templates for generated artifacts | **Forbidden** | See failure 2 below |
| Prose docs quoting the marker | N/A | No `description` field; structurally exempt |

An `assets/` template for authoring *a new meta-skill in this repo* should carry
it. Apply the destination test.

### Why wrong inheritance is dangerous

Three distinct failures, worth keeping separate:

1. **Self-destruct.** If this repo's `.agents/skills/` carried the marker, a
   cleanup pass run inside this repo would delete this repo's own harness.
2. **Harness erasure.** A meta-skill's job is to emit durable project files. If
   a template inside it carries a live marker and an agent copies it verbatim,
   the *generated harness inherits the marker and deletes itself at cleanup* —
   silently, right after the build reports success.
3. **Trust collapse.** One over-broad deletion and users stop running cleanup
   at all. Meta-skills then persist forever, which is exactly the context bloat
   this repo exists to remove. The disposal contract only works if it is never
   scary.

## Disposability Consequences

- Whatever a meta-skill produces must stand on its own. Nothing durable in the
  target may reference the meta-skill, its files, or its name.
- Installed skills lose everything outside their own directory. No relative link
  may escape the skill root, and no skill may depend on a sibling skill's
  behavior. To build on another skill, instruct the user to install it rather
  than linking to it.
- Keep `README.md` out of a skill root; it ships to targets and earns nothing.

## Writing The Description

Every meta-skill shares an identical 41-character opening, which costs
discriminative power exactly where it is scarcest — meta-skills are mutually
similar by construction. Compensate:

- The first word after the marker is the distinctive action verb or domain noun.
  Never `This`, `A`, or `Helps`.
- Front-load what no *other meta-skill* does, in the first ~15 words. Assume
  everything before it was clipped by a truncating listing.
- Add `Use when ...` with concrete phrases a user would really say.
- Add a negative boundary (`Not for ...`).
- The budget is 1024 characters on the resolved value, of which the marker takes
  41. Length warnings compare against the marker-stripped value.

## Removal

Removal is a target-side procedure and therefore travels inside the shipped
disposal meta-skill, not in this repo: target agents cannot read
`.agents/knowledge/`. This section fixes the requirements that procedure must
meet.

- **Discovery is never a recursive grep.** This repo's own docs contain the
  marker literal. Enumerate only `<skill-root>/<name>/SKILL.md` at depth 2, then
  match the parsed `description` field. Prose has no `description`, so it cannot
  match.
- **Gate on the harness's own verification**, not on an agent's judgment that it
  is done.
- **Dry-run first**, listing resolved paths and each skill's first description
  line. That listing is what the human approves.
- **Require fresh confirmation.** An earlier "build me a harness" request is not
  consent to delete.
- **Reject symlinks and path escapes.** Resolve each candidate and require it to
  stay under the skill root. If a candidate is itself a symlink, unlink it only
  — never recurse through it into a shared or global install.
- **Check for dangling pointers** before deleting: scan surviving harness files
  for references to the skill. A harness pointing into a deleted directory is
  worse than no cleanup.
- **Delete the skill directory**, not just `SKILL.md`; orphaned `scripts/` is
  garbage.
- **Scope to the project skill root only** — never a global or user-level root.
- **Verify afterwards** that no marker remains, and be idempotent: zero markers
  found is "nothing to do", not an error.
- The disposal skill is itself marked and deletes itself **last**. This is safe
  because its `SKILL.md` is already in context by then; removing the file does
  not abort the run.

## Gotchas

- A near-miss marker is worse than no marker: cleanup will not find the skill,
  but the author believes it is marked. The validator's codepoint diff exists
  for this.
- The description channel is best-effort, not guaranteed. An installer that
  rewrites descriptions breaks it the same way renaming broke the name channel.
  State this honestly rather than implying the contract is airtight.
- A skill that should not carry the marker does not belong in this repo. The
  marker is the admission test; durable design aids belong in
  `ryan-minato/skills` instead.
