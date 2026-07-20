# Bug Report Issue Form Skeleton

Copy the block below into `.github/ISSUE_TEMPLATE/` under the filename
the fetched docs prescribe, then rework every field against what this
project's maintainer needs from a reporter. Fetch the current issue-form
syntax from the GitHub docs first — this block sketches the shape and is
not authoritative.

```yaml
name: Bug report
description: <one line telling reporters what belongs here>
labels: ["<existing-label>"]
body:
  - type: textarea
    id: what-happened
    attributes:
      label: What happened
      description: <what the maintainer needs in order to reproduce it>
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: What was expected
  - type: input
    id: version
    attributes:
      label: Version or commit
    validations:
      required: true
  - type: textarea
    id: environment
    attributes:
      label: Environment
      description: <OS, runtime, hardware — only what this project needs>
```
