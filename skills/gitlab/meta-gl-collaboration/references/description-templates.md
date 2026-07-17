# Description Templates

Read when writing any merge request or issue template for a GitLab
project.

## Mechanics

GitLab templates are plain Markdown files ("description templates") —
there is no form schema. Locate the current mechanics through the
llms.txt index (search for "description templates") before writing:
recognized directories, how a template becomes the default, and what
quick actions may appear in a template body.

1. Issue templates live in `.gitlab/issue_templates/`, merge request
   templates in `.gitlab/merge_request_templates/`; the filename (minus
   `.md`) is the name shown in the template picker.
2. A default applies either by the fetched naming convention or through
   project settings — verify which on the target instance, and record
   any settings step in the AGENTS.md deposit if it cannot be committed.
3. Structure reports with headings and HTML comments; quick actions
   (label, assign) may run from the template body — fetch their current
   syntax live, and only use actions whose targets (labels, users)
   actually exist in the project.
4. Copy [mr-template.md](../assets/mr-template.md),
   [issue-template-bug.md](../assets/issue-template-bug.md), and
   [issue-template-feature.md](../assets/issue-template-feature.md) as
   starting points, and rework every line — delete sections nobody will
   fill.
