from openai import OpenAI
from shared.core.config import settings

client = OpenAI(
    base_url=settings.ENDPOINT,
    api_key=settings.API_TOKEN,
)


def make_query(query: str, context: str = None):
    response = client.chat.completions.create(
        messages=[
            {"role": "system",
             "content": """
             Human: You are an AI assistant. You are able to find answers to the questions from the contextual 
             passage snippets provided."""},
            {
                "role": "user",
                "content": f"""
                Context: {context}
                
                Query: {query}""",
            }
        ],
        model=settings.MODEL_NAME,
        stream=True
    )

    for update in response:
        if update.choices[0].delta.content:
            print(update.choices[0].delta.content, end="")
