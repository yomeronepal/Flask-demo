from settings import app
from flask import request, jsonify
from repo import TodoRepo

from celery_task.task import add_numbers
from celery_task.scheduler import get_event_schedules
from datetime import datetime, timedelta

from settings import celery
from celery.schedules import crontab
from datetime import datetime, timedelta
from datetime import datetime, timedelta
from airflow import DAG
from jinja2 import Template
import os


@app.route("/api/", methods=["GET", "POST"])
def todo():
    todo_repo = TodoRepo()
    time_now = datetime.now()
    event_time = datetime.now() + timedelta(seconds=10)
    # Generate unique dag_id
    dag_id = f"task_{datetime.now().strftime('%Y%m%d%H%M%S')}"

    # Load DAG template
    with open("dag_template.py", "r") as f:
        template = Template(f.read())

    # Populate the template with user inputs
    rendered_dag = template.render(dag_id=dag_id, user_datetime=event_time)

    # Save the generated DAG to the Airflow DAGs folder
    print(os.path.curdir)
    dag_path = f"./dags/{dag_id}.py"
    with open(os.path.expanduser(dag_path), "w") as f:
        f.write(rendered_dag)
    if request.method == "GET":
        todos = todo_repo.get()
        return todos, 200
    elif request.method == "POST":
        data = request.get_json()
        todo = todo_repo.create(
            data["title"], data["date"], data["description"], data["content"]
        )
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


@app.route("/health/", methods=["GET"])
def health_check():
    return {}, 200


@app.route("/check/", methods=["GET"])
def just_check():
    return {"uri": os.environ.get("DATABASE_URI")}, 200
