import os
from flask import Flask, render_template, request, redirect
from models import Todo

from settings import app, celery
from settings import db
from views import *
from api import *
from celery_task.task import add_numbers


@app.route("/", methods=["POST", "GET"])
def index():
    print(request.method)
    if request.method == "POST":
        test_content = request.form["content"]
        new_task = Todo(title=test_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "Exception"
    else:
        todo = Todo.query.all()
        print(todo)
    return render_template(
        "index.html",
        context={"todos": todo},
    )


@app.route("/delete/<int:id>/")
def delete(id):
    print(id)
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "There was problem deleting the content"


@app.route("/update/<int:id>/", methods=["GET", "POST"])
def update(id):
    task_to_update = Todo.query.get_or_404(id)
    if request.method == "POST":
        content = request.form["content"]
        task_to_update.content = content
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "Error While Updating"
    return render_template("update.html", context=task_to_update)


@app.route("/calendar/")
def calendar():
    return render_template("calendar_temp.html", context={})


# with app.app_context():
#     db.create_all()


if __name__ == "__main__":
    celery.tasks.register(add_numbers)
    app.run(debug=True, port=8000, host="0.0.0.0")
