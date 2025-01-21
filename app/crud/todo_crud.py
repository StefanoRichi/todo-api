from app.models import Todo
from sqlalchemy.orm import Session
from app.schemas import TodoUpdate

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
        todo.due_date=data.duedate
        todo.title=data.title
        todo.detail=data.detail
        db.commit()
        db.refresh(todo)
        return "update Todo success"

    def delete_by_id(self, db: Session , todo: Todo  ):
        db.delete(todo)
        db.commit()
        return "Delete Todo Success"

todo_crud = CrudTodo()
