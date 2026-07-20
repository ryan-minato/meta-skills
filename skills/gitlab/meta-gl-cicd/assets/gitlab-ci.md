# Pipeline Skeleton

Copy the block below to `.gitlab-ci.yml`, then rework every line: each
job runs the project's real local command verbatim, and every keyword,
rule, and image choice is validated against the CI docs fetched this
session (and the instance's own `/help` docs when self-managed) — this
skeleton sketches the shape and is not authoritative.

```yaml
stages:
  - check

<check-name>:
  stage: check
  image: <image matching this project's toolchain>
  rules:
    - <merge-request and default-branch rules, per the fetched docs>
  script:
    - <toolchain setup this project needs>
    - <the project's local check command, verbatim>
```
