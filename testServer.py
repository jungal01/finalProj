#!flask/bin/python
from flask import Flask, render_template, request
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
