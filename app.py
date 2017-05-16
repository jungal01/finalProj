#!/usr/bin/python
# coding: utf-8
from flask import Flask, render_template, request
from sqlalchemy import create_engine, Column, Integer, Numeric, String, desc, asc, Table, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from json import load


app = Flask(__name__)
engine = create_engine('postgres://swplgjqcmrfmmy:50c0e2902aca895e575bb703e08ad518c8a08b3bb17254be94b064aa9bd134db@ec2-54-235-120-39.compute-1.amazonaws.com:5432/d9moo2fhh5flfn')

# Now, we can do queries using connection.execute("SQL_QUERY")
# Use indexing to get the column value from result (see example in index())
@app.route('/')
@app.route('/index')
def index():
    connection = engine.connect()
    result = connection.execute("select title from title limit 10")
    alist = []
    for row in result:
        alist.append(row['title'])
    connection.close()


    # for item in titles:
    #     alist.append(str(item))
    return render_template('index.html', titleList=alist, title='Movies Search')

@app.route('/<string:movie>')
def moviesearch(movie):
    if movie == "favicon.ico":
        damovie == ""
    connection = engine.connect()
    damovie = str(movie)
    sqlquery = "select title from release_date where title = " + damovie
    result = connection.execute(sqlquery)
    alist = []
    for row in result:
        alist.append( [row['title'], row['date']])
    return render_template('form.html', title=alist)

@app.route('/cool_form', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('moviesearch'))

    # show the form, it wasn't submitted
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
