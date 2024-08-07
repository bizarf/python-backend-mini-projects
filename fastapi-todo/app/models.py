# import the field types for tables
from sqlalchemy import Column, Integer, String

# this would be used if i had more than one table which had a relation with another table. needed for primary and foreign keys
from sqlalchemy.orm import relationship

from .database import Base


# make a class to define the table
class Todo(Base):
    __tablename__ = "todos"

    # table columns. index is used for improving performance for queries for that column at the cost of space
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
