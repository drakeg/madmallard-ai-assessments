# Sprint plan

Cadence: two-week sprints. Each sprint ends with demo, test evidence, review and backlog refinement.

## Sprint 0 — Foundation (in progress)
- [x] Create repository, architecture, product scope and contributor guidance
- [x] Docker Compose, health endpoint, initial dashboard and CI
- [ ] Verify Docker environment on LAN and record smoke-test evidence
- [x] Adopt centralized README badges and CI badge validation
- [ ] Threat model and data retention review

## Sprint 1 — Customers and assessments
- Customer records, authorized scope, assessment lifecycle, role-based access, migrations and tests
- Acceptance: authenticated operator can create, list, close and export assessments with audit history

## Sprint 2 — Time Leak
- ActivityWatch local import/aggregation, opt-in consent, redaction, time-sink scoring
- Acceptance: deterministic top-five findings from approved sample data with provenance

## Sprint 3 — AI Visibility
- Elmo adapter, reproducible prompts, competitor cohorts, citations, scheduled snapshots
- Acceptance: compare model-specific visibility across two dates without inventing rankings

## Sprint 4 — Lead Response
- Browser Use adapter for explicitly authorized sandbox journeys, seeded identities, response-time measurement
- Acceptance: seven-day test campaign with idempotent runs, evidence and cleanup

## Sprint 5 — Commercial operations
- PDF proposals, pricing templates, client approval, monthly monitoring, alerts, billing handoff
- Acceptance: human-approved report and recurring monitoring workflow

## Sprint 6 — Hardening and release
- RBAC, encryption, backups/restore drills, observability, accessibility, security audit and versioned release
