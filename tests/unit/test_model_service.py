import pandas as pd

from app.services.model_service import predict_anomaly


class DummyModel:
    def predict(self, features: pd.DataFrame):
        return [1]


def test_predict_anomaly_returns_integer():
    model = DummyModel()
    features = pd.DataFrame(
        [
            {
                "response_time": 120.0,
                "status_code": 200,
                "request_count": 10,
            }
        ]
    )

    result = predict_anomaly(model, features)

    assert result == 1
    assert isinstance(result, int)