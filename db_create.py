from app import db
from models import Post


# create db and tables

db.create_all()

# insert

db.session.add(Post(title="Good", description="Good Person"))
db.session.add(Post(title="Bad", description="Bad Person"))
db.session.add(Post(title="Normal", description="Normal Person"))

# commit the changes

db.session.commit()

"""
Query samples

from model import Post
post = Post.query.all() # select * from posts

posts

"""
