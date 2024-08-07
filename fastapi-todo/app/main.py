from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import router as todoRouter

app = FastAPI()


# Cross Origin Resource Sharing. Need to set this if the frontend and backend are on different servers.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)


# loads all the paths from the router declared in that file. prefix sets how you want to the endpoints for that router to begin. here all endpoints will start with "/api"
app.include_router(todoRouter, prefix="/api")
