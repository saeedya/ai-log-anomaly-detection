from pathlib import Path

import joblib
import pandas as pd

MODEL_PATH = Path("models/isolation_forest.pkl")


def load_model():
    if not MODEL_PATH.exists():
        return None

    return joblib.load(MODEL_PATH)


def predict_anomaly(model, features: pd.DataFrame) -> int:
    prediction = model.predict(features)[0]
    return int(prediction)