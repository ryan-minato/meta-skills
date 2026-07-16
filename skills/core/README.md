# core

[中文](README.zh.md)

The required set. Install every `core` skill into a target project before
asking an agent to build its harness, then add topic catalogs as the project
needs them.

These skills are **disposable**: once the harness is built and verified,
their own removal skill deletes them all.

```bash
npx skills add ryan-minato/meta-skills --skill <skill-name>
```

## Skills

| Skill | Description |
|---|---|
| [meta-harness-plan](meta-harness-plan/) | Plans, audits, or improves the project's agent harness on independent decision axes; produces the user-approved plan the other builders follow |
| [meta-agents-md](meta-agents-md/) | Creates or improves the AGENTS.md entrypoint and framework pointer files, offloading long architecture material behind section-locating pointers |
| [meta-knowledge-base](meta-knowledge-base/) | Builds the agent knowledge base: one consistent structure, per-type document seeds, and authoring rules deposited in skill or entrypoint form |
| [meta-project-skill](meta-project-skill/) | Creates or retrofits durable project skills from shaped skeletons, and deposits the project's skill-authoring rules for the agents that come after |
| [meta-harness-sync](meta-harness-sync/) | Installs bidirectional keep-current mechanisms — one per concern, in skill or entrypoint form — plus periodic entropy reclamation and the compromise-mode proposal rule |
| [meta-disposal](meta-disposal/) | Removes every installed meta-skill by its description marker: dry-run listing, fresh explicit confirmation, then deletion with itself last |
