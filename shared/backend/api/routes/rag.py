from fastapi import APIRouter
from typing import Any

router = APIRouter(prefix="/api/rag", tags=["rag"])


@router.post("/")
def rag_query() -> Any:
    pass
