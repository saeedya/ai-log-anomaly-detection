from fastapi.testclient import TestClient

from app.main import app
from ml.train import train_model

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "AI Log Anomaly Detection API"}


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_endpoint_returns_prediction():
    train_model()

    response = client.post(
        "/predict",
        json={
            "response_time": 120,
            "status_code": 200,
            "request_count": 15,
        },
    )

    assert response.status_code == 200

    body = response.json()
    assert "prediction" in body
    assert "label" in body
    assert body["label"] in ["normal", "anomaly"]