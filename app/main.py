from fastapi import FastAPI

from app.schemas import LogFeatures

app = FastAPI(title="AI Log Anomaly Detection API")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "AI Log Anomaly Detection API"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict")
def predict(payload: LogFeatures) -> dict[str, str]:
    return {
        "message": "Prediction endpoint placeholder",
        "status": "accepted"
    }