---
name: meta-skill-discovery
description: >-
  Disposable meta-skill (delete after the harness is built): discovers the
  live catalogs and skills published by ryan-minato/meta-skills, filters them
  by catalog, and explains project or global installation. Use when choosing,
  locating, or installing these meta-skills, or when another meta-skill names
  a required catalog/skill. Not for discovering skills from other sources.
compatibility: Requires Python 3.11+ and network access; installation requires the skills CLI or Claude Code.
---

# Meta-Skill Discovery

Discover only skills published by `ryan-minato/meta-skills`. Treat its live
default branch as the source of truth; do not substitute a remembered or
third-party inventory.

## Workflow

1. Run the bundled [discovery script](scripts/discover.py). It downloads one
   live repository snapshot, reads only the marketplace inventory and its
   explicitly listed skills, and emits compact JSON without installing
   anything:

   ```bash
   python3 scripts/discover.py
   ```

2. Filter only through the script. Use `--full` when the complete marker-free
   description is needed:

   ```bash
   python3 scripts/discover.py --catalog <catalog> --full
   python3 scripts/discover.py --skill <catalog>/<skill> --full
   ```

   An unknown catalog or skill reports the valid choices and returns no
   guessed result.
3. For every complete description in one run, add `--full --output <path>`;
   read the JSON file and remove it after presenting the result. The default
   output stays below common tool-output limits by returning deterministic
   skill summaries.
4. Present the catalog name and description plus each requested skill name
   and summary or full description. If the script fails, report its reason
   and do not substitute memory, a cached inventory, or another registry.
5. When another meta-skill names a dependency, query its exact
   `catalog/skill`, confirm the script returned it, and show what is missing
   before discussing installation.

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
- Discovery reads one live repository archive in memory and never extracts or
  caches it. Do not replace the bundled script with ad hoc repository or
  registry searches.
