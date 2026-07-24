# Live Demo Checklist

## Before students enter

- Open this folder.
- Open `sample_repo/`.
- Open `sample_repo/app.py`.
- Open `sample_repo/tests/test_complaints.py`.
- Open `sample_repo/openapi.yaml`.
- Open `demo_data/reopen_complaint_story.md`.
- Open the `prompts/` folder.
- Start with a clean terminal in `sample_repo/`.

## Commands to verify

```bash
python --version
git --version
pytest --version
ruff --version
```

If `pytest` or `ruff` are missing, run this from `sample_repo/`:

```powershell
.\setup_windows.ps1
```

## Demo commands

```bash
git status
git switch -c demo/reopen-complaint
pytest
ruff check .
git diff
git add app.py tests/test_complaints.py openapi.yaml
git diff --staged
```

## What to point out

- The AI is asked for one artifact at a time.
- Tests and API contract come before implementation.
- The human decides which assumptions become product policy.
- The human reviews every generated change.
- Git history should make the work understandable.
