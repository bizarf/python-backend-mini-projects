from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.userRouter import router as userRouter

app = FastAPI()

# Cross Origin Resource Sharing. Need to set this if the frontend and backend are on different servers.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)


@app.get("/")
def root():
    return {"message": "Welcome to the API"}


# routers
app.include_router(userRouter, prefix="/api/user")
