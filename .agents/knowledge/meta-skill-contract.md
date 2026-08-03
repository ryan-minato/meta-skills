# The Meta-Skill Contract

Read this before authoring, reviewing, renaming, or removing anything under
`skills/`, and before touching the marker. This file is the source of truth
for what a published meta-skill is and how it is identified and removed.

## Audience Model

A published skill is written for agents in **target projects**. Its only
channels to that audience are its frontmatter `description` and its body —
the target agent never sees this repository. Consequences:

- Assume the target project's conventions, never this repository's: no
  bilingual READMEs, no Linear workflow, no `just check` inside a published
  skill's instructions (the skill validator rejects repo-only names, check
  M5).
- **File isolation.** Installed skills lose every file outside their own
  directory. No relative link may escape the skill root (check L1), and no
  README may sit in a skill root (check S2).
- **Repository-only composition.** A skill may assume the `core` catalog is
  installed, and nothing else. Catalog installation is recommended but does
  not prove that a sibling skill is present. Every non-core dependency,
  including one in the same catalog, follows the dependency contract below;
  external-skill dependencies are forbidden.
- Catalog-level files (`CONTEXT.md` and the README pair) are never loaded
  in a target: skill-directory installers copy skill directories only, and
  the marketplace plugins ship the catalog directory but load only its
  `<name>/SKILL.md` directories. Write them for this repository's
  maintainers regardless — but never put anything there a target must act
  on, because nothing will read it.

## Skill Dependencies

Only dependencies on published skills in this repository are valid. A skill
with one or more non-core dependencies declares them twice:

```yaml
metadata:
  meta-skills.dependencies: "catalog/meta-skill catalog/meta-other-skill"
```

The metadata value is a space-separated string of source identifiers. Each
identifier names an existing `skills/<catalog>/<skill>/` directory; core
dependencies are implicit and must not be listed.

The same identifiers appear in a `## Meta-skill Dependencies` section in the
skill body, one backticked identifier per bullet with its purpose. The section
also instructs the target agent to use `core/meta-skill-discovery` to verify
the live target and learn how to install it. It never embeds an installation
command: centralizing commands prevents stale or unsafe copies from spreading
through the catalog. Omit both the metadata key and the section when there is
no non-core dependency.

The metadata is machine-checkable; the body is the portable fallback for
frameworks that ignore custom metadata. They must name the same set. A
dependency hidden in ordinary prose violates the contract even if its target
happens to be installed.

## The Marker

Every published skill's resolved `description` begins with the marker,
followed by one space (check M3):

```text meta-skill-marker
Disposable meta-skill (delete after the harness is built):
```

The marker is the one deliberate cross-audience channel: it tells the
target-project agent what these skills are, and it is simultaneously the
machine key the removal procedure matches on.

Identification is by **description, never by name or directory**. Installers
rename skills to avoid collisions, and the Agent Skills spec ties the `name`
field to the directory name, so both channels are unstable; the description
survives. The `meta-` directory prefix in this repository only groups the
file tree — it carries no contract.

## YAML Authoring Form

The marker starts with a letter, so it is a valid YAML plain scalar in every
style — no quoting or folding tricks are required. The recommended form:

```yaml
description: >-
  Disposable meta-skill (delete after the harness is built): scaffolds X
  for the new harness. Use when the user asks for Y. Not for Z.
```

Keep the marker on one physical line. Conformance is checked by parsing the
YAML and testing the **resolved** value, never by regex over raw frontmatter
text — folded scalars, quoting, and indentation would defeat raw matching.

## Who Carries It

The destination test: the marker belongs on exactly the files that will be
**installed artifacts in a target project** and must be found and deleted.

| File | Marker |
|---|---|
| every `skills/<catalog>/<skill>/SKILL.md` | required (check M3) |
| any SKILL.md outside `skills/` — this repository's own skills | forbidden (checks M3 and D2) |
| templates a meta-skill copies into the target's harness | forbidden — they must survive the cleanup |
| the authoring template's own frontmatter | required (check D3) — published skills are copied from it |

## Removal (Target Side)

The specification any removal implementation must satisfy:

1. Enumerate `<skill-root>/<name>/SKILL.md` at depth 2, parse each file's
   YAML frontmatter, and select those whose **resolved** description starts
   with the marker. Prose has no `description` field, so it cannot match.
2. Dry-run first: print the resolved path, name, and first description line
   of every match. That listing is what the human approves.
3. Require fresh, explicit confirmation. An earlier "build me a harness"
   request is not consent to delete.
4. Delete the matched skill directories; the removal skill deletes itself
   last.
5. Report what was deleted. Skip and report any unparsable frontmatter —
   never guess.

## Embedding The Literal

The marker appears verbatim only in: the `MARKER` constants in both
validators (`scripts/validate_repo.py` and `scripts/check_skill.py`), fences
tagged `text meta-skill-marker` (byte-checked against the constant, check
D1), the YAML authoring form above (near-miss-checked, also D1), and
published descriptions (check M3). Everywhere else, write "the marker" and
link here.

Changing the marker is the `sync-contract` skill's procedure — do not
improvise it from this file. It is a breaking change for already-installed
copies and needs explicit user sign-off.
