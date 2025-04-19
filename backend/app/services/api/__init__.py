from openai import OpenAI
from backend.app.core.config import settings

client = OpenAI(
    base_url=settings.ENDPOINT,
    api_key=settings.OPENAI_TOKEN,
)
