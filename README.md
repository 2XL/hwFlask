hwFlask
=======

VirtualEnvWrapper
```
step 0  always setup local virtual env for each project
pip install virtualenvwrapper 
# then update ur .profile | .bashrc with
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
# reload profile
source .profile

step 1 create virtualenv
mkvirtualenv $(basename `pwd`)
pip install -r requirements.txt

```




User passwords
```
Rule: Never store plain text user pass

1. add <hashlib> instance to app.py
2. update user model to hash the pass
3. apply the model changes to our database with a db migratin
4. delete all data in the user table within the psql shell
5. add new users to the table 
6. manually test to ensure pass are hashed

```





Deploy on heroku
```
1. create git repo at heroku
heroku create {{cookiecutter.reponame}}

2. push local source to heroku repo
git push heroku master

3. enable worker for the repo service
heroku ps:scale web=1

4 list running services
heroku ps

5. check the deployed site
heroku open

6. run tests
heroku run [python test.py -v] # run command 

7. check logs
heroku logs


8. set environ vars to heroku env
git remote -v # retrieve the remote host user, default: heroku 
heroku config:set <VARNAME>=<config.ClassConfig> --remote heroku

9. plugins to heroku
# postgresql
heroku addons:add heroku -postgresql:dev
heroku pg:promote <HEROKU_POSTGRESQL_YELLOW_URL>
heroku run python app.py

10. migrate local db to remote

# list heroku instance database 
heroku config | grep HEROKU_POSTGRESQL
heroku run python db_create.py


11. get interactive shell from heroku
heroku run python
```



Migrate Flask Database
```
pip install flask_migrate

1. setup manage.py file
python manage.py db migrate
## generates the sql scripts ready to be executed for:
# upgrade
python manage.py db upgrade
# downgrade
python manage.py db downgrade

```


Project Structure
```
The main app contains functionality that is not associated with the blueprints
```
