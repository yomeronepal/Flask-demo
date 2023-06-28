from flask import Flask
from flask_sqlalchemy import SQLAlchemy

database_uri = "postgresql://postgres:postgres@localhost:5432/practise"
# database_uri = "postgresql://postgres:postgres@postgres:5432/practise"
sql_lite_db_uri = "sqlite:///test.db"
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
db = SQLAlchemy(app)
