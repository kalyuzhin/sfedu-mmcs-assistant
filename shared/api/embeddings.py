from shared.api import client, settings
from shared.scripts import process_tasks_by_batches


async def create_embeddings(text: str):
    return client.embeddings.create(input=text, model=settings.EMBEDDING_MODEL).data[0].embedding


async def generate_embeddings():
    pass
