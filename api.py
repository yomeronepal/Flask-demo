from settings import app
from flask import request, jsonify
from repo import TodoRepo


@app.route("/api/", methods=["GET", "POST"])
def todo():
    todo_repo = TodoRepo()
    if request.method == "GET":
        todos = todo_repo.get()
        return todos, 200
    elif request.method == "POST":
        data = request.get_json()
        todo = todo_repo.create(data["content"])
        return jsonify(todo.serialize()), 201


@app.route("/api/todo/<int:id>/", methods=["DELETE", "PUT", "GET"])
def todo_create_update(id):
    todo_repo = TodoRepo()
    if request.method == "DELETE":
        todo_repo.delete(id)
        return {}, 200
    elif request.method == "PUT":
        data = request.get_json()
        todo = todo_repo.update(id, data["content"])
        return jsonify(todo.serialize())
    elif request.method == "GET":
        todo = todo_repo.get_todo_from_id(id)
        return jsonify(todo.serialize()), 200
