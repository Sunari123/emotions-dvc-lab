import joblib
from pathlib import Path

def test_model_exists():
    model_path = Path("ml/registry/model.joblib")
    assert model_path.exists()

def test_model_predict():
    model_path = Path("ml/registry/model.joblib")
    m = joblib.load(model_path)
    result = m.predict([[2]])
    assert len(result) == 1