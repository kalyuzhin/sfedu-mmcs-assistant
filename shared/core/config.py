from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_ignore_empty=True,
        extra='ignore',
    )

    API_TOKEN: str

    ENDPOINT: str

    MODEL_NAME: str = "gpt-4o-mini"

    EMBEDDING_MODEL: str = "text-embedding-3-small"

    MILVUS_NAME: str

    COLLECTION_NAME: str

    PROJECT_NAME: str

    ENVIRONMENT: Literal["production", "development"] = "development"


settings = Settings()
