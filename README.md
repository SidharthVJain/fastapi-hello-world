# Minimal FastAPI App

A tiny FastAPI project with a single endpoint.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

## Test

- Root endpoint: http://127.0.0.1:8000
- Interactive docs: http://127.0.0.1:8000/docs

`GET /` returns:

```json
{"message": "Hello from my API"}
```
