from shared.api import client, settings


def make_query(query: str, context: list[str] = None) -> str:
    output = ""
    response = client.chat.completions.create(
        messages=[
            {"role": "system",
             "content": """
             Human: You are an AI assistant. You are able to find answers to the questions from the contextual 
             passage snippets provided."""},
            {
                "role": "user",
                "content": f"""
                Context:
                ``` 
                {context}
                ```
                
                Query: {query}""",
            }
        ],
        model=settings.MODEL_NAME,
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        # stream=True,
    )
    print("Ответ: \n")

    # for update in response:
    #     if update.choices[0].delta.content:
    #         output += update.choices[0].delta.content
    #         print(update.choices[0].delta.content, end="")
    output = response.choices[0].message.content
    print(output)
    return output


def make_query_ru(query: str, context: list[str] = None) -> str:
    output = ""
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""
                На основе следующего контекста, ответьте на запрос:
                ``` 
                {context}
                ```

                Запрос: {query}""",
            }
        ],
        model=settings.MODEL_NAME,
        # stream=True,
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
    )
    print("Ответ: \n")

    # for update in response:
    #     if update.choices[0].delta.content:
    #         output += update.choices[0].delta.content
    #         print(update.choices[0].delta.content, end="")
    output = response.choices[0].message.content
    print(output)
    return output
