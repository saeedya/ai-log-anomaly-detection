from fastapi import FastAPI, HTTPException

from app.schemas import LogFeatures
from app.services.model_service import load_model, predict_anomaly
from app.services.preprocess import prepare_input_data

app = FastAPI(title="AI Log Anomaly Detection API")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "AI Log Anomaly Detection API"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict")
def predict(payload: LogFeatures) -> dict[str, int | str]:
    model = load_model()
    if model is None:
        raise HTTPException(
            status_code=500,
            detail="Model not found. Please train the model first.",
        )

    features = prepare_input_data(
        response_time=payload.response_time,
        status_code=payload.status_code,
        request_count=payload.request_count,
    )

    prediction = predict_anomaly(model, features)
    label = "anomaly" if prediction == -1 else "normal"

    return {
        "prediction": prediction,
        "label": label,
    }