from openai import OpenAI
from shared.core.config import settings

client = OpenAI(
    base_url=settings.ENDPOINT,
    api_key=settings.API_TOKEN,
)


def make_query():
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "",
            },
            {
                "role": "user",
                "content": "",
            }
        ],
        model=settings.MODEL_NAME,
        stream=True
    )

    for update in response:
        if update.choices[0].delta.content:
            print(update.choices[0].delta.content, end="")
