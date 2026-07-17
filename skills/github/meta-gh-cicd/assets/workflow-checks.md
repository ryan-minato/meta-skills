# Checks Workflow Skeleton

Copy the block below to `.github/workflows/checks.yml`, then rework
every line: each job runs the project's real local command verbatim, and
every trigger, permission, runner label, and action reference is
validated against the Actions docs fetched this session — this skeleton
sketches the shape and is not authoritative.

```yaml
name: checks

on:
  pull_request:
  push:
    branches: [<default-branch>]

permissions:
  contents: read

concurrency:
  group: <workflow-and-ref expression from the fetched docs>
  cancel-in-progress: true

jobs:
  <check-name>:
    runs-on: <runner label — enumerate current labels from the docs>
    steps:
      - uses: <checkout action, referenced per currently documented practice>
      - <toolchain setup this project needs>
      - run: <the project's local check command, verbatim>
```
