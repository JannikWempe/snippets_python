# app.py or __init__.py or whatever...

# ...
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask()
db = SQLAlchemy(app)
# ...

# models.py
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100), unique=True)

# command line
from app import db
from models import User

# insert
user = User(name="Max")
db.session.add(user)
db.session.commit()

# update
max = User.query.filter_by(name="Max").first()
max.name = "Maxi"
db.session.commit()

# delete
maxi = db.session.query(User).filter_by(username="maxi").first()
db.session.delete(user)
db.session.commit()
# CAUTION: the following is not recommended, since it doesn't trigger cascading
# db.session.query(User).filter_by(username="maxi").delete()
