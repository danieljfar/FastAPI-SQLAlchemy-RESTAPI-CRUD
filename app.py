from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="My first API",
    description="This is my first API",
    version="0.0.1",
    openapi_tags=[{
        "name": "users",
        "description": "Users routes"
    }]
)

app.include_router(user)