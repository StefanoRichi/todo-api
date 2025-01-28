from app.models import Todo
from sqlalchemy.orm import Session
from app.schemas import TodoUpdate , TodoCreate

class CrudTodo:
    def get_all(self, db: Session  ):
        return db.query(Todo).all()
    
    def get_by_id(self, db: Session , id :int ):
        return (
            db.query(Todo)
            .filter(
                Todo.id == id
            )
            .first()
        )

    def get_by_title(self, db: Session , title : str ):
        search = "%{}%".format(title)
        return (
            db.query(Todo)
            .filter(
                Todo.title.like(search)
            )
            .all()
        ) 
    
    def update_by_id(self, db: Session , todo: Todo , data: TodoUpdate  ):
        todo.due_date=data.due_date # type: ignore
        todo.title=data.title # type: ignore
        todo.detail=data.detail # type: ignore
        todo.is_done=data.is_done # type: ignore
        db.commit()
        db.refresh(todo)
        return {"status": "Update Success"}

    def insert_todo(self, db: Session , data: TodoCreate ):
        todo = Todo(
        title=data.title,
        detail=data.detail,
        due_date=data.due_date
        )
        db.add(todo)
        db.commit()
        db.refresh(todo)
        return {"status": "Create Success"}
    

    def delete_by_id(self, db: Session , todo: Todo  ):
        db.delete(todo)
        db.commit()
        return {"status": "Delete Success"}

todo_crud = CrudTodo()
