import sqlite3
import os

DB_PATH = "dataset/Chinook_Sqlite.sqlite"

def inspect_database():
    print("Absolute path:", os.path.abspath(DB_PATH))
    print("File exists:", os.path.exists(DB_PATH))
    print("File size (bytes):", os.path.getsize(DB_PATH))

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    print("Tables found:", tables)

    conn.close()


if __name__ == "__main__":
    inspect_database()
