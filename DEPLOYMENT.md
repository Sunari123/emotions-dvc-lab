\# Deployment Guide



Two ways to run this demo project:

1\. Local: activate venv, launch FastAPI with uvicorn

2\. Container: build Docker image from provided Dockerfile, expose port 8000



Dataset is managed by DVC and stored on Azure Blob Storage:

\- Use `dvc pull` to get the dataset locally

\- Azure SAS token shall not be committed into GitHub repo, use GitHub Secrets

