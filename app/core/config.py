import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

path = "%s/.env" % os.getcwd()
load_dotenv(dotenv_path=path)

sqlite_file_name = "todo.db"

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Todo API"
    SQLALCHEMY_DATABASE_URI: str = (
        f"sqlite:///{sqlite_file_name}"
    )
    
settings = Settings()