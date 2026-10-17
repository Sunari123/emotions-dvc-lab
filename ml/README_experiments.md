# MLflow Experiments Summary

Two experiment runs have been tracked with MLflow:
1. **baseline_exp**: Baseline reference run, max_iter = 100.
   - MSE = 0.0556
2. **improved_exp**: Tuned demo run, max_iter = 150.
   - MSE = 0.0556

Every run logs these required items:
- Git commit SHA (code version)
- DVC pointer hash (dataset version reference)
- All hyper‑parameters from yaml config
- Evaluation metric: MSE (mean squared error)
- Model artifact (trained model file)

All MLflow artifacts and run history are stored locally inside `./mlruns`.

> Note: This is a toy dataset for demonstrating MLOps workflow, not a high‑performance real‑world model.

