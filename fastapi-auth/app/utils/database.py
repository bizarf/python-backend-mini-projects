import sqlite3

DATABASE_URL = "app/sql_app.db"


def get_db():
    conn = sqlite3.connect(DATABASE_URL)
    # gets a dictionary-like row of objects
    conn.row_factory = sqlite3.Row
    return conn
