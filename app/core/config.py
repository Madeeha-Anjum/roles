from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=(".env"),
        env_file_encoding="utf-8",
    )
    PROJECT_NAßME: str = "FastAPI Application"
    ENVIRONMENT: str 
    PG_DB_NAME: str 
    PG_USERNAME: str 
    PG_PASSWORD: str 
    PG_HOSTNAME: str #db = hostname for docker container. needs to match if calling from another container.
    PG_PORT: int 
    DEBUG: bool = False
    
    @property
    def DIRECT_DATABASE_URL(self) -> str:
        return (
            f"postgresql+psycopg://{self.PG_USERNAME}:{self.PG_PASSWORD}"
            f"@{self.PG_HOSTNAME}:{self.PG_PORT}/{self.PG_DB_NAME}"
        )


settings = Settings()
