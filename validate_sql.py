def validate_sql(query: str):
    forbidden = ["DROP", "DELETE", "UPDATE", "INSERT"]
    for word in forbidden:
        if word in query.upper():
            return False
    return True
