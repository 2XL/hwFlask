from models import *

from project.main import app

# create db and tables


# insert

app.db.session.add(User(name="Good", email="asdf", password="Good Person"))
app.db.session.add(User(name="Bad", email="qwer", password="Bad Person"))
app.db.session.add(User(name="Normal", email="zxcv", password="Normal " \
                                                                  "Person"))

# commit the changes

app.db.session.commit()
