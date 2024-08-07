from pydantic import BaseModel

# this file is for type declaration. Similar to how TypeScript works


# this is the base model containing all the common fields that our todo app will either get, post, or put
class TodoBase(BaseModel):
    title: str
    description: str | None = None


# this is for creating new todo items. TodoBase is inherited here. we use pass, because we're not adding any new fields
class TodoCreate(TodoBase):
    pass


# it inherits the TodoBase. id is declared here as we're adding it to the table as it's the primary key.
class Todo(TodoBase):
    id: int

    # this is to tell Pydantic to support ORM models. A SQLAlchemy thing
    class Config:
        orm_mode = True
