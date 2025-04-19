from fastapi import FastAPI
from shared.core.config import settings
from shared.backend.app.api.main import api_router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix='/api/v1')
