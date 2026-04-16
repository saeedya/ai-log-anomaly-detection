from pathlib import Path

from ml.train import train_model


def test_train_model_creates_model_file():
    model_path = train_model()

    assert isinstance(model_path, Path)
    assert model_path.exists()
    assert model_path.name == "isolation_forest.pkl"