from fastapi import APIRouter 
from app.api.endpoint import todo

api_router = APIRouter()

api_router.include_router(todo.router, prefix="/todo" ,tags=["Todo"])