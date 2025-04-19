import os
import time

from glob import glob
from tqdm import tqdm
from typing import List, Dict
from pymilvus import MilvusClient
from langchain.text_splitter import RecursiveCharacterTextSplitter
from shared.api.embeddings import create_embeddings
from shared.api import settings


class Milvus:
    def __init__(self, uri: str) -> None:
        if os.path.exists("milvus.db"):
            self.client = MilvusClient(uri=uri)
        else:
            self.client = MilvusClient(uri=uri)
            self.start()

    def create_collection(self, collection_name: str, dimension: int = 3072, metric_type: str = "IP") -> None:
        self.client.create_collection(collection_name=collection_name,
                                      dimension=dimension,
                                      metric_type=metric_type,
                                      )

    @staticmethod
    def get_data(data_path: str) -> str:
        for file_path in glob(f"{data_path}/*.txt", recursive=True):
            with open(file_path, "r") as file:
                text = file.read()

        return text

    @staticmethod
    def split_into_chunks(document: str, chunk_size: int = 500, chunk_overlap: int = 300) -> List[str]:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                                       chunk_overlap=chunk_overlap,
                                                       length_function=len,
                                                       separators=['\n\n', '\n', ' ', '. '])
        chunks = []
        chunks.extend(text_splitter.split_text(document))

        return chunks

    def fill_embeddings(self, lines: List[str], collection_name: str) -> None:
        data: List[Dict[str, List[float] | int | str]] = []
        try:
            for i, line in enumerate(tqdm(lines, desc="Creating embeddings")):
                data.append({"id": i, "vector": create_embeddings(line), "text": line})
                time.sleep(1)
        except Exception as e:
            raise e
        self.client.insert(collection_name=collection_name, data=data)

    def search_vectors(self, query: str, collection_name: str,
                       search_params: Dict[str, str] = None) -> str:
        if search_params is None:
            search_params = {"metric_type": "IP", "params": {}}
        search_result = self.client.search(
            collection_name=collection_name,
            data=[
                create_embeddings(query)
            ],
            limit=3,
            search_params=search_params,
            output_fields=["text"],
        )
        retrieved_lines_with_distances = [
            (res["entity"]["text"], res["distance"]) for res in search_result[0]
        ]
        result = "\n".join([line_with_distance[0] for line_with_distance in retrieved_lines_with_distances])

        return result

    def start(self):
        self.create_collection(settings.COLLECTION_NAME)
        text = self.get_data(settings.DATA_PATH)
        chunks = self.split_into_chunks(text)
        self.fill_embeddings(chunks, settings.COLLECTION_NAME)
