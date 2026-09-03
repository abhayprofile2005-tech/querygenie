import os
from groq import Groq
from .prompts import SYSTEM_PROMPT, build_user_prompt

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_sql(question: str, schema: str) -> str:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        max_tokens=300,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(question, schema)}
        ],
    )
    sql = response.choices[0].message.content.strip()
    sql = sql.replace("```sql", "").replace("```", "").strip()
    return sql