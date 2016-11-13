from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)

#############
# CONFIGURATION

import os
# app.config.from_object('config.BaseConfig')
# export APP_SETTINGS="config.DevelopmentConfig"
if 'APP_SETTINGS' not in os.environ:
    os.environ['APP_SETTINGS'] = "config.DevelopmentConfig"

app.config.from_object(os.environ['APP_SETTINGS'])

#############
# DATABASES

db = SQLAlchemy(app)  # register database to

#############
# VARIABLES

app.secret_key = "\x91\xe3\xf5c\xbc|]\x1f\x93\xabX\xa7S\x0f\xc7\xf1>\xaf" \
             "}\xb05" \
             "\x06'\xb5"


#############
# WRAPPERS

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("you need to login first")
            return redirect(url_for('login'))
    return wrap

#############
# EXTENSIONS


bcrypt = Bcrypt(app)
#

#############
# HELPERS
# def connect_db():
#     return sqlite3.connect(app.database)

#############
# ENDPOINTS


@app.route('/')             # browser endpoint
@login_required             # receive function from parameter and their params
def home():                 # url_for
    try:
        pass
        #return render_template('index.html', posts=posts)
    except:
        pass

    return render_template('index.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    print "login request {}".format(request.method)
    if request.method == 'POST':
        if request.form['username'] != 'user' \
                or request.form['password'] != 'pass':
            error = 'Invalid credentials. Hint: user:pass'
        else:
            session['logged_in'] = True
            flash('you just log in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@login_required
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('you just log out')
    return redirect(url_for('welcome'))


if __name__ == '__main__':
    app.run(debug=True, port=1234)
    # debug mode automatically restart
    # service when the source is modified
