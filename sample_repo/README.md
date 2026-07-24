# Complaint Management Demo Repository

Small demo repository for teaching AI-augmented software engineering.

## Demo feature

A resident can reopen a closed complaint within seven calendar days when the issue is unresolved. A reopening reason is required. Only the complaint creator may reopen it.

## Project contents

- `app.py`: minimal Flask API with complaint status and reopen behaviour.
- `tests/test_complaints.py`: pytest tests for the reopen feature.
- `openapi.yaml`: API contract for the demo route.
- `requirements.txt`: runtime and test dependencies.
- `.gitignore`: common Python ignored files.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

On Windows PowerShell, you can also run:

```powershell
.\setup_windows.ps1
```

## Run tests

```bash
pytest
```

## Run the API

```bash
flask --app app run
```

Example request:

```bash
curl -X POST http://127.0.0.1:5000/complaints/cmp-100/reopen ^
  -H "Content-Type: application/json" ^
  -H "X-User-Id: resident-1" ^
  -d "{\"reason\":\"Leak is still visible after repair\"}"
```

## Teaching use

Use this repository to demonstrate:

- Asking AI to review requirements before coding.
- Creating API contracts before implementation.
- Writing tests before implementation.
- Reviewing generated code before accepting it.
- Inspecting a staged diff.
- Drafting a commit message and PR description.

## Disposable demo branch

Create a live-demo branch before editing:

```bash
git switch -c demo/reopen-complaint
```
