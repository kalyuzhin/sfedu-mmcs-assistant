import os
import time
import random
import requests

from glob import glob
from tqdm import tqdm
from typing import List, Dict
from pymilvus import MilvusClient
from langchain.text_splitter import RecursiveCharacterTextSplitter, MarkdownTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from app.services.api.embeddings import create_embeddings_openai, create_embeddings_hf
from app.services.api import settings


class Milvus:
    def __init__(self, uri: str) -> None:
        if os.path.exists("milvus.db"):
            self.client = MilvusClient(uri=uri)
        else:
            self.client = MilvusClient(uri=uri)
            self.start()

    def create_collection(self, collection_name: str, dimension: int = 384, metric_type: str = "IP") -> None:
        self.client.create_collection(collection_name=collection_name,
                                      dimension=dimension,
                                      metric_type=metric_type,
                                      )
        index_params = self.client.prepare_index_params()
        index_params.add_index(
            field_name="vector",
            index_type="IVF_FLAT",
            metric_type=metric_type,
            params={
                "M": 16,
                "efConstruction": 40
            }
        )
        self.client.create_index(
            collection_name=collection_name,
            index_params=index_params,
        )
        # self.client.load_collection(collection_name=collection_name)

    @staticmethod
    def get_data(data_path: str) -> str:
        for file_path in glob(f"{data_path}/*.txt", recursive=True):
            with open(file_path, "r") as file:
                text = file.read()

        return text

    @staticmethod
    def split_into_chunks(document: str, chunk_size: int = 600, chunk_overlap: int = 100) -> List[str]:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                                       chunk_overlap=chunk_overlap,
                                                       length_function=len,
                                                       separators=['\n\n', '\n', ' '])
        chunks = []
        chunks.extend(text_splitter.split_text(document))

        return chunks

    @staticmethod
    def split_mds() -> List[str]:
        loader = DirectoryLoader(path=settings.DATA_PATH, glob='*.md')
        documents = loader.load()
        chunks: List[str] = []
        text_splitter = MarkdownTextSplitter(chunk_size=800, chunk_overlap=160, length_function=len)
        for doc in documents:
            chunks.extend(text_splitter.split_text(doc.page_content))
        print(f'{len(chunks)} chunks have been created')

        return chunks

    def fill_embeddings(self, lines: List[str], collection_name: str) -> None:
        data: List[Dict[str, List[float] | int | str]] = []
        try:
            for i, line in enumerate(lines):
                print(i)
                data.append({"id": i, "vector": create_embeddings_openai(line), "text": line})
                time.sleep(1 + random.random())
        except Exception as e:
            raise e
        finally:
            self.client.insert(collection_name=collection_name, data=data)

    def fill_embeddings_hf(self, lines: List[str], collection_name: str) -> None:
        embs = create_embeddings_hf(lines)
        data: List[Dict[str, List[float] | int | str]] = []
        for i, emb in enumerate(embs):
            data.append({"id": i, "vector": emb, "text": lines[i]})
        self.client.insert(collection_name=collection_name, data=data)

    def search_vectors(self, query: str, collection_name: str,
                       search_params: Dict[str, str] = None) -> str:
        if search_params is None:
            search_params = {"metric_type": "IP", "params": {"ef": 40}}
        search_result = self.client.search(
            collection_name=collection_name,
            data=[
                create_embeddings_hf(query)
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
        chunks = self.split_mds()
        self.fill_embeddings_hf(chunks, settings.COLLECTION_NAME)
