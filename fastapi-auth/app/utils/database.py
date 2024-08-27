import sqlite3

DATABASE_URL = "app/sql_app.db"


def get_db():
    conn = sqlite3.connect(DATABASE_URL)
    # returns fetchOne() and fetchAll() data as dicts
    conn.row_factory = sqlite3.Row
    return conn
