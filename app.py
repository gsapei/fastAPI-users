from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="API REST (fastAPI & mongoDB)",
    description="Endpoints for users",
    version="0.1"
)

app.include_router(user)