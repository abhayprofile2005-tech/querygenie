import re

BLOCKED_KEYWORDS = [
    "INSERT", "UPDATE", "DELETE", "DROP", "ALTER",
    "TRUNCATE", "CREATE", "GRANT", "REVOKE", "ATTACH", "PRAGMA"
]

class UnsafeQueryError(Exception):
    pass

def validate_sql(sql: str) -> str:
    if sql.startswith("ERROR:"):
        raise UnsafeQueryError(sql)

    upper = sql.upper()
    if not upper.strip().startswith("SELECT"):
        raise UnsafeQueryError("Only SELECT queries are allowed.")

    for word in BLOCKED_KEYWORDS:
        if re.search(rf"\b{word}\b", upper):
            raise UnsafeQueryError(f"Blocked keyword detected: {word}")

    if ";" in sql.strip()[:-1]:  # multiple statements ek saath nahi
        raise UnsafeQueryError("Multiple statements are not allowed.")

    return sql