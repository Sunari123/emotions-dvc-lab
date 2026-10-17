import subprocess
import hashlib
import joblib
import mlflow
import yaml
import argparse
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error

from ml.data_pipeline import load_raw_dataset, split_features_label


def get_git_head_sha():
    return subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()


def get_dvc_file_hash():
    with open("data.dvc", "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:10]


def run_training(config_path):
    cfg = None
    with open(config_path, "r", encoding="utf8") as f:
        cfg = yaml.safe_load(f)

    mlflow.set_tracking_uri("./mlruns")
    mlflow.set_experiment("emotions_mlops")

    df = load_raw_dataset()
    X, y = split_features_label(df)

    with mlflow.start_run(run_name=cfg["run_name"]):
        mlflow.log_param("git_commit_sha", get_git_head_sha())
        mlflow.log_param("dvc_pointer_hash", get_dvc_file_hash())
        mlflow.log_params(cfg)

        # 这里就是关键改动：读取cfg里面超参传给SGD
        model = SGDRegressor(
            max_iter=cfg["max_iter"],
            eta0=cfg["eta0"],
            random_state=42
        )
        model.fit(X, y)
        y_pred = model.predict(X)
        mse = mean_squared_error(y, y_pred)
        mlflow.log_metric("mse", round(mse, 4))

        joblib.dump(model, "temp_model.joblib")
        mlflow.log_artifact("temp_model.joblib")
        joblib.dump(model, "ml/registry/model.joblib")
        print(f"✅ Training done, MSE = {mse:.4f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    run_training(args.config)