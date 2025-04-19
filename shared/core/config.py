from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_ignore_empty=True,
        extra='ignore',
    )

    OPENAI_TOKEN: str

    ENDPOINT: str

    MODEL_NAME: str = "gpt-4o-mini"

    EMBEDDING_MODEL: str = "text-embedding-3-small"

    MILVUS_NAME: str

    COLLECTION_NAME: str

    PROJECT_NAME: str

    ENVIRONMENT: Literal["production", "development"] = "development"

    SBER_TOKEN: str

    YANDEX_TOKEN: str

    DEEPSEEK_TOKEN: str


settings = Settings()
