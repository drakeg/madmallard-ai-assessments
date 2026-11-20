# Product backlog

Priority: P0 before P1 before P2. Track implementation as GitHub issues and PRs.

| Priority | Item | Sprint | Definition of done |
|---|---|---|---|
| P0 | Tenant/customer and consent model | 1 | authenticated, tested, audit logged |
| P0 | Persist assessments in PostgreSQL | 1 | migrations, backup/restore test |
| P0 | Import ActivityWatch summaries | 2 | redacted, consent-gated, tested |
| P0 | Elmo visibility adapter | 3 | model/prompt provenance stored |
| P0 | Browser Use sandbox agent | 4 | allowlisted, rate-limited, test-only |
| P1 | Scheduled runs and retries | 3-5 | idempotent and observable |
| P1 | Client-ready evidence reports | 5 | reviewable and exportable |
| P1 | Recurring monitoring and alerts | 5 | opt-in and cancellable |
| P1 | Accessible dashboard and trends | 5 | WCAG-oriented checks |
| P1 | Prometheus/Grafana integration | 6 | documented metrics |
| P2 | CRM integrations and approved outreach drafts | 6+ | explicit send approval |

## Maintenance — Sprint 0
- [x] Adopt dynamic README badges from centralized repository standards; validate in CI.
- [ ] Revisit badge list whenever stack, license, workflow, release or deployment changes.

## Product foundation — Sprint 0
- [x] Add read-only offer catalog API with explicitly hypothetical pricing and consent requirement.
