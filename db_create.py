from app import *
from models import *


# create db and tables

database.create_all()

# insert

database.session.add(Post(title="Good", description="Good Person"))
database.session.add(Post(title="Bad", description="Bad Person"))
database.session.add(Post(title="Normal", description="Normal Person"))

# commit the changes

database.session.commit()

"""
Query samples

#######
#sqlite
from model import Post
post = Post.query.all() # select * from posts
posts

#######
#postgresql
psql
CREATE DATABASE <DBNAME>;

\c <DBNAME> # connect to db

\d # list relations

\d <TABLE_NAME> # show table information

INSERT INTO <TABLE_NAME> VALUES (1, 'admin', 'email@obytes.com', 'admin')

UPDATE <TABLE_NAME> SET <TABLE_FIELD> = <VALUE>


"""

