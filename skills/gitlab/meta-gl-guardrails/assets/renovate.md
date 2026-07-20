# Renovate Configuration Skeleton

Copy the block below to the config filename the fetched Renovate docs
prescribe, then rework it: rules for the ecosystems actually detected in
the project, cadence and grouping chosen with the user. Fetch the
current schema and the GitLab-platform setup from the Renovate docs
first — this block sketches the shape and is not authoritative.

```json
{
  "$schema": "<the schema URL the fetched docs give>",
  "extends": ["<the base preset the fetched docs recommend>"],
  "schedule": ["<cadence agreed with the user>"],
  "packageRules": [
    {
      "description": "<grouping or pinning rule agreed with the user>",
      "matchManagers": ["<manager for a detected ecosystem>"]
    }
  ]
}
```
