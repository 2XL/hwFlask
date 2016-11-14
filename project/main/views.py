from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from functools import wraps

#####
main_blueprint = Blueprint(
    'main', __name__,
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
            return redirect(url_for('users.login'))
    return wrap


@main_blueprint.route('/')             # browser endpoint
@login_required             # receive function from parameter and their params
def home():                 # url_for => with redirect
    try:
        pass
        #return render_template('index.html', posts=posts)
    except:
        pass

    return render_template('index.html')


@main_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')

