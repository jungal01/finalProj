from flask import Flask, render_template, request
import sqlalchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import createDB


@app.route('/')

@app.route('/movie')

@app.route('/history', method=['GET'])

@app.route('/history', method=['DELETE'])

@app.route('/history/movie')
