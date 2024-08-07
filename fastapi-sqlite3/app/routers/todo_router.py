import sqlite3
from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.schemas import TodoBase, TodoResponse

router = APIRouter()

DATABASE_URL = "sql_app.db"


def get_db():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row  # To get dictionary-like row objects
    return conn


@router.get("/todos", response_model=List[TodoResponse])
def get_todos(skip: int = 0, limit: int = 50):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todo LIMIT ? OFFSET ?", (limit, skip))
    rows = cursor.fetchall()
    conn.close()

    todos = [dict(row) for row in rows]
    return todos


@router.post("/todos", response_model=TodoResponse, status_code=201)
def create_todo(todo: TodoBase):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO todo (title, description) VALUES (?, ?)",
        (todo.title, todo.description),
    )
    conn.commit()
    new_id = cursor.lastrowid
    cursor.execute("SELECT * FROM todo WHERE id = ?", (new_id,))
    new_todo = cursor.fetchone()
    conn.close()
    return dict(new_todo)


@router.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo: TodoBase):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE todo SET title = ?, description = ? WHERE id = ?",
        (todo.title, todo.description, todo_id),
    )
    conn.commit()
    cursor.execute("SELECT * FROM todo WHERE id = ?", (todo_id,))
    updated_todo = cursor.fetchone()
    conn.close()
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return dict(updated_todo)


@router.delete("/todos/{todo_id}", response_model=dict)
def delete_todo(todo_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todo WHERE id = ?", (todo_id,))
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Todo not found")
    conn.close()
    return {"message": "Todo deleted successfully"}
