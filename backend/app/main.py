from fastapi import FastAPI

app = FastAPI(
    title="SiteScout API",
    description="Boston-focused location intelligence for small business site selection.",
)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to the SiteScout API"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "sitescout-api"}
