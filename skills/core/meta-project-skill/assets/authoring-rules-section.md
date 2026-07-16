# Skill-Authoring Section

The document form of the project's skill-authoring rules, for projects
whose harness is the entrypoint alone (or that keep rules in the knowledge
base). Copy the block into the entrypoint or a knowledge document, fill
the placeholders, and delete what the team does not need.

````markdown
## Creating Project Skills

Skills live at `<skill root>`. Create one only for a recurring,
non-obvious procedure that is fragile, order-sensitive, or branchy — a
one-line rule belongs in this file, stable facts in the knowledge base.

- One concern per skill; directory name equals the `name` field.
- Description = the user requests that trigger it + the project
  condition + a "Not for" exclusion; never internal file names.
- Keep the body short: common path inline, rare branches in the skill's
  references behind load conditions; scripts non-interactive.
- State the skill's update trigger in its body, and revise the skill in
  the same change that alters what it depends on.
````
