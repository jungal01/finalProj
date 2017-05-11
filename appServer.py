from flask import Flask, render_template, request
import sqlalchemy
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

engine = create_engine('sqlite:///:memory', echo=True)
db = sessionmaker(bind=engine)

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

@app.route('/movie')
def specificMovie(movie):
    for x in db.query()

@app.route('/history', method=['GET'])

@app.route('/history', method=['DELETE'])

@app.route('/history/movie')
