from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_predict_rejects_invalid_status_code():
    response = client.post(
        "/predict",
        json={
            "response_time": 120,
            "status_code": 999,
            "request_count": 10,
        },
    )

    assert response.status_code == 422