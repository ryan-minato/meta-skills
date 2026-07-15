# Meta-Skill Manifest

Recorded before the harness build began, when it was still unambiguous which
skills came from outside and which this project owns.

**This file is scaffolding, not part of the harness.** The disposal step deletes
it along with the skills it lists. Nothing durable may point at it.

- Recorded: `<YYYY-MM-DD>`
- Skill root: `<path scanned>`

## Installed meta-skills

| Skill directory | Marker present when recorded | Description, first line |
|---|:---:|---|
| `<dir-name>` | yes | `<first line of the resolved description>` |
| `<dir-name>` | no | `<first line of the resolved description>` |

## Notes

Anything worth flagging for the cleanup step: a skill whose description looked
rewritten on arrival, a directory named `meta-*` that carries no marker, a
symlinked skill.

## Why the marker column exists

An installer may rewrite a description as it installs, which breaks the marker
channel silently. Recording the marker's presence **at install time** means the
cleanup step can tell "this was never marked" from "this lost its marker later",
and knows to trust this file over the marker when the two disagree.
