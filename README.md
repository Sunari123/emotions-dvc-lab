# MLOps Final Project
MLOps project combining DVC data versioning, MLflow experiment tracking, FastAPI prediction service, Docker containerization and GitHub‑Actions CI/CD.

## Project branch strategy
Branching scheme follow the requirement: `feature/* → dev → staging → main`
- `feature/model‑dev`: feature development branch, contains full implementation of this practical work.
- `dev`: integration branch for merging finished features
- `staging`: pre‑production environment
- `main`: production stable branch

> Note: For this practical work, all development work is completed on branch `feature/model‑dev`. The branch workflow is documented below.

## Code lifecycle flow
`git commit` → GitHub‑Actions CI (lint + pytest + docker build) → merge to `dev` → merge to `staging` → CD builds staging docker image → merge to `main` → CD builds production docker image.

## Pipeline trigger rules
1. **CI Pipeline (ci.yml)**
- Trigger: push on `feature/model‑dev` / pull‑request to `dev`, `staging`, `main`
- Steps: ruff static linting → run pytest test suite → build docker image
- Rule: Pull Request cannot be merged if CI fails.

2. **CD Pipeline (cd.yml)**
- Trigger: push to branch `staging` or `main`
- Steps: read environment secrets from GitHub Secrets → generate `.env` → build corresponding docker image.

> Limitation note:
This project uses Azure blob storage managed by course teacher for DVC remote storage.
We cannot expose private Azure DVC credential inside public GitHub repository.
Therefore, CI environment cannot download model file `ml/registry/model.joblib` via `dvc pull`.
Two model‑related unit‑tests are marked as `skip` on CI.
**All four unit‑tests pass on local development environment.**

## Project structure
```
├── app/                # FastAPI web service
├── ml/                 # ML training, pipeline, registry and documentation
├── tests/              # Unit test suite
├── .github/workflows/  # CI / CD github actions yaml
├── Dockerfile          # slim inference dockerfile
├── .dockerignore
├── requirements.txt
├── requirements-dev.txt
├── DEPLOYMENT.md
``` 
## Key MLOps components
1. DVC: dataset version v1 / v2, stored on Azure remote storage, git only track `.dvc` pointer files. Git tags: `v1`, `v2`.
2. MLflow: 2 experiment runs: baseline model and improved tuned model. Log git‑sha, DVC dataset hash, hyper‑parameters, metrics and model artifacts.

## How to run locally
```powershell
# create venv
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt

# pull dataset from azure dvc remote
dvc pull

# start api service
uvicorn app.main:app --reload --port 8000

# run unit test
pytest tests/ -v0
```