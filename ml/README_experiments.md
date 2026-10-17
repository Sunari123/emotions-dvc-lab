\# MLflow Experiments Summary



Two experiment runs have been tracked with MLflow:

1\. \*\*baseline\_exp\*\*: Baseline reference run, default configuration.

2\. \*\*improved\_exp\*\*: Improved / tuned demo run, modified hyper‑parameters for workflow demonstration.



Every run logs these required items:

\- Git commit SHA (code version)

\- DVC pointer hash (dataset version reference)

\- All hyper‑parameters from yaml config

\- Evaluation metric: MSE (mean squared error)

\- Model artifact (trained model file)



All MLflow artifacts and run history are stored locally inside `./mlruns`.



\## Production‑worthy run selection

For this demo project, `improved\_exp` is selected as the candidate production model.

We optimize for lower MSE, which measures prediction error between ground‑truth and model output.



> Note: This is a toy dataset for demonstrating MLOps workflow, not a high‑performance real‑world model.

