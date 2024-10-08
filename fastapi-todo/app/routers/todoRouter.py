from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.TodoModel import Todo
from app.schemas.todoSchemas import TodoBase

# groups all of the path operations into one. this is for use in the main.py file
router = APIRouter()


# get route
@router.get("/")
# the function goes here and will run when this route is accessed.
# db is a parameter, and the type (Session) tells the function what sort of data db will give. Depends tells FastAPI to run the function get_db which starts a database session
# skip and limit are pagination features. skip tells where to start, and limit is the maximum results returned. the api endpoint would be something like "/api/?limit=50&skip=50" for the second page, and "/api/?limit=50&skip=100" for the third page
def get_todo(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    # query the model, Todo which is holds the name of the table. all() is the equivalent of SELECT *.
    todos = db.query(Todo).offset(skip).limit(limit).all()
    return todos


# post route
@router.post("/")
# the request data type is set to TodoBase which contains the data fields with their types. this is how data is validated
def post_todo(request: TodoBase, db: Session = Depends(get_db)):
    # declare a variable with the table model.
    todo = Todo(title=request.title, description=request.description)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@router.delete("/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()

    return {"message": "Todo deleted successfully"}


@router.put("/{id}")
def update_todo(id: int, request: TodoBase, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.title = request.title
    todo.description = request.description
    db.commit()
    db.refresh(todo)
    return todo
