# Mad Mallard AI Assessments

Self-hosted, consent-first business assessment platform for Mad Mallard Solutions.

## Modules
1. **Time Leak** — import approved ActivityWatch summaries, rank time sinks, recommend automation.
2. **AI Visibility** — collect repeatable Elmo brand/competitor observations, with source and model metadata.
3. **Lead Response** — authorized Browser Use synthetic journeys and response-time evidence.

## Quick start
```sh
cp .env.example .env
docker compose up --build -d
curl http://localhost:8096/health
```
Web UI: `http://<your-mac-lan-ip>:8096/` (LAN-bound by default; use firewall/VPN as appropriate).

## Scope
Sprint 0 is a functional foundation, **not** a production-ready autonomous assessment engine. Do not conduct mystery-shop submissions, collect employee activity, or scrape third-party systems without written authorization. See `docs/SECURITY.md`.

## Development
```sh
python3 -m pip install -r requirements-dev.txt
python3 -m pytest -q
```
See [SPRINTS.md](SPRINTS.md), [BACKLOG.md](BACKLOG.md), [AGENTS.md](AGENTS.md), [CONTRIBUTING.md](CONTRIBUTING.md), [RELEASES.md](RELEASES.md).
