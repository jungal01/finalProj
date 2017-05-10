from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    year = db.Column(db.Integer(4))

    def __init__(self, username, email):
        self.title = title
        self.year = year

    def __repr__(self):
        return '<Title %r>' % self.title

class Moviecast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    year = db.Column(db.Integer(4))
    name = db.Column(db.String(100))
    type = db.Column(db.String(10))
    character = db.Column(db.String(100))
    n = db.Column(db.Integer(10))
