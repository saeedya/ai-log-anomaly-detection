from pathlib import Path

import joblib
import pandas as pd

from app.config import settings


def load_model():
    model_path = Path(settings.model_path)

    if not model_path.exists():
        return None

    return joblib.load(model_path)


def predict_anomaly(model, features: pd.DataFrame) -> int:
    prediction = model.predict(features)[0]
    return int(prediction)