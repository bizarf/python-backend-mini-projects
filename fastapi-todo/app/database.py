from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# declare sqlite file
DATABASE_URL = "sqlite:///./sql_app.db"

# creates a connection engine for an SQLite database using SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# class which is used to create database models
Base = declarative_base()


# dependency function to get to the database. use in routers
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
