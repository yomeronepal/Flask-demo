from settings import db
from datetime import datetime


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(
        db.String(200),
    )
    description = db.Column(db.String(10000))
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    event_date = db.Column(db.DateTime)
    content = db.Column(db.String(10000))

    def __repr__(self):
        return "<Task %r>" % self.id

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "date_created": self.date_created.strftime("%d-%m-%y"),
            "description": self.description,
            "event_date": self.event_date,
            "content": self.content,
        }
