# ResearchFlow AI Backend

Backend service for ResearchFlow AI.

## Setup

Create a virtual environment:

```bash
uv venv
```

Activate:

Windows

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
uv sync
```

Run (after Batch 1.2):

```bash
uv run uvicorn src.main:app --reload
```