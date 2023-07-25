from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from celery import Celery
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


# from celery_task.task import add_numbers

database_uri = os.environ.get("DATABASE_URI")
# database_uri = "postgresql://postgres:postgres@postgres:5432/practise"
sql_lite_db_uri = "sqlite:///test.db"
app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
app.config["CELERY_BROKER_URL"] = "redis://localhost:6379/0"
app.config["result_backend"] = "redis://localhost:6379/0"
app.config["DEBUG"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)


celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])
celery.conf.update(app.config)
celery.conf.imports = ("celery_task.task",)
celery.conf.worker_pool = "eventlet"
