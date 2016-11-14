import jinja2
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from config import config_by_name, root_templates

from .views import main_blueprint
from project.users.views import users_blueprint


app = Flask(__name__)

#############
# CONFIGURATION

import os
# app.config.from_object('config.BaseConfig')
# export APP_SETTINGS="config.DevelopmentConfig"
if 'APP_SETTINGS' not in os.environ:
    os.environ['APP_SETTINGS'] = "dev"

app.config.from_object(config_by_name[os.environ['APP_SETTINGS']])

#############
# DATABASES

db = SQLAlchemy(app)  # register database to

#############
# TEMPLATES - LOADERS

print root_templates
app.jinja_loader = jinja2.ChoiceLoader([
    # app.jinja_loader,
    jinja2.FileSystemLoader(root_templates)
])

#############
# BLUEPRINTS - ENDPOINTS

app.register_blueprint(main_blueprint)
app.register_blueprint(users_blueprint)

#############
# EXTENSIONS

bcrypt = Bcrypt(app)



#############
# HELPERS
# def connect_db():
#     return sqlite3.connect(app.database)

if __name__ == '__main__':
    app.run(debug=True, port=1234)
    # debug mode automatically restart
    # service when the source is modified
