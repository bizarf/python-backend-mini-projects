import sqlite3

connection = sqlite3.connect("sql_app.db")
cursor = connection.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT
)
"""
)

# Insert some sample data
cursor.execute(
    """
INSERT INTO todo (title, description) VALUES
('Sample Todo 1', 'Description for todo 1'),
('Sample Todo 2', 'Description for todo 2')
"""
)

connection.commit()
connection.close()
