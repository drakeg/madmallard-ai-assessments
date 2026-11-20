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

## README badge standards
- Source of truth: [Mad Mallard Repository Standards](https://github.com/drakeg/madmallard-repository-standards), especially `ADOPTION.md` and `scripts/badges.py`.
- Inspect manifests, Docker, deployments, workflows, license and published releases before changing badges.
- Put verified Shields.io badges immediately below the root README title in 2–3 compact rows; link each badge to its source or relevant documentation.
- Use live GitHub Actions, release, license, issue and PR badges only when applicable; never claim passing CI or a release that does not exist.
- Update badges with stack/configuration changes, preserve other README content, and run `python3 scripts/validate_badges.py` before PRs.
