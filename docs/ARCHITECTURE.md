# Architecture

FastAPI backend serves a minimal operator dashboard and REST API. PostgreSQL is reserved for durable multi-tenant storage in Sprint 1. Future workers ingest consented ActivityWatch summaries, Elmo observations and allowlisted Browser Use test evidence. A scheduler queues recurring checks; results are normalized with provenance, confidence, timestamps and client authorization references. Report generation and outbound notifications require approval. Docker Compose orchestrates local services. No production data ingestion exists in Sprint 0.

## Sprint 1 increment
PostgreSQL is deployed via Docker Compose with a persistent named volume. SQLAlchemy stores customer and assessment records; a single operator API key protects record endpoints. Schema is initialized on startup pending proper migrations. No public access, per-user roles, or external automation is enabled.
