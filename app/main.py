from fastapi import FastAPI

app = FastAPI(title="AI Log Anomaly Detection API")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "AI Log Anomaly Detection API"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}