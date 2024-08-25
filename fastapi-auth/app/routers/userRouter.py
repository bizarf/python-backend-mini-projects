from typing import Annotated

from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from pydantic import BaseModel

from app.utils.auth import get_password_hash
from app.utils.database import get_db

router = APIRouter()


class SignupBase(BaseModel):
    username: str
    password: str
    name: str


@router.post("/signup")
def post_sign_up(signup: SignupBase):
    try:
        # database connection
        conn = get_db()
        # database cursor
        cursor = conn.cursor()

        name = signup.name
        username = signup.username
        hashedPassword = get_password_hash(signup.password)

        values = (
            name,
            username,
            hashedPassword,
        )

        cursor.execute(
            "INSERT INTO users (name, username, password) VALUES (?, ?, ?)", values
        )
        conn.commit()
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"success": False, "message": "Failed to add user"},
        )
    finally:
        conn.close()
    raise HTTPException(
        status_code=status.HTTP_201_CREATED,
        detail={"success": True, "message": "Sign up is successful"},
    )


@router.get("/login")
def get_login():
    return
