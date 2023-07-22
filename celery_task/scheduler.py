from celery_task.task import add_numbers
from celery.schedules import crontab
from models import Todo
from settings import db


def get_event_schedules():
    # Retrieve event details from your data source
    events = [
        {"id": 1, "details": {"time": "11:19 PM", "date": "2023-07-04"}},
        {"id": 2, "details": {"time": "11:20 PM", "date": "2023-07-04"}}
        # Add more events as needed
    ]

    schedules = []
    for event in events:
        event_id = event["id"]
        event_details = event["details"]
        schedule = {
            "task": "your_task_name",
            "schedule": crontab(
                minute=event_details["time"].split(":")[1].split(" ")[0],
                hour=event_details["time"].split(":")[0],
                day_of_month=event_details["date"].split("-")[2],
                month_of_year=event_details["date"].split("-")[1],
                day_of_week="*",
            ),
            "args": (event_id, event_details),
        }
        schedules.append(schedule)

    return schedules
