from sqlalchemy import create_engine, Column, Integer, Numeric, String, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///:memory:')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Title(Base):
    __tablename__ = 'title'
    title_id = Column(Integer, primary_key=True)
    title = Column(String(50), index=True)
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
    title = Column(String(50), index=True)
    year = Column(String(2))
    name = Column(String(60))

    def __repr__(self):
        return "%s %s %s" % (self.title, self.year, self.name)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

#title
with open("datafiles/title.csv", "r") as f:
    num = 0
    aset = set()
    listoftitles = []
    # f_no_colname = iter(f)
    # next(f_no_colname)
    for aline in f:
        if "title," in aline:
            continue
        # if pleasestop == 3:
        #     break
        #linestr = ""
        # for ch in aline:
        #     if ch is not "\n":
        #         linestr = linestr + ch

        linestr = aline.split(',')
        #print(linestr)
        try:
            linestr[2] = int(linestr[2])
        except:
            continue
        # if linestr[2] < 2000:
        #     continue
        new_title = Title(title_id=num, title=linestr[1], year=linestr[2])
        #session.add(new_title)
        aset.add(new_title)
        num += 1
        print("title number:", num)
print("okay, now let's save those titles")
session.bulk_save_objects(aset)
session.commit()

#release_date
with open("datafiles/release_date.csv", "r") as f:
    # pleasestop = 0
    aset = set()
    num = 0
    f_no_colname = iter(f)
    next(f_no_colname)
    for aline in f_no_colname:
        # if pleasestop == 3:
        #     break
        linestr = ""
        for ch in aline:
            if ch is not "\n":
                linestr = linestr + ch
        # pleasestop += 1
        linestr = linestr.split(',')
        #print(linestr)
        try:
            linestr[1] = int(linestr[1])
            linestr[4] = int(linestr[4])
            linestr[5] = int(linestr[5])
            linestr[6] = int(linestr[6])
        except:
            continue
        new_release_date = Release_Date(
        title=linestr[0],
        year=linestr[1],
        country=linestr[2],
        date=linestr[3],
        month=linestr[4],
        day=linestr[5],
        dow=linestr[6]
        )
        #session.add(new_release_date)
        aset.add(new_release_date)
        #session.add(new_release_date)
        print("rld number:", num)
        num += 1

print("let's commit these release dates (oh please work)")
session.bulk_save_objects(aset)
session.commit()



#cast
with open("datafiles/cast.csv", "r") as f:
    # pleasestop = 0
    num = 0
    aset = set()
    f_no_colname = iter(f)
    next(f_no_colname)
    for aline in f_no_colname:
        # if pleasestop == 3:
        #     break
        linestr = ""
        for ch in aline:
            if ch is not "\n":
                linestr = linestr + ch
        # pleasestop += 1
        linestr = linestr.split(',')
        #print(linestr)
        try:
            linestr[2] = int(linestr[2])
        except:
            continue
        new_cast = Cast(
        title=linestr[1],
        year=linestr[2],
        name=linestr[3]
        )
        # session.add(new_cast)
        aset.add(new_cast)
        print("cast number:", num)
        num += 1
print("now let's save the cast!")
session.bulk_save_objects(aset)
session.commit()

# Print it all!
# titles = session.query(Title).all()
# print(titles)
# dareleasedates = session.query(Release_Date).all()
# print(dareleasedates)
# dacast = session.query(Cast).all()
# print(dacast)

# Print some of all!
# query = session.query(Title).order_by(Title.title).limit(3)
# print([result.title for result in query])
# query = session.query(Release_Date).order_by(Release_Date.year).limit(3)
# print([result for result in query])
# query = session.query(Cast).order_by(Cast.name).limit(3)
# print(result for result in query)





# for title in session.query(Title).order_by(desc(Title.year)):
#     print(title.title, title.year)



# That's all folks!
