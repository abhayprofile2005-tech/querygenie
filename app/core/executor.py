from sqlalchemy import create_engine, text
import pandas as pd
import os

def run_query(sql: str) -> pd.DataFrame:
    engine = create_engine(os.getenv("DATABASE_URL"))
    with engine.connect() as conn:
        result = conn.execute(text(sql))
        rows = result.fetchall()
        cols = result.keys()
    return pd.DataFrame(rows, columns=cols)