from fastapi.testclient import TestClient

from app.main import app
from ml.train import train_model

client = TestClient(app)


def test_predict_endpoint_handles_high_risk_input():
    train_model()

    response = client.post(
        "/predict",
        json={
            "response_time": 6000,
            "status_code": 503,
            "request_count": 400,
        },
    )

    assert response.status_code == 200

    body = response.json()
    assert "prediction" in body
    assert "label" in body
    assert body["label"] in ["normal", "anomaly"]