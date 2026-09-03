from sqlalchemy import create_engine, inspect
import os

def get_schema_description(db_url: str = None) -> str:
    db_url = db_url or os.getenv("DATABASE_URL")
    engine = create_engine(db_url)
    inspector = inspect(engine)

    lines = []
    for table in inspector.get_table_names():
        cols = inspector.get_columns(table)
        col_desc = ", ".join(f"{c['name']} ({c['type']})" for c in cols)
        lines.append(f"Table {table}: {col_desc}")
    return "\n".join(lines)