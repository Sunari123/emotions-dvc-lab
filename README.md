\# Emotions‑MLOps‑Demo

End‑to‑end MLOps workflow practice: Git + DVC + MLflow + FastAPI + Pytest + Docker + GitHub Actions.



Note: DVC uses local cache (instead of Azure) for safety, no cloud subscription.



Project structure

\- data/: dataset managed by DVC

\- ml/: data pipeline, training script, config, model registry

\- app/: FastAPI prediction service

\- tests/: validation \& test suite

\- .github/workflows/: CI workflow definition

