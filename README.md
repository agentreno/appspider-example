# appspider-example

## Description

An example of how to trigger AppSpider DAST scanning with an example API target
hosted in Heroku.

Heroku allow penetration tests without prior authorization:
https://devcenter.heroku.com/articles/pentest-instructions

## Instructions

Contact Karl Hopkinson-Turrell (karl.hopkinsonturrell@pearson.com) to access
the example app running at https://appspider-example.herokuapp.com or deploy
this app to your own Heroku account.

Alternatively you can run the app locally with:

```
docker build -t exampleapi .
docker run -it -p 8000:8000 exampleapi
curl -d '{"name": "testcourse", "category": "test", "max_participants": 10}' -H "Content-Type: application/json" -X POST localhost:8000/api/courses/
curl localhost:8000/api/courses/
```

The API can require authentication if you set the `ENABLE_AUTHENTICATION` env
var. If this is done, a user must make a POST to `/token` with JSON params
`username` and `password` to receive a token, which must be placed in a header
like `Authorization: Token <token>` for all API requests. Create a user by
running Django's management command in the instance e.g. locally `docker exec
-it <container> python manage.py createsuperuser --username=testuser
--email=testemail`.
