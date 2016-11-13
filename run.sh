#!/bin/bash


echo "Run the service"


source venv/bin/activate


#pip install pipreqs
#pipreqs .
#pip install -r requirements.txt

python app.py

deactivate # quit virtualenv
