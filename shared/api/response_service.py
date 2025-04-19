from openai import OpenAI
from shared.api import settings


class ResponseService:
    def __init__(self, client: OpenAI):
        self.client = client

    def make_response(self, context: str, query: str) -> str:
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": """
                    Ты умный голосовой помощник, работающий для студентов и преподавателей МехМата ЮФУ. 
    Твоя цель — давать точные, краткие и полезные ответы на вопросы, используя только предоставленный контекст. 
    Если ответа в предоставленном контексте нет, честно скажи это. 
    Указывай на источники в ответе, если это возможно, и избегай фантазирования."""
                    },
                    {
                        "role": "user",
                        "content": f"""
                            Контекст:
                            ``` 
                            {context}
                            ```
                            Запрос: {query}""",
                    }
                ],
                model=settings.MODEL_NAME,
                # stream=True,
                temperature=0.5,
                top_p=1.0,
                max_tokens=1000,
            )
        except Exception as ex:
            return f"Ошибка запроса к LLM: {str(ex)}"

        return response.choices[0].message.content
