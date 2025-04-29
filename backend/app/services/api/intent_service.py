from openai import OpenAI

from app.services.api import settings


class IntentService:
    def __init__(self, client: OpenAI):
        self.client = client

    def get_intent(self, user_question: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=settings.MODEL_NAME,
                messages=[
                    {"role": "user",
                     "content": f"""
                 Задача: Извлеки ключевые слова из следующего вопроса. Не отвечай ни на что другое, кроме ключевых слов.
                 Вопрос: {user_question}"""}
                ],
                max_tokens=100)
        except Exception as ex:
            return f"Ошибка запроса к LLM: {str(ex)}"

        return response.choices[0].message.content
