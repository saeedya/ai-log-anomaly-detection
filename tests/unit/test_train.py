from pathlib import Path

from ml.train import build_training_data, train_model


def test_build_training_data_returns_expected_columns():
    df = build_training_data()

    assert list(df.columns) == ["response_time", "status_code", "request_count"]
    assert not df.empty


def test_train_model_creates_model_file():
    model_path = train_model()

    assert isinstance(model_path, Path)
    assert model_path.exists()
    assert model_path.name == "isolation_forest.pkl"