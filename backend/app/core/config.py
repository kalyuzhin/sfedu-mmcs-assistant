from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal, Optional


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_ignore_empty=True,
        extra='ignore',
    )
    # HTTP
    HOST: str = '0.0.0.0'
    PORT: int = 8080

    # OpenAI
    OPENAI_TOKEN: str
    ENDPOINT: str
    MODEL_NAME: str = "gpt-4o-mini"
    EMBEDDING_MODEL: str = "text-embedding-3-small"

    # SBER
    SBER_TOKEN: str = None
    SYNTHESIZE_SBER_ENDPOINT: Optional[str] = None
    RECOGNIZE_SBER_ENDPOINT: Optional[str] = None
    CERTS: str

    # Tokens
    YANDEX_TOKEN: Optional[str] = None
    DEEPSEEK_TOKEN: Optional[str] = None

    # Database
    MILVUS_NAME: str
    COLLECTION_NAME: str
    PROJECT_NAME: str
    DATA_PATH: str = "./data"

    # Other
    ENVIRONMENT: Literal["production", "development", 'test'] = "development"


settings = Settings()
