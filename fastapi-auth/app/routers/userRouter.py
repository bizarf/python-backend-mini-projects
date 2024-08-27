from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from app.models.User import User
from app.utils.auth import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
    get_current_user,
    get_password_hash,
    verify_password,
)
from app.utils.database import get_db
from app.utils.helper import get_user

router = APIRouter()


# type declaration for the signup post endpoint. tells the function what data type to expect
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

        # make variables with the info and put them into a tuple
        name = signup.name
        username = signup.username
        hashedPassword = get_password_hash(signup.password)

        values = (
            name,
            username,
            hashedPassword,
        )

        # safely replace the placeholders with the above tuple
        cursor.execute(
            "INSERT INTO users (name, username, password) VALUES (?, ?, ?)", values
        )
        # save the db
        cursor.close()
        conn.commit()
    except Exception:
        # if error then raise a http error to the client
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"success": False, "message": "Failed to add user"},
        )
    finally:
        # close the database
        conn.close()
    raise HTTPException(
        status_code=status.HTTP_201_CREATED,
        detail={"success": True, "message": "Sign up is successful"},
    )


@router.post("/login")
# OAuth2PasswordRequestForm collects the username and password for oauth2 password flow. depends function is needed as this a dependency class
async def post_login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        username = form_data.username
        password = form_data.password

        user = get_user(username=username)
        
        if not user or not verify_password(password, user["password"]):
            return HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"success": False, "message": "Incorrect username or password"},
            )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"success": False, "message": "Incorrect username or password"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # store the username in the jwt
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"success": True, "access_token": access_token}


# example of a protected route. will only display the message below if the user is logged in, or else it will return an unauthorised error
@router.get("/protected")
async def get_protected_endpoint(current_user: User = Depends(get_current_user)):    
    return {"message": f"Hello, {current_user["name"]}!"}
