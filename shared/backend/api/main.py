from fastapi import APIRouter
from shared.backend.api.routes import rag

api_router = APIRouter()

api_router.include_router(rag.router)
