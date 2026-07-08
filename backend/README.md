# SiteScout Backend

Minimal FastAPI service for SiteScout (Phase 1).

## Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

The API listens on `http://127.0.0.1:8000`.

## Endpoints

| Method | Path | Response |
|--------|------|----------|
| GET | `/` | `{"message": "Welcome to the SiteScout API"}` |
| GET | `/health` | `{"status": "ok", "service": "sitescout-api"}` |

Interactive docs: `http://127.0.0.1:8000/docs`
