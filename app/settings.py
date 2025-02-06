from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        # `.env.prod` takes priority over `.env`
        env_file=('.env', '.env.prod'),
        env_file_encoding='utf-8')
    ENVIRONMENT: str
    HOST: str
    PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str


settings = Settings()

DIRECT_DATABASE_URL = f'postgresql://{settings.DB_USER}:{settings.DB_PASS}@{settings.HOST}:{settings.PORT}/{settings.DB_NAME}'
