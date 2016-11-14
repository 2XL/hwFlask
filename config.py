"""
verbose app config

from app import app
print app.config


define environemnt variables for each release, so the config.py remains
unchanged and sensitive information doesn't get revealed

"""

#
import os

import jinja2

basedir = os.path.abspath(os.path.dirname(__file__))
root_templates = os.path.join(basedir,'templates')

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "\x91\xe3\xf5c\xbc|]\x1f\x93\xabX\xa7S\x0f\xc7\xf1>\xaf" \
                 "}\xb05" \
                 "\x06'\xb5"
    # export DATABASE_URL="sqlite:///posts.db"
    # export DATABASE_URL="postgresql://localhost/flask_dev"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sample.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
