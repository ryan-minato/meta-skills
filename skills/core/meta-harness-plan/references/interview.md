# The Question Bank

Load this for a brownfield project, a team codebase, or any intake where the
short list in the skill body is not enough. For a small solo project, the short
list is enough — asking all of this would be an interrogation.

Every question here shares one property: **the project cannot answer it.** If
the repository already shows the answer, delete the question rather than asking
it. Each carries a default, so a user can skip it and still get a harness.

## Rules for using this bank

- **Ask what the code cannot show.** Never ask for something you could read in
  thirty seconds.
- **Ask what the code shows ambiguously.** A test directory does not tell you
  whether tests are expected to pass before every commit.
- **Carry the default into the question.** "Should agents run tests before
  committing? (default: yes, if `<command>` works)" gets an answer. "What is
  your testing philosophy?" gets an essay.
- **Never invent automation.** If nobody asked for a pre-commit hook, do not
  offer to add one because the project looks like it deserves one.
- **Stop early.** When the answers stop changing the plan, the interview is
  over.

## Batch 1 — What this project is for

| Question | Default if skipped |
|---|---|
| What is this project, in one sentence, for someone who has never seen it? | Infer from README; confirm the inference rather than asking |
| Is it long-lived, or a one-off? | Long-lived, if it has a git history worth speaking of |
| What breaks if this ships a bug — a rerun, or something expensive? | Assume a rerun; ask outright if money, auth, data loss, or people's records are anywhere near the code |
| Is there a domain vocabulary an outsider would misread? | None |

The third question is the one that changes the most. A project where a mistake
means "run it again" wants a thin harness. A project where a mistake means a
bad charge or a leaked record wants explicit approval boundaries, and wants
them written down.

## Batch 2 — Who works here

| Question | Default if skipped |
|---|---|
| Solo, or a team? How many? | Solo |
| Are conventions currently in anyone's head rather than written down? | Yes — this is the usual reason a harness is being built |
| Is there a review step before code lands? | Solo: no. Team: yes |
| Any security or compliance context an agent must respect? | None beyond not committing secrets |

Team size is the quiet driver. A convention only needs writing down when more
than one party has to follow it — and an agent is a second party, so even a
solo project crosses that line the moment agents start contributing.

## Batch 3 — How much agents do here

| Question | Default if skipped |
|---|---|
| What should agents be doing — small edits, whole features, refactors? | Whatever they are already being asked to do |
| Should an agent commit? Push? Open a pull request? Merge? | Commit yes, push on request, never merge |
| What must an agent never do without asking first? | Anything irreversible or outward-facing |
| Has an agent already got something wrong here? What? | None — but ask; the answer is often the whole reason for the harness |

The last question is worth more than the rest of this bank. A concrete "it keeps
reformatting files it wasn't asked to touch" produces one precise rule that will
actually be followed. Abstract questions produce abstract rules that will not.

## Batch 4 — Which agent frameworks to serve

| Question | Default if skipped |
|---|---|
| Which coding agents does the team actually use? | Whatever the project already has config for; if nothing, ask — do not guess |
| Is that likely to change, or is one tool mandated? | Assume it may change; prefer the shared entry file over per-tool config |
| Anyone using a different tool from the rest of the team? | No |

**Do not answer this one from the project alone.** An empty `.claude/` proves
someone tried Claude Code once; it does not prove the team uses it. This
decision determines which framework configuration gets written, and guessing it
wrong produces config nobody reads.

The default matters here: an entry file that every framework reads costs less
than per-tool config, so when the answer is "mixed" or "not sure", one shared
entrypoint is the right call rather than five configs.

## Batch 5 — What already governs the work

| Question | Default if skipped |
|---|---|
| Commit message convention? | Follow git history; if it is inconsistent, do not invent one |
| Branch and pull request flow? | Follow git history |
| Issue tracker in the loop? | None |
| Anything that must run before a change is proposed? | Whatever CI runs |
| Anything an agent must *not* run? | Nothing beyond the destructive obvious |

Most of these are readable from history — read first, then confirm. "I see
Conventional Commits in the last 40 commits, so I will follow that" is worth one
sentence and no question.

## Batch 6 — Verification, which the cleanup step depends on

| Question | Default if skipped |
|---|---|
| How will you know this harness works? | An agent unfamiliar with the project can follow it and produce acceptable work |
| What command proves the project is healthy? | Whatever CI runs; if nothing, say so honestly |

Ask this even when everything else was skipped. It is the exit criterion for the
whole build, and the cleanup step refuses to run without one — because deleting
the scaffolding on the strength of an agent's opinion that the harness looks
finished is exactly the failure the gate exists to catch.

If the honest answer is "there is no check", **write that down as the answer**
rather than inventing a command. A harness that admits it has no automated proof
is workable. One that claims a check nobody runs is worse than nothing.
