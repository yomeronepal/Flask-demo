from models import Todo
from settings import db
# Perform a data migration to update existing data
def perform_data_migration():
    todos = Todo.query.all()
    for todo in todos:
        if not todo.title:
            todo.title = 'Todo'
    db.session.commit()

perform_data_migration()