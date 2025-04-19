from shared.speech.speech import recognize_speech_sr, synthesize_speech_pyttsx, synthesize_speech_gtts
from shared.api.query import make_query, make_query_ru
from shared.db.milvus import search_vectors


def run():
    flag = input()
    query = recognize_speech_sr()
    print(f"{query}")
    context = search_vectors(query)
    print(f"Контекст:\n{context}\n")
    output = make_query_ru(query, context)
    synthesize_speech_pyttsx(output)
    # synthesize_speech_gtts(output)


def main() -> None:
    while True:
        run()


if __name__ == "__main__":
    main()
