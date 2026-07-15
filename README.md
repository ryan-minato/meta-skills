# meta-skills

[中文](README.zh.md)

Disposable meta-skills that help an agent build a durable **harness** in your
project — and then get out of the way.

A harness is everything agent-visible that helps agents meet your expectations:
the environment they run in, the constraints on what they produce, the tools they
can call, and the knowledge they can reach. Building a good one is a skill in
itself. That is what these skills carry.

They are the inverse of a normal skill library: they are designed to delete
themselves.

## How it works

1. **Install** the `core` catalog into your project, plus any topic catalogs that
   fit your stack.
2. **Ask** — hand your project's requirements and conventions to an agent and ask
   it to build a harness.
3. **Build** — the agent invokes the meta-skills, which encode the practices.
4. **Remove** — once the harness is built and you have verified it, ask the agent
   to remove the meta-skills. They have done their job, and every skill left
   installed costs context in every future session.

Removal is confirmation-gated by design: an earlier request to build a harness is
never treated as consent to delete anything.

## Catalogs

| Catalog | Contents | Install scope |
|---|---|---|
| [core](skills/core/) | The required set: enough to take any project from no harness to a working one | Per project, before a harness build |

## Installation

```bash
npx skills add ryan-minato/meta-skills                      # interactive
npx skills add ryan-minato/meta-skills --skill <skill-name>
```

Install these **per project**, not globally. They are scaffolding for one job in
one project, and a global install would follow you into projects that already
have a harness.

## How a meta-skill identifies itself

Every published skill's description begins with a marker:

```text
[META-SKILL: remove after harness setup]
```

That marker is how an agent finds these skills again in order to remove them.
Identification is by **description, not by name**, because installers rename
skills to avoid collisions — the `meta-` name prefix only groups them in the file
tree.

## Related

The sibling library [ryan-minato/skills](https://github.com/ryan-minato/skills)
ships **durable** skills, including `meta-harness`, a general design aid that
stays installed. This repository ships the disposable, per-project builders. Both
are useful together.

## Contributing

Start at [AGENTS.md](AGENTS.md), then [ARCHITECTURE.md](ARCHITECTURE.md). Run
`just setup` once, and `just check` before committing.

## License

[Apache-2.0](LICENSE)
