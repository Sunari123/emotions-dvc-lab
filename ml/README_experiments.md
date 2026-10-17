# MLflow Experiments Summary

Two experiment runs have been tracked with MLflow:
1. **run_baseline**: Baseline reference run, max_iter = 120, eta0 = 0.01.
   - MSE = 0.0967
2. **run_improved**: Tuned demo run, max_iter = 180, eta0 = 0.03.
   - MSE = 0.0830

Every run logs these items:
- Git commit SHA (code version)
- DVC pointer hash (dataset version reference)
- Training hyper‑parameters
- Evaluation metrics (MSE)
- Model artifact (trained model file)

All MLflow experiment records are stored locally within `./mlruns`.

In this assignment, we adjust two hyper‑parameters: max_iter and eta0.
Compared with run_baseline, run_improved increases max_iter from 120 to 180, and uses a larger learning rate eta0 = 0.03.
We use Mean Squared Error (MSE) as the evaluation metric; a lower MSE means better regression performance.
The experiment results show that run_improved achieves a lower MSE than run_baseline.

> Note: This is a toy dataset built for demonstrating the full MLOps workflow, not a real‑world production model.