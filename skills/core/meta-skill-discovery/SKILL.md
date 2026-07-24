---
name: meta-skill-discovery
description: >-
  Disposable meta-skill (delete after the harness is built): discovers the
  live catalogs and skills published by ryan-minato/meta-skills, filters them
  by catalog, and explains project or global installation. Use when choosing,
  locating, or installing these meta-skills, or when another meta-skill names
  a required catalog/skill. Not for discovering skills from other sources.
compatibility: Requires network access; installation requires the skills CLI or Claude Code.
---

# Meta-Skill Discovery

Discover only skills published by `ryan-minato/meta-skills`. Treat its live
default branch as the source of truth; do not substitute a remembered or
third-party inventory.

## Workflow

1. Fetch the live marketplace manifest from
   `https://raw.githubusercontent.com/ryan-minato/meta-skills/main/.claude-plugin/marketplace.json`.
   Read each plugin's `name` and `description` as the catalog inventory.
2. If the user supplied a catalog, require an exact manifest name. On an
   unknown name, show the valid catalogs and stop.
3. Ask before running a command that downloads or executes the skills CLI.
   With approval, list without installing:

   ```bash
   npx skills add ryan-minato/meta-skills --list
   npx skills add ryan-minato/meta-skills/skills/<catalog> --list
   ```

   Use the first form for every catalog, grouped by marketplace catalog, and
   the second for a catalog filter.
4. Present catalog, skill name, and description. Remove the common disposable
   marker from descriptions for readability, but do not otherwise rewrite
   them. If either live source fails, report which source failed and do not
   guess from memory.
5. When another meta-skill names a dependency, resolve the exact
   `catalog/skill`, confirm it appears in the live result, and show the user
   what is missing before discussing installation.

Done when: every result came from the live repository, the requested filter
was applied exactly, and any missing or failed lookup was reported.

## Installation

Recommend catalog installation, but never infer that every skill in a catalog
is installed. Install `core` at the same scope before any topic catalog or
individual topic skill.

For the skills CLI, project scope is the default:

```bash
npx skills add ryan-minato/meta-skills/skills/<catalog>
npx skills add ryan-minato/meta-skills/skills/<catalog> --skill <skill-name>
```

Add `--global` to either command for a global installation:

```bash
npx skills add ryan-minato/meta-skills/skills/<catalog> --global
npx skills add ryan-minato/meta-skills/skills/<catalog> --skill <skill-name> --global
```

For Claude Code, each catalog is one plugin. Project scope is shared through
the repository; user scope is global:

```bash
claude plugin marketplace add ryan-minato/meta-skills
claude plugin install <catalog>@meta-skills --scope project
claude plugin install <catalog>@meta-skills --scope user
```

Before any install, show the exact command, scope, selected catalog or skill,
and every declared dependency; require fresh confirmation before running it.
For a global install, warn that these disposable skills will load across
projects and must be removed globally after the harness work is complete.

Plugin-managed installs must be removed with `claude plugin uninstall` at the
matching scope. Skills CLI global installs must be removed with
`npx skills remove --global`; copied project skills use the disposal workflow.

## Gotchas

- A catalog install is a recommendation, not evidence that any particular
  sibling skill exists in the active session.
- Never search for or install a dependency outside
  `ryan-minato/meta-skills`; another meta-skill may depend only on this
  repository's catalog/skill identifiers.
- Listing is read-only, but `npx` may download executable code. Obtain
  approval before running it.
