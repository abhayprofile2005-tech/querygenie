# 🧞 QueryGenie

Natural Language to SQL Query Generator — ask your database questions in plain English, get SQL and results instantly.

**🔗 Live Demo:** [querygenie-2005.streamlit.app](https://querygenie-2005.streamlit.app)

## What it does

QueryGenie lets you query a database using plain English instead of writing SQL. It reads your database schema, sends it along with your question to an LLM, validates the generated SQL for safety, and returns the results — all without needing to know SQL.

**Example:**

> "top 5 artists by number of albums"

This generates a query with a JOIN, GROUP BY, and LIMIT, and returns results like Iron Maiden, Led Zeppelin, Deep Purple instantly.

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
- **Database:** SQLite — using the [Chinook sample database](https://github.com/lerocha/chinook-database) (digital music store data: artists, albums, tracks, customers, invoices, employees)
- **Testing:** Pytest
- **Deployment:** Docker, Render (backend), Streamlit Community Cloud (frontend)

## Key Features

- **Schema-aware prompting** — the LLM only sees the actual tables/columns, reducing hallucinated queries
- **SQLite-specific prompting** — enforces `LIMIT` instead of dialect-specific syntax like `TOP`
- **Safety validation layer** — allows only `SELECT` and `WITH` (CTE) queries; blocks `DROP`, `DELETE`, `UPDATE`, and multi-statement queries before execution
- **Tested** — validator logic covered by automated pytest tests

## Example Queries to Try

- "top 5 artists by number of albums"
- "total sales by country"
- "which customer has spent the most money"
- "which genre generates the most revenue"
- "which employee has the most customers"

## Running Locally

```bash
git clone https://github.com/abhayprofile2005-tech/querygenie.git
cd querygenie
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file with:

```
GROQ_API_KEY=your_groq_api_key
DATABASE_URL=sqlite:///./data/chinook.sqlite
```

Then start the backend:

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