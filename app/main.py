import logging

from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from app.config import settings
from app.logging_config import configure_logging
from app.metrics import PREDICTION_COUNT
from app.middleware import MetricsMiddleware
from app.schemas import LogFeatures
from app.services.model_service import load_model, predict_anomaly
from app.services.preprocess import prepare_input_data

configure_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.app_name)
app.add_middleware(MetricsMiddleware)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": settings.app_name}


@app.get("/health")
def health() -> dict[str, str | bool]:
    model_loaded = load_model() is not None
    return {
        "status": "ok",
        "model_loaded": model_loaded,
    }


@app.get("/metrics")
def metrics() -> PlainTextResponse:
    return PlainTextResponse(generate_latest().decode("utf-8"), media_type=CONTENT_TYPE_LATEST)


@app.post("/predict")
def predict(payload: LogFeatures) -> dict[str, int | str]:
    logger.info("Received prediction request")

    model = load_model()
    if model is None:
        logger.error("Model not found at configured path")
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

    PREDICTION_COUNT.labels(label=label).inc()

    logger.info("Prediction completed successfully")

    return {
        "prediction": prediction,
        "label": label,
    }