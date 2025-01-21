from shared.speech.speech import recognize_speech, synthesize_speech
from shared.api.query import make_query
from shared.api.embeddings import create_embeddings
from shared.db.milvus import search_vectors, create_collection, fill_embeddings
from shared.scripts import get_data


def main() -> None:
    # data = get_data()
    # create_collection()
    # fill_embeddings(data)
    query = recognize_speech()
    print(f"{query}")
    context = search_vectors(query)
    print(f"{context}\n\n")
    output = make_query(query, context)
    synthesize_speech(output)


if __name__ == "__main__":
    main()
