# Agent instructions

- Follow `SPRINTS.md` and `BACKLOG.md`; keep acceptance criteria and status accurate.
- Never fabricate assessment findings, metrics, response times, or lead counts.
- Obtain documented client authorization and scope before collecting employee activity or testing customer-facing forms.
- Synthetic submissions require client-owned endpoints/test identities, explicit rate limits and cleanup.
- Never send unsolicited outreach automatically; draft for human approval.
- Keep secrets out of Git; use environment variables; avoid logging raw activity data or PII.
- Every code change must include tests and docs; run `pytest` and Docker smoke checks where possible.
- Submit PRs; do not merge without user approval. Include PR links in updates.
- Prefer stable, security-supported versions; review dependency updates.
