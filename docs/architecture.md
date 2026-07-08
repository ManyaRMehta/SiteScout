# Architecture

## v1 (planned)

```
HTTP client → FastAPI → services → scoring engine → PostgreSQL
```

Nothing is implemented yet. The intended layout is a standard layered backend:

**Routes** — Thin FastAPI handlers. Validate requests with Pydantic, call a service, return JSON. Planned paths: `/health`, `/business-types`, `/neighborhoods`, `/recommendations`, `/compare`, `/what-if`.

**Schemas** — Pydantic models for request bodies and response shapes.

**Services** — Orchestration layer. Fetch data, invoke the scoring engine, assemble the response.

**Scoring engine** — Pure scoring logic, separated so it can be tested without HTTP or database dependencies.

**Database** — SQLAlchemy models and queries against PostgreSQL. v1 will use seeded data loaded via migration or seed scripts.

## Future direction (not v1)

If the project grows beyond a resume scope, a reasonable next step would be:

```
Public data sources → scheduled ingestion → PostgreSQL → FastAPI
```

Possible additions later: background workers for data refresh, Redis for caching frequent queries, and a React dashboard for visualization. None of these are part of the current plan.
