from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app import db as database, bcrypt


class Post(database.Model):

    __tablename__ = "posts"

    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String, nullable=False)
    description = database.Column(database.String, nullable=False)
    author_id = database.Column(database.Integer, ForeignKey('users.id'))

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        """
        How we want it to be printed
        :return:
        """
        return '<title {}'.format(self.title)


class User(database.Model):
    __tablename__ = "users"
    id =database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False)
    password = database.Column(database.String, nullable=False)
    posts = relationship("Post", backref="author")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<name {}'.format(self.name)
