# meta-skills

[中文](README.zh.md)

Disposable meta-skills that help an agent build a durable **harness** in
your project — and then get out of the way.

A harness is everything agent-visible that helps agents meet your
expectations: the environment they run in, the constraints on what they
produce, the tools they can call, and the knowledge they can reach. Building
a good one is a skill in itself; that is what these skills carry. They are
the inverse of a normal skill library: they are designed to delete
themselves.

## How It Works

1. **Install** the `core` catalog into your project's skill directory (for
   example `./.agents/skills/`), plus any topic catalogs that fit your
   stack.
2. **Ask** — hand your project's requirements and conventions to an agent
   and ask it to build a harness.
3. **Build** — the agent invokes the meta-skills, which encode the
   practices.
4. **Remove** — once the harness is built and verified, the agent finds
   every meta-skill by its marker and deletes them all. They have done their
   job, and every skill left installed costs context in every future
   session.

Removal is confirmation-gated by design: an earlier request to build a
harness is never treated as consent to delete anything.

## How A Meta-Skill Identifies Itself

Every published skill's description begins with the marker:

```text meta-skill-marker
Disposable meta-skill (delete after the harness is built):
```

The marker is how an agent finds these skills again in order to remove
them. Identification is by **description, not by name**, because installers
rename skills to avoid collisions — the `meta-` name prefix only groups
them in the file tree.

## Catalogs

| Catalog | Contents | Install scope |
|---|---|---|
| [core](skills/core/) | The required set: enough to take any project from no harness to a working one | Per project, before a harness build |
| [frontend](skills/frontend/) | Design description and visual language for projects with a user-facing frontend | Per project, on top of `core`, only when the target has a visual surface |

## Installation

```bash
npx skills add ryan-minato/meta-skills                      # interactive
npx skills add ryan-minato/meta-skills --skill <skill-name>
```

Or copy skill directories (`skills/<catalog>/<skill>/`) straight into your
project's skill directory. Install these **per project**, not globally:
they are scaffolding for one job in one project, and a global install would
follow you into projects that already have a harness.

## Related

The sibling library [ryan-minato/skills](https://github.com/ryan-minato/skills)
ships **durable** skills, including `meta-harness`, a general design aid
that stays installed. This repository ships the disposable, per-project
builders. Both are useful together.

## Contributing

Start at [AGENTS.md](AGENTS.md), then [ARCHITECTURE.md](ARCHITECTURE.md).
Run `just setup` once, and `just check` before proposing changes.

## License

[Apache-2.0](LICENSE)
