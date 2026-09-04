# 🧞 QueryGenie

Natural Language to SQL Query Generator — ask your database questions in plain English, get SQL and results instantly.

**🔗 Live Demo:** [querygenie-2005.streamlit.app](https://querygenie-2005.streamlit.app)

## What it does

QueryGenie lets you query a database using plain English instead of writing SQL. It reads your database schema, sends it along with your question to an LLM, validates the generated SQL for safety, and returns the results — all without needing to know SQL.

**Example:**

> "which customer has the highest order amount"

This generates a SQL query with a JOIN and GROUP BY, and returns the answer instantly.

## Architecture

```
User (Streamlit UI)
      │
      ▼
FastAPI Backend ──► Schema Extractor
      │
      ▼
LLM (Groq / Llama)
      │
      ▼
SQL Safety Validator
      │
      ▼
Query Executor ──► Database
      │
      ▼
Result back to UI
```

## Tech Stack

- **Backend:** FastAPI, SQLAlchemy
- **LLM:** Groq API (`openai/gpt-oss-20b`)
- **Frontend:** Streamlit
- **Database:** SQLite (swappable with Postgres/MySQL)
- **Testing:** Pytest
- **Deployment:** Docker, Render (backend), Streamlit Community Cloud (frontend)

## Key Features

- **Schema-aware prompting** — the LLM only sees the actual tables/columns, reducing hallucinated queries
- **Safety validation layer** — blocks `DROP`, `DELETE`, `UPDATE`, and multi-statement queries before execution; only `SELECT` is allowed
- **Tested** — validator logic covered by automated pytest tests

## Running Locally

```bash
git clone https://github.com/abhayprofile2005-tech/querygenie.git
cd querygenie
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python scripts/seed_db.py
```

Add your `GROQ_API_KEY` to a `.env` file, then start the backend:

```bash
uvicorn app.main:app --reload --port 8000
```

In a separate terminal, start the frontend:

```bash
streamlit run frontend/streamlit_app.py
```

## Running Tests

```bash
pytest tests/ -v
```
