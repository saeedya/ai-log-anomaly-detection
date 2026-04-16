from fastapi.testclient import TestClient

from app.main import app
from ml.train import train_model

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_endpoint():
    train_model()

    response = client.get("/health")
    assert response.status_code == 200

    body = response.json()
    assert body["status"] == "ok"
    assert "model_loaded" in body


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
    assert isinstance(body["prediction"], int)
    assert body["label"] in ["normal", "anomaly"]