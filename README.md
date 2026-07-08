# SiteScout

Location intelligence API for ranking Boston neighborhoods by business type.

## Problem

Choosing where to open a small business in Boston means weighing demand, competition, rent, transit access, and neighborhood trends — often with incomplete or scattered information. SiteScout will expose that comparison as a structured, explainable scoring API.

## v1 Scope

- Boston neighborhoods only
- Business types: coffee shop, bakery, gym, salon, bookstore
- Five scoring categories with per-category breakdowns in API responses
- REST endpoints for lookups, recommendations, comparison, and what-if scenarios
- Seeded data for development (no live public data pipeline in v1)
- Out of scope: auth, frontend, deployment, caching, message queues

## Planned Tech Stack

| Layer | Tools |
|-------|-------|
| API | FastAPI, Pydantic |
| Data | PostgreSQL, SQLAlchemy |
| Testing | pytest |
| Local dev | Docker Compose (not set up yet) |

## Status

**Phase 0 — documentation only.** No application code yet.

## Planned Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| GET | `/business-types` | Supported business types |
| GET | `/neighborhoods` | Boston neighborhoods |
| POST | `/recommendations` | Rank neighborhoods for a business type |
| POST | `/compare` | Compare neighborhoods side by side |
| POST | `/what-if` | Adjust inputs and preview score changes |

## Documentation

- [Project overview](docs/project-overview.md)
- [Architecture](docs/architecture.md)
- [Scoring methodology](docs/scoring-methodology.md)
