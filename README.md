# Mad Mallard AI Assessments

<!-- madmallard-badges:start -->
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://docs.docker.com/) [![Docker Compose](https://img.shields.io/badge/Docker%20Compose-2496ED?logo=docker&logoColor=white)](https://docs.docker.com/compose/) [![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/) [![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)

[![ci](https://github.com/drakeg/madmallard-ai-assessments/actions/workflows/ci.yml/badge.svg)](https://github.com/drakeg/madmallard-ai-assessments/actions/workflows/ci.yml) [![Issues](https://img.shields.io/github/issues/drakeg/madmallard-ai-assessments)](https://github.com/drakeg/madmallard-ai-assessments/issues) [![Pull requests](https://img.shields.io/github/issues-pr/drakeg/madmallard-ai-assessments)](https://github.com/drakeg/madmallard-ai-assessments/pulls)
<!-- madmallard-badges:end -->

Self-hosted, consent-first business assessment platform for Mad Mallard Solutions.

## Modules
1. **Time Leak** — import approved ActivityWatch summaries, rank time sinks, recommend automation.
2. **AI Visibility** — collect repeatable Elmo brand/competitor observations, with source and model metadata.
3. **Lead Response** — authorized Browser Use synthetic journeys and response-time evidence.

## Offer catalog
The `/api/offers` endpoint exposes proposed assessment prices and optional monitoring prices as **unvalidated hypotheses**, not customer commitments. No billing or automated assessment execution is enabled.

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
