from shared.api import client, settings


def create_embeddings(text: str):
    return client.embeddings.create(input=text, model=settings.EMBEDDING_MODEL).data[0].embedding
