"""
verbose app config

from app import app
print app.config


define environemnt variables for each release, so the config.py remains
unchanged and sensitive information doesn't get revealed

"""


#
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    DEBUG = False


    # export DATABASE_URL="sqlite:///posts.db"
    # export DATABASE_URL="postgresql://localhost/flask_dev"



    SQLALCHEMY_DATABASE_URI = 'sqlite:///sample.db'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
