from tqdm import tqdm
from pymilvus import MilvusClient
from shared.core.config import settings
from shared.api.embeddings import create_embeddings
from shared.scripts import get_data
import time

milvus_client = MilvusClient(uri=settings.MILVUS_NAME)


def create_collection() -> None:
    milvus_client.create_collection(collection_name=settings.COLLECTION_NAME,
                                    dimension=3072,
                                    metric_type="IP",
                                    )


def fill_embeddings(lines: list[str], collection_name: str = settings.COLLECTION_NAME) -> None:
    data = []
    for i, line in enumerate(tqdm(lines, desc="Creating embeddings")):
        data.append({"id": i, "vector": create_embeddings(line), "text": line})
        time.sleep(2)
    milvus_client.insert(collection_name=collection_name, data=data)


def     search_vectors(query: str):
    search_result = milvus_client.search(
        collection_name=settings.COLLECTION_NAME,
        data=[
            create_embeddings(query)
        ],
        limit=3,
        search_params={"metric_type": "IP", "params": {}},
        output_fields=["text"],
    )

    retrieved_lines_with_distances = [
        (res["entity"]["text"], res["distance"]) for res in search_result[0]
    ]
    result = "\n".join(
        [line_with_distance[0] for line_with_distance in retrieved_lines_with_distances]
    )
    return result
