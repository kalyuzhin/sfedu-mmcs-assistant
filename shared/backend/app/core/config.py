from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_ignore_empty=True,
        extra='ignore',
    )

    HOST: str = '0.0.0.0'
    PORT: int = 9000

    ENVIRONMENT: Literal["production", "development", 'test'] = 'dev'


settings = Settings()
