import requests
from typing import List
from app.services.api import client, settings

API_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"


def create_embeddings_openai(text: str) -> List[float]:
    try:
        return client.embeddings.create(input=text, model=settings.EMBEDDING_MODEL).data[0].embedding
    except Exception as e:
        raise e


def create_embeddings_hf(texts: List[str]) -> List[List[float]]:
    headers = {
        "Authorization": f"Bearer {settings.HF_TOKEN}",
    }
    response = requests.post(API_URL, json={"inputs": texts, "options": {"wait_for_model": True}}, headers=headers)

    return response.json()
