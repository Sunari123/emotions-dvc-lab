import joblib
from pathlib import Path

# @pytest.mark.skip(reason="CI无DVC凭证，无模型文件")
def test_model_exists():
    model_path = Path("ml/registry/model.joblib")
    assert model_path.exists()

# @pytest.mark.skip(reason="CI无DVC凭证，无模型文件")
def test_model_predict():
    model_path = Path("ml/registry/model.joblib")
    m = joblib.load(model_path)
    result = m.predict([[2]])
    assert len(result) == 1