drop table if exists movie cascade;
create table movie(
  id serial unique,
  title varchar(100),
  year int(4),
  primary key(id, title)
);

drop table if exists moviecast cascade;
create table moviecast(
  id serial unique,
  title varchar(100) references movie(title),
  year int(4),# we should take this out since we already have this in movie
  name varchar(100),
  type varchar(20),
  character varchar(50),
  n int,
  primary key(id, name)
);

drop table if exists course_requirement;
create table course_requirement(
  course int references course(id),
  requirement int references requirement(id),
  primary key(course, requirement)
);
