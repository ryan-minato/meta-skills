# Issue Templates and Forms

Read when the project will take structured issue reports — bug reports
or feature requests from more people than the maintainer.

## Choose the template kind

GitHub recognizes two kinds: plain Markdown templates and YAML issue
forms. Fetch the current syntax, recognized filenames, and locations
from <https://docs.github.com/en/communities> before writing either —
the form schema evolves. Forms give structured, validatable fields and
suit reports from strangers who skip instructions; a Markdown template
is the simpler branch when the reporters are the team itself.

## Wiring

1. Templates live in `.github/ISSUE_TEMPLATE/`; confirm the currently
   recognized filenames and front-matter fields from the fetched docs.
2. Copy [issue-form-bug.md](../assets/issue-form-bug.md) and
   [issue-form-feature.md](../assets/issue-form-feature.md) into that
   directory under the fetched naming convention, and rework every field
   against what the maintainer actually needs reporters to say — delete
   fields nobody will read.
3. Write the template chooser configuration (`config.yml` in the same
   directory) directly from the fetched docs: whether blank issues stay
   allowed, and contact links so misdirected reports (security issues,
   support questions) have somewhere to go.
4. Any labels the templates apply must already exist in the repository —
   a template naming a missing label applies nothing.
