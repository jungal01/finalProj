#!/usr/bin/python
# coding: utf-8
from flask import Flask, render_template, request
from sqlalchemy import create_engine, Column, Integer, Numeric, String, desc, asc, Table, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from json import load


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://swplgjqcmrfmmy:50c0e2902aca895e575bb703e08ad518c8a08b3bb17254be94b064aa9bd134db@ec2-54-235-120-39.compute-1.amazonaws.com:5432/d9moo2fhh5flfn'
# db = SQLAlchemy(app)
engine = create_engine('postgres://swplgjqcmrfmmy:50c0e2902aca895e575bb703e08ad518c8a08b3bb17254be94b064aa9bd134db@ec2-54-235-120-39.compute-1.amazonaws.com:5432/d9moo2fhh5flfn')
# Session = sessionmaker(bind=engine)
# session = Session()
#
# Base = declarative_base()

connection = engine.connect()
result = connection.execute("select title, year from title")
for row in result:
    print("title,year:", row['title'], row['year'])
connection.close()



@app.route('/')
@app.route('/index')
def index():
    # query = db.query(Title).filter_by(title='Inception').first()
    # titles = session.query(Title).order_by(asc(Title.title)).limit(10)
    connection = engine.connect()
    result = connection.execute("select title from title limit 10")
    alist = []
    for row in result:
        # print("title,year:", row['title'], row['year'])
        alist.append(row['title'])
    connection.close()


    # for item in titles:
    #     alist.append(str(item))
    return render_template('index.html', titleList=alist, title='Movies Search')

@app.route('/<string:movie>')
def moviesearch(movie):
    return movie


if __name__ == '__main__':
    app.run(debug=True)
