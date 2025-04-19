from typing import List
from shared.api import client, settings


def create_embeddings(text: str) -> List[float]:
    try:
        return client.embeddings.create(input=text, model=settings.EMBEDDING_MODEL).data[0].embedding
    except Exception as e:
        raise e
