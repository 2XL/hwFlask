#!/bin/bash


echo "Run the service"


source ../venv/bin/activate


#pip install pipreqs
#pipreqs .
#pip install -r requirements.txt


# setup env vars

export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="sqlite///sample.db"

python app.py

deactivate # quit virtualenv
