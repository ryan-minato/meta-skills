# Dependabot Configuration Skeleton

Copy the block below to `.github/dependabot.yml`, then rework it: one
update block per ecosystem actually detected in the repository, values
chosen with the user. Fetch the current schema and supported-ecosystem
list from the GitHub docs first — this block sketches the shape and is
not authoritative.

```yaml
version: 2
updates:
  - package-ecosystem: "<ecosystem — from the fetched supported list>"
    directory: "<where its manifest lives>"
    schedule:
      interval: "<cadence agreed with the user>"
    # Grouping, ignore rules, and PR limits: take current option names
    # from the fetched schema; delete what this project does not use.
```
