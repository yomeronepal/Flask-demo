from models import Todo
from settings import db
from exception import CustomException
from flask import jsonify
from interface import TodoInterface


class TodoRepo(TodoInterface):
    def get_todo_from_id(self, id: int):
        todo = Todo.query.get_or_404(id)
        return todo

    def get(self):
        todos = Todo.query.all()
        return jsonify([todo.serialize() for todo in todos])

    def create(self, content: str):
        todo = Todo(content=content)
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
