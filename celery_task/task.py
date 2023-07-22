from settings import celery
from models import Todo
from settings import db


@celery.task
def add_numbers(x, y):
    todo = Todo(title="celery", event_date="05-07-23", description="description")
    db.session.add(todo)
    db.session.commit()

    return x + y


celery.tasks.register(add_numbers)
