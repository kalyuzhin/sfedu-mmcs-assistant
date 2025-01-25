from fastapi import FastAPI
from shared.core.config import settings
from shared.backend.api.main import api_router

app = FastAPI(title=settings.PROJECT_NAME,
              )

app.include_router(api_router, prefix=settings.API_V1_STR)
