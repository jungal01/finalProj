"""
see:  http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#relationships-many-to-many
      http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#building-a-many-to-many-relationship
"""

from json import load
from sqlalchemy import Table, Column, Integer, String, ForeignKey, create_engine, desc, asc
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Title(Base):
    __tablename__ = 'title'
    title_id = Column(Integer, primary_key=True)
    title = Column(String(80), index=True)
    year = Column(Integer, primary_key=True)

    def __repr__(self):
        return "%s %s %s" % (self.title_id, self.title, self.year)

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

# course_requirement = Table('course_requirement',
#                            Base.metadata,
#                            Column('course', Integer, ForeignKey('course.id')),
#                            Column('requirement', Integer, ForeignKey('requirement.id')))
#
# class Course(Base):
#     """
#     SQLAlchemy Model object to represent a course
#     """
#     __tablename__ = 'course'
#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     number = Column(String)
#     dept = Column(String)
#     description = Column(String)
#     fulfills = relationship("Requirement",
#                             secondary=course_requirement,
#                             back_populates="satisfied_by")
#
#     def __repr__(self):
#         return "Course({}, {})".format(self.number, self.title)
#
#
# class Requirement(Base):
#     """
#     SQLAlchemy Model object to represent an all college requirement
#     """
#     __tablename__ = 'requirement'
#     id = Column(Integer, primary_key=True)
#     description = Column(String)
#     satisfied_by = relationship("Course", secondary=course_requirement, back_populates="fulfills")
#
#     def __repr__(self):
#         return "Requirement({})".format(self.description)


# engine = create_engine('postgres://swplgjqcmrfmmy:50c0e2902aca895e575bb703e08ad518c8a08b3bb17254be94b064aa9bd134db@ec2-54-235-120-39.compute-1.amazonaws.com:5432/d9moo2fhh5flfn')
engine = create_engine('postgres://wvawagxkuzyopc:3a8afe1fdb7c5fdc5bdf6d5f232e3d2a5a9829fc1e382bbb373abbb77678b3ed@ec2-54-83-205-71.compute-1.amazonaws.com:5432/d3er1l7rrjf0g5')
Session = sessionmaker(bind=engine)

db = Session()
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# with open('geneds.json', 'r') as gf:
#     class_info = load(gf)
#
# rset = set()
# ged = {}
# for c in class_info:  # first pass collect all distinct gened designators
#     for g in c['fulfills']:
#         rset.add(g)
#
# for g in rset:
#     res = Requirement(description=g)
#     db.add(res)
#     ged[g] = res
#
# for c in class_info:
#     newc = Course(title=c['title'], dept=c['subject'], number=c['number'],
#                   fulfills=[ged[g] for g in c['fulfills']])
#     db.add(newc)
#
# db.commit()
with open('title.json','r') as titles:
    all_titles = load(titles)
    for t in all_titles:
        newtitle = Title(title=t['title'], year=t['year'])
        db.add(newtitle)

with open('release_date.json') as release_dates:
    all_release_dates = load(release_dates)
    for r in all_release_dates:
        newrd = Release_Date(title=r['title'],year=r['year'], country=r['country'],date=r['date'],month=r['month'],day=r['day'],dow=r['dow'])
        db.add(newrd)

with open('cast.json') as casts: #I know "casts" isn't a word
    all_cast = load(casts)
    for c in all_cast:
        newcast = Cast(name=c['name'], year=c['year'],title=c['title'])
        db.add(newcast)

db.commit()
#print(all_titles)


# Now lets try a query

# quants = db.query(Requirement).filter_by(description='Quantitative').first()
#
# print([x.number for x in quants.satisfied_by])
#
# x = db.query(Course).filter(Course.fulfills.any(description='Quantitative')).all()
# print([y for y in x])
#
# # filter_by is simpler than filter and uses key value pairs for queries
# #y = db.query(Course).filter_by(number='CS 150').first()
#
# y = db.query(Course).filter(Course.number == 'CS 150').first()
#
# print(y, y.fulfills)
