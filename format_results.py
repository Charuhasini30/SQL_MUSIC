def format_results(result):
    if "error" in result:
        return f"Error: {result['error']}"

    columns = result["columns"]
    rows = result["rows"]

    if not rows:
        return "No results found."

    formatted = ""
    for row in rows:
        formatted += ", ".join(f"{col}: {val}" for col, val in zip(columns, row))
        formatted += "\n"

    return formatted
