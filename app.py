from flask import Flask
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from functools import wraps

import sqlite3

app = Flask(__name__)

#############
# DATABASES

app.database = "sample.db"



#############
# VARIABLES

app.secret_key = "secret"  # used for user session


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
# FUNCTIONS


def connect_db():
    return sqlite3.connect(app.database)

#############
# ENDPOINTS


@app.route('/')             # browser endpoint
@login_required             # reciben por parametro funciones y sus parametros
def home():                 # url_for
    try:
        g.db = connect_db()
        cur = g.db.execute('select * from posts')
        posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
        g.db.close()
    except sqlite3.OperationalError:
        flash('u have no db')
    return render_template('index.html', posts=posts)


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
