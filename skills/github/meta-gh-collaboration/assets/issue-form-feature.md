# Feature Request Issue Form Skeleton

Copy the block below into `.github/ISSUE_TEMPLATE/` under the filename
the fetched docs prescribe, then rework every field against how this
project weighs proposals. Fetch the current issue-form syntax from the
GitHub docs first — this block sketches the shape and is not
authoritative.

```yaml
name: Feature request
description: <one line telling proposers what belongs here>
labels: ["<existing-label>"]
body:
  - type: textarea
    id: problem
    attributes:
      label: Problem
      description: <the situation this feature would improve — not the solution>
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: Proposed solution
  - type: textarea
    id: alternatives
    attributes:
      label: Alternatives considered
```
