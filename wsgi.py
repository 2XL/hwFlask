"""
This file tell Gunicorn server how to interact with the application

gunicorn [OPTIONS] APP_MODULE
APP_MODULE = $MODULE_NAME:$VARIABLE_NAME

gunicorn -b 0.0.0.0:<port> app
"""

from app import app as application

if __name__ == "__main__":
    application.run()
