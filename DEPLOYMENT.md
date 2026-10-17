# Deployment Guide

There are two ways to run this demo project:
1. Local: activate virtual environment, launch FastAPI service with uvicorn
2. Container: build Docker image from the provided Dockerfile, expose port 8000

Dataset is managed by DVC and stored on Azure Blob Storage:
- Use `dvc pull` to download the dataset locally
- Azure SAS token shall NOT be committed into the GitHub repository; please store it using GitHub Secrets

## Local Deployment Steps
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
dvc pull
uvicorn app.main:app --reload --port 8000
```