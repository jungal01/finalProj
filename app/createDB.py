from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    year = db.Column(db.Integer(4), unique=True)

    def __init__(self, username, email):
        self.title = title
        self.year = year

    def __repr__(self):
        return '<Title %r>' % self.title
