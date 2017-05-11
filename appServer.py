#!flask/bin/python
from flask import Flask, render_template, request
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from app import db_create

app = Flask(__name__)
#engine = create_engine('postgresql://{}', echo=False .format(os.environ["DATABASE_URL"]))
# engine = create_engine('sqlite:///:memory:')
engine = db_create.engine
#db = sessionmaker(bind=engine)

# Session = sessionmaker(bind=engine)
Session = db_create.Session
#db = Session() #called "session" in db_create.py
db = db_create.session
@app.route('/')
def allMovies():
    movies = set()
    movieIds = set()
    for x in db.query(title):
        movies.add((x.title, x.year))
        movieIds.add(x.index)

    return render_template('index.html',
                            movies= list(movies),
                            columns=[x for x in movieIds])
#For testing purposes
@app.route('/test')
def moviesubmit():
    actorSet = set()
    count = 1

    #movieQ = db.query(Release_Date, Cast).join('Title').filter_by(asc(title=movie)).limit(5)
    query = db.query(db_create.Title).order_by(db_create.Title.year).limit(3)
    print([result.title for result in query])
    daActorList = [result.title for result in query]
    #actorSet.add(query.date)
    # count += 1
    # for x in movieQ:
    #     actorSet.add(x.name)
    #     count+=1

    return render_template('moviepage.html',
                            daActorList = daActorList,
                            columns = [x for x in range(count)])

@app.route('/test', methods=['POST'])
def my_form_post():

    text = request.form['text']
    body = {'t': text}
    response = requests.post("http://www.omdbapi.com/?",data=body)
    # processed_text = text.upper()
    return response


@app.route('/movie/<string:movie>')
def specificMovie(movie):
    actorSet = set()
    count = 1

    movieQ = db.query(release_date, cast).join('title').filter_by(title=movie).all()
    actorSet.add(movieQ.date)
    count += 1
    for x in movieQ:
        actorSet.add(x.name)
        count+=1

    return render_template('movie.html',
                            actorList = list(actorSet),
                            columns = [x for x in range(count)])

# @app.route('/history', method=['GET'])
# def someFunction():
#     pass
# @app.route('/history', method=['DELETE'])
# def someOtherFunction():
#     pass

#this path is optional and low priority
#@app.route('/history/movie')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
