import os
import sqlite3
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

client = Groq(api_key=api_key)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_PATH = os.path.join(BASE_DIR, "dataset", "Chinook_Sqlite.sqlite")


def get_schema():
    """Return database schema as string."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    schema = ""

    for table in tables:
        table_name = table[0]
        schema += f"\nTable: {table_name}\n"

        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        for col in columns:
            schema += f" - {col[1]} ({col[2]})\n"

    conn.close()
    return schema


def validate_sql(query: str):
    if not query:
        raise ValueError("Generated SQL is empty.")

    forbidden = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER"]
    upper_query = query.upper().strip()

    for word in forbidden:
        if word in upper_query:
            raise ValueError("Unsafe SQL query detected.")

    if not upper_query.startswith("SELECT"):
        raise ValueError(f"Only SELECT queries allowed. Got: {query}")


def execute_sql(query: str):
    """Execute SQL query and return results."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]

    conn.close()
    return columns, rows


def format_results(columns, rows):
    """Format SQL results nicely."""
    if not rows:
        return "No results found."

    # If single value (like COUNT)
    if len(columns) == 1 and len(rows) == 1:
        return f"{columns[0]}: {rows[0][0]}"

    result = ""
    result += " | ".join(columns) + "\n"
    result += "-" * 40 + "\n"

    for row in rows:
        result += " | ".join(str(item) for item in row) + "\n"

    return result


def generate_sql(question: str, schema: str):
    prompt = f"""
You are a strict SQL generator.

Use ONLY the table and column names EXACTLY as provided in the schema.
Do NOT invent or pluralize table names.

Database Schema:
{schema}

Question:
{question}

Rules:
- Only SELECT queries.
- No explanations.
- No markdown.
- Return only SQL.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You generate SQL queries only."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
    )

    if not completion.choices:
        raise ValueError("No response from LLM.")

    content = completion.choices[0].message.content

    if content is None:
        raise ValueError("LLM returned empty content.")

    sql = content.strip()

    # Remove markdown if present
    if "```" in sql:
        sql = sql.split("```")[1]

    sql = sql.replace("sql", "").strip()

    print("Generated SQL:", sql)

    return sql


def run_agent(question: str):
    """Main agent pipeline."""
    try:
        schema = get_schema()
        sql_query = generate_sql(question, schema)

        validate_sql(sql_query)

        columns, rows = execute_sql(sql_query)
        formatted = format_results(columns, rows)

        return {
            "question": question,
            "sql_query": sql_query,
            "answer": formatted
        }

    except Exception as e:
        return {
            "error": str(e)
        }
print("Database path:", os.path.abspath(DATABASE_PATH))
print("File exists:", os.path.exists(DATABASE_PATH))
