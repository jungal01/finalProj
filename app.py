#!/usr/bin/python
# coding: utf-8
from flask import Flask, render_template, request
from sqlalchemy import create_engine, Column, Integer, Numeric, String, desc, asc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from json import load


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://swplgjqcmrfmmy:50c0e2902aca895e575bb703e08ad518c8a08b3bb17254be94b064aa9bd134db@ec2-54-235-120-39.compute-1.amazonaws.com:5432/d9moo2fhh5flfn'
# db = SQLAlchemy(app)
engine = create_engine('postgres://swplgjqcmrfmmy:50c0e2902aca895e575bb703e08ad518c8a08b3bb17254be94b064aa9bd134db@ec2-54-235-120-39.compute-1.amazonaws.com:5432/d9moo2fhh5flfn')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Title(Base):
    __tablename__ = 'title'
    title_id = Column(Integer, primary_key=True)
    title = Column(String(80), index=True)
    year = Column(Integer, primary_key=True)

    def __repr__(self):
        return "%s %s" % (self.title, self.year)

class Release_Date(Base):
    __tablename__ = 'release_date'
    entry_id = Column(Integer, primary_key=True)
    title = Column(String(50), index=True)
    year = Column(Integer)
    country = Column(String(50))
    date = Column(String(15))
    month = Column(Integer)
    day = Column(Integer)
    dow = Column(Integer)

    def __repr__(self):
        return "%s, %s" % (self.title, self.date)

class Cast(Base): #replace file then you're done
    __tablename__ = 'cast'
    cast_id = Column(Integer, primary_key=True)
    title = Column(String(80), index=True)
    year = Column(Integer)
    name = Column(String(80))

    def __repr__(self):
        return " %s %s %s" % (self.title, self.year, self.name)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with open('title.json','r') as titles:
    all_titles = load(titles)
    for t in all_titles:
        newtitle = Title(title=t['title'], year=t['year'])
        session.add(newtitle)

with open('release_date.json') as release_dates:
    all_release_dates = load(release_dates)
    for r in all_release_dates:
        newrd = Release_Date(title=r['title'],year=r['year'], country=r['country'],date=r['date'],month=r['month'],day=r['day'],dow=r['dow'])
        session.add(newrd)

with open('cast.json') as casts: #I know "casts" isn't a word
    all_cast = load(casts)
    for c in all_cast:
        newcast = Cast(name=c['name'], year=c['year'],title=c['title'])
        session.add(newcast)
print("let's commit")
session.commit()

@app.route('/')
def hello_world():
    # engine = create_engine('postgres://swplgjqcmrfmmy:50c0e2902aca895e575bb703e08ad518c8a08b3bb17254be94b064aa9bd134db@ec2-54-235-120-39.compute-1.amazonaws.com:5432/d9moo2fhh5flfn')
    # # engine = create_engine('postgres://swplgjqcmrfmmy:50c0e2902aca895e575bb703e08ad518c8a08b3bb17254be94b064aa9bd134db@ec2-54-235-120-39.compute-1.amazonaws.com:5432/d9moo2fhh5flfn')
    # Session = sessionmaker(bind=engine)
    #
    # db = Session()
    # query = db.query(Title).filter_by(title='Inception').first()
    # alist = [result for result in query]
    # astring = ""
    # for item in alist:
    #     astring.append(str(item))
    # return astring
    titles = session.query(Title).order_by(asc(Title.title)).limit(10)
    alist = []
    for item in titles:
        alist.append(str(item))
    return render_template('index.html', titleList=alist, title='Movies Search')



if __name__ == '__main__':
    app.run()
