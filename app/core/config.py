import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

path = "%s/.env" % os.getcwd()
load_dotenv(dotenv_path=path)

PG_USER = os.getenv("POSTGRES_USER", "")
PG_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")
PG_HOST = os.getenv("POSTGRES_HOST", "")
PG_DB = os.getenv("POSTGRES_DB", "")

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Todo API"
    SQLALCHEMY_DATABASE_URI: str = (
        f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}/{PG_DB}"
    )
    
settings = Settings()