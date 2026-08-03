# core

[中文](README.zh.md)

The required set. Install `core` into a target project before asking an agent
to build its harness, then preferably add topic catalogs as the project needs
them. Only core may be assumed present; catalog installation never proves a
non-core sibling is available.

These skills are **disposable**: once the harness is built and verified,
their own removal skill deletes them all.

```bash
claude plugin marketplace add ryan-minato/meta-skills   # once per machine
claude plugin install core@meta-skills --scope project
# or via the skills CLI (the catalog path scopes discovery):
npx skills add ryan-minato/meta-skills/skills/core
npx skills add ryan-minato/meta-skills/skills/core --skill <skill-name>
```

## Skills

| Skill | Description |
|---|---|
| [meta-skill-discovery](meta-skill-discovery/) | Discovers the repository's live catalogs and skills, filters by catalog, and centralizes project/global installation guidance |
| [meta-harness-plan](meta-harness-plan/) | Plans, audits, or improves the project's agent harness on independent decision axes; produces the user-approved plan the other builders follow |
| [meta-agents-md](meta-agents-md/) | Creates or improves the AGENTS.md entrypoint and framework pointer files, offloading long architecture material behind section-locating pointers |
| [meta-knowledge-base](meta-knowledge-base/) | Builds the agent knowledge base: one consistent structure, per-type document seeds, and authoring rules deposited in skill or entrypoint form |
| [meta-project-skill](meta-project-skill/) | Creates or retrofits durable project skills from shaped skeletons, and deposits the project's skill-authoring rules for the agents that come after |
| [meta-harness-sync](meta-harness-sync/) | Installs bidirectional keep-current mechanisms — one per concern, in skill or entrypoint form — plus periodic entropy reclamation and the compromise-mode proposal rule |
| [meta-disposal](meta-disposal/) | Removes every installed meta-skill by its description marker: dry-run listing, fresh explicit confirmation, then deletion with itself last |
