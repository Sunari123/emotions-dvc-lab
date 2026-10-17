# Dataset Version Information
> Note: This project uses the course‑provided MS Azure Blob Storage (account: wut2026, sub‑folder: group29) as DVC remote.
> SAS authentication token is stored locally inside `.dvc/config.local` and is NOT committed to Git.
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
