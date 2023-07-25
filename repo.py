from models import Todo
from settings import db
from exception import CustomException
from flask import jsonify
from interface import TodoInterface
from datetime import datetime


class TodoRepo(TodoInterface):
    def get_todo_from_id(self, id: int):
        todo = Todo.query.get_or_404(id)
        return todo

    def get(self):
        todos = Todo.query.order_by(Todo.date_created).all()
        return jsonify([todo.serialize() for todo in todos])

    def create(self, title: str, date_created, description, content):
        todo = Todo(
            title=title,
            event_date=datetime.strptime(date_created, "%d/%m/%Y"),
            description=description,
            content=content,
        )
        try:
            db.session.add(todo)
            db.session.commit()
        except:
            raise CustomException("Error Creating Todo")
        return todo

    def delete(self, id: int) -> None:
        todo = self.get_todo_from_id(id)
        try:
            db.session.delete(todo)
            db.session.commit()
        except:
            raise CustomException("Error While deleting todo")

    def update(self, id: int, content: str):
        todo = self.get_todo_from_id(id)
        todo.content = content
        try:
            db.session.commit()
        except:
            raise CustomException("Error While Updating")
        return todo
