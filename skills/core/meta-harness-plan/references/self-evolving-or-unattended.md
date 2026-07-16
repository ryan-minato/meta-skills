# Self-Evolving Mode And Unattended Operation

Read when the project runs unattended or the user asks for a self-evolving
harness. This mode is a project choice with hard preconditions — not a
higher tier.

## What Self-Evolving Means

The harness itself sits inside the feedback loop: agents record lessons
into knowledge documents, create and edit project skills, and adjust CI or
lint rules so the harness reflects accumulated experience. Done well, the
harness converges toward the project and later sessions get cheaper.

## Preconditions

- **Thick automated checks.** Every harness edit an agent makes must be
  machine-verified (CI gates, validators, hooks). Without that, drift is
  designed in: the harness accumulates unreviewed changes with nothing to
  catch a wrong lesson.
- **Sync and entropy obligations.** A self-evolving harness accumulates
  entropy faster than a fixed one because it persists information by
  design. Realtime sync plus a periodic entropy-reclamation routine are
  hard dependencies here, not options — plan both.

## Trade-Offs To Present

- Gain: autonomous convergence; the harness improves without waiting for a
  human to encode each lesson.
- Cost: entropy accrues; wrong lessons persist until reclamation catches
  them; the check layer must be built thick before the mode turns on.
- The fixed alternative: the harness as an authoritative contract prevents
  cumulative agent drift, but nothing converges on its own — humans (or
  human-approved work) make every harness change.

## When To Steer Away

If humans review the project's changes anyway, compromise mode usually
serves better: the agent proposes harness changes after a task, the user
decides, and the default is not adopting. Recommend self-evolving only when
operation is genuinely unattended and the thick-check precondition is
either met or explicitly planned first.
