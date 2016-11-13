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

5. check the deployed site
heroku open

6. run tests
heroku run [python test.py -v] # run command 

7. check logs
heroku logs

```
