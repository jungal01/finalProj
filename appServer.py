from flask import Flask, render_template, request
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import os


app = Flask(__name__)

engine = create_engine('postgresql://{}', echo=False .format(os.environ["DATABASE_URL"]))
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

@app.route('/history', method=['GET'])

@app.route('/history', method=['DELETE'])

#this path is optional and low priority
#@app.route('/history/movie')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
