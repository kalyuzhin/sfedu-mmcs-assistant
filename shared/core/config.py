from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_ignore_empty=True,
        extra='ignore',
    )

    # OpenAI
    OPENAI_TOKEN: str
    ENDPOINT: str
    MODEL_NAME: str = "gpt-4o-mini"
    EMBEDDING_MODEL: str = "text-embedding-3-small"

    # SBER
    SBER_TOKEN: str
    SYNTHESIZE_SBER_ENDPOINT: str
    RECOGNIZE_SBER_ENDPOINT: str
    CERTS: str

    # Tokens
    YANDEX_TOKEN: str
    DEEPSEEK_TOKEN: str

    # Database
    MILVUS_NAME: str
    COLLECTION_NAME: str
    PROJECT_NAME: str
    DATA_PATH: str = "./data"

    # Other
    ENVIRONMENT: Literal["production", "development"] = "development"


settings = Settings()
