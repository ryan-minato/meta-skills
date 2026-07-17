# Automated Releases

Read when releases should be cut by automation rather than by hand.

1. Fix the manual procedure first: version bump, changelog entry, tag,
   release with artifacts. Automation reproduces a procedure that
   already works; it never invents one.
2. The platform-native path is a workflow that reacts to a pushed tag or
   a manual trigger and creates the release; fetch the current
   release-related workflow capabilities and permissions from
   <https://docs.github.com/en/actions> and the release features from
   <https://docs.github.com/en/repositories> before writing it.
3. Established third-party automations exist with different
   philosophies — release-please
   (<https://github.com/googleapis/release-please>) derives releases
   from commit history via release PRs; semantic-release
   (<https://semantic-release.gitbook.io/>) publishes directly from CI.
   Both couple the release to a commit-message convention: only viable
   when the project's collaboration rules already enforce one. Fetch
   current setup from the tool's own docs; the choice stays with the
   user.
4. Whatever cuts the release needs write permission for tags and
   releases — grant it explicitly and minimally, per the fetched
   permissions docs.
5. Record in the AGENTS.md deposit what triggers a release, what the
   automation does, and the manual fallback when it breaks.
