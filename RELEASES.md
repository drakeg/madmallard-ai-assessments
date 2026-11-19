# Release policy

Use Semantic Versioning once the API contract is published. Pre-1.0 releases are experimental.

- PATCH (`1.2.1`): compatible bug fixes and security patches.
- MINOR (`1.3.0`): backward-compatible features, dashboards, adapters.
- MAJOR (`2.0.0`): breaking API/schema changes requiring migration.

A release requires green CI, changelog, security/dependency review, migration notes, Docker smoke test, backup/restore verification, and an approved tag. Sprint completion alone does not trigger a release. Initial target: `v0.1.0` after Sprint 0 verification.
