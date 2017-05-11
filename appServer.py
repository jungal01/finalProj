from flask import Flask, render_template, request
import sqlalchemy
from sqlalchemy.orm import relationship, sessionmaker

app = Flask(__name__)

engine = create_engine('sqlite:///:memory', echo=True)
db = sessionmaker(bind=engine)

@app.route('/')

@app.route('/movie')

@app.route('/history', method=['GET'])

@app.route('/history', method=['DELETE'])

@app.route('/history/movie')
