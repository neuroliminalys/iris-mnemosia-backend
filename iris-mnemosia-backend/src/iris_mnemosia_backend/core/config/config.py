from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_path: str
    debug: bool
    cors_allowed_origins: list[str]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )
