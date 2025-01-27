import os , errno
from pydantic_settings import BaseSettings

try:
    os.makedirs("db-data")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

sqlite_file_name = "db-data/todo.db"

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Todo API"
    SQLALCHEMY_DATABASE_URI: str = (
        f"sqlite:///{sqlite_file_name}"
    )
    
settings = Settings()