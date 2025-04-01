# Backend Setup for OpenFootprint

This directory contains the FastAPI backend for the OpenFootprint application.

## Structure

- `app/`: Main application package
  - `api/`: API endpoints
  - `core/`: Core functionality and configuration
  - `db/`: Database models and connection
  - `models/`: Pydantic models for request/response
  - `services/`: Business logic
- `tests/`: Test cases
- `alembic/`: Database migrations

## Setup

1. Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Set up environment variables:
```
cp .env.example .env
# Edit .env with your configuration
```

4. Run migrations:
```
alembic upgrade head
```

5. Start the development server:
```
uvicorn app.main:app --reload
```
