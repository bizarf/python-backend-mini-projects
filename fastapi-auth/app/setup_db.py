# run this script in python first to create the database file
import sqlite3

connection = sqlite3.connect("app/sql_app.db")
cursor = connection.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
"""
)

connection.commit()
connection.close()
