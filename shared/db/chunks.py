from typing import List
from langchain.text_splitter import TextSplitter
from langchain.schema.document import Document


def split_into_chunks(documents: List[Document], chunk_size: int, chunk_overlap: int) -> List[str]:
    text_splitter = TextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap, length_function=len)
    chunks = []
    for document in documents:
        chunks.extend(text_splitter.split_text(document.page_content))

    return chunks
