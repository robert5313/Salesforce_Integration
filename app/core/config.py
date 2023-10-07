from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_key: str
    app_name: str
    app_description: str
    app_version: str

    model_config = SettingsConfigDict(env_file="prod.env", env_file_encoding="utf-8")


settings = Settings(_env_file="prod.env", _env_file_encoding="utf-8")
