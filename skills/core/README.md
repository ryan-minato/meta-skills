# core

[中文](README.zh.md)

The required set. Install every `core` skill into a target project before asking
an agent to build its harness, then add topic catalogs as the project needs them.

These skills are **disposable**: once the harness is built and verified, remove
them.

```bash
npx skills add ryan-minato/meta-skills --skill <skill-name>
```

## Skills

Listed in the order a build uses them.

| Skill | Description |
|---|---|
| `meta-harness-plan` | Works out what the project needs before anything is written — and what it does not. Reads what the repository already shows, asks about what it cannot, and settles the build. |
| `meta-agents-md` | Writes the entrypoint: what belongs on the always-loaded page, what moves behind a pointer, and the when-to-read table that makes the rest findable. |
| `meta-knowledge-file` | Creates the files the entrypoint points at — goal, plan, quality, workflow, reference — and decides which are one file and which are a folder. |
| `meta-framework-wiring` | Wires the harness into the agents the team actually uses. Which file each reads first, where skills and MCP config go, what hooks exist. Fetches the vendor's docs rather than trusting notes. |
| `meta-project-skill` | Turns the procedures worth capturing into the project's own durable skills — without letting them inherit the marker that would delete them at cleanup. |
| `meta-harness-maintenance` | Builds what keeps the harness true once nobody is watching: realigning facts duplicated across files, and pruning what has gone stale. |
| `meta-disposal` | Removes the meta-skills once the harness is built and verified. Dry-runs first, asks before deleting, and takes itself last. |
