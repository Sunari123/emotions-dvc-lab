# Dataset Version Information
> Note: MS Azure storage account is used in this project, to avoid unexpected cloud charges.
> DVC local cache `.dvc/cache` is used to demonstrate full data‑versioning workflow.
> Raw dataset is never pushed to GitHub; only `.dvc` pointer files are tracked by Git.

## Dataset
Small toy CSV for workflow demo: columns id, value

- v1 (git tag: v1, commit hash: 726693a): value=3
- v2 (git tag: v2, commit hash: 3cca96b): value=4

Changes from v1 to v2: Modified one sample's value from 3 to 4 to simulate dataset iterative update.

Recover each version:
```bash
git checkout v1
dvc checkout

git checkout v2
dvc checkout
