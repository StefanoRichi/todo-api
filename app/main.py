from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import api_router
from app.db.database import create_db_and_tables

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_V1_STR
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"message": "Hello API"}
