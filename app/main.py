from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.core.schema import get_schema_description
from app.core.llm import generate_sql
from app.core.validator import validate_sql, UnsafeQueryError
from app.core.executor import run_query

app = FastAPI(title="QueryGenie API")

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
def query(req: QueryRequest):
    schema = get_schema_description()
    sql = generate_sql(req.question, schema)

    try:
        validate_sql(sql)
    except UnsafeQueryError as e:
        raise HTTPException(status_code=400, detail=str(e))

    df = run_query(sql)
    return {
        "question": req.question,
        "sql": sql,
        "columns": list(df.columns),
        "rows": df.to_dict(orient="records"),
    }

@app.get("/health")
def health():
    return {"status": "ok"}