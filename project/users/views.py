from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from functools import wraps

#####
users_blueprint  = Blueprint(
    'users', __name__,
    template_folder='templates'
)

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


##############
# ROUTES


@users_blueprint.route('/login', methods=['GET', 'POST'])
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
            return redirect(url_for('main.home'))
    return render_template('login.html', error=error)


@login_required
@users_blueprint.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('you just log out')
    return redirect(url_for('main.welcome'))



