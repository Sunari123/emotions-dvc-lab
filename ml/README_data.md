\# Dataset Version Information

> Note: MS Azure storage account is NOT used in this project, to avoid unexpected cloud charges.

> DVC local cache `.dvc/cache` is used to demonstrate full data‑versioning workflow.

> Raw dataset is never pushed to GitHub; only `.dvc` pointer files are tracked by Git.



\## Dataset

Small toy CSV for workflow demo: columns id, value

\- v1 (git tag: v1): value=3

\- v2 (git tag: v2): value=4



Recover each version:

```bash

git checkout v1

dvc checkout



git checkout v2

dvc checkout

