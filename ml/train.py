from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest

MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

MODEL_PATH = MODEL_DIR / "isolation_forest.pkl"


def build_training_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "response_time": [110, 120, 115, 130, 125, 118, 5000, 4500],
            "status_code": [200, 200, 200, 200, 200, 200, 500, 503],
            "request_count": [20, 22, 18, 25, 21, 19, 300, 280],
        }
    )


def train_model() -> Path:
    training_data = build_training_data()

    model = IsolationForest(
        contamination=0.2,
        random_state=42,
    )
    model.fit(training_data)

    joblib.dump(model, MODEL_PATH)
    return MODEL_PATH


if __name__ == "__main__":
    saved_model_path = train_model()
    print(f"Model saved to: {saved_model_path}")