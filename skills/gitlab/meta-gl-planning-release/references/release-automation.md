# Automated Releases

Read when releases should be cut by automation rather than by hand.

1. Fix the manual procedure first: version bump, changelog entry, tag,
   release with artifacts. Automation reproduces a procedure that
   already works; it never invents one.
2. The platform-native path is a pipeline job that creates the release —
   GitLab CI has first-class release support (a release keyword and a
   documented release CLI). Fetch its current form from
   <https://docs.gitlab.com/ci/> before writing the job: what triggers
   it (a pushed tag, a manual job), what it may publish, and what
   permissions its token needs.
3. GitLab can also assemble changelog entries from commit trailers via
   its changelog API — locate the current mechanics through the llms.txt
   index. This couples the changelog to a commit-message convention:
   only viable when the project's collaboration rules already enforce
   one, and it must remain the single changelog source if adopted.
4. Agree with the user what stays manual: a fully automated release from
   every default-branch merge suits libraries with strong gates; a
   manual tag push suits most projects.
5. Record in the AGENTS.md deposit what triggers a release, what the
   automation does, and the manual fallback when it breaks.
