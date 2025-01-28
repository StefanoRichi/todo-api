from fastapi import APIRouter , Depends, HTTPException
from datetime import date,datetime
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.todo import Todo
from app.schemas import TodoCreate , TodoUpdate
from app.crud import todo_crud

router = APIRouter()

@router.get("")
def get_todos(
     db: Session = Depends(get_db)
):  
    todo_obj = todo_crud.get_all(db)
    if not todo_obj:
        raise HTTPException(status_code=404, detail="Data not found!")
    return todo_obj

@router.get("/{id:int}")
def get_todos_by_id(
     id: int,
     db: Session = Depends(get_db)
):  
    todo_obj = todo_crud.get_by_id(db,id)
    if not todo_obj:
        raise HTTPException(status_code=404, detail="Data not found!")
    return todo_obj

@router.get("/{title:str}")
def get_todos_by_title(
     title: str,
     db: Session = Depends(get_db)
):  
    todo_obj = todo_crud.get_by_title(db,title)
    if not todo_obj:
        raise HTTPException(status_code=404, detail="Data not found!")
    return todo_obj

@router.post("/create")
def create_todos(
    data: TodoCreate,
    db: Session = Depends(get_db),
    ):
    todo_obj = todo_crud.insert_todo(db,data)
    return todo_obj

@router.put("/{id:int}")
def update_todos(
    id: int,
    data: TodoUpdate,
    db: Session = Depends(get_db)
    ):
  
    todo_obj = todo_crud.get_by_id(db,id)
    if todo_obj:
        result = todo_crud.update_by_id(db,todo_obj,data)
    else:
        raise HTTPException(status_code=404, detail="Data not found!")
    
    return {"message": result}

@router.delete("/{id:int}")
def delete_todos(
    id: int,
    db: Session = Depends(get_db)
    ):
    todo_obj = todo_crud.get_by_id(db,id)
    if todo_obj:
        result = todo_crud.delete_by_id(db,todo_obj)
    else:
        raise HTTPException(status_code=404, detail="Data not found!")
    return {"message": result}

