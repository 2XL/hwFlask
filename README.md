hwFlask
=======


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

5. check site
heroku open
```
