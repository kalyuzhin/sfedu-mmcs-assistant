from fastapi import APIRouter
from backend.api.routes import rag

api_router = APIRouter()


@api_router.get("/ping")
async def ping():
    return "pong"


api_router.include_router(rag.router)
