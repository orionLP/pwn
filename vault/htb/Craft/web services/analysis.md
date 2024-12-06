From the exercise of enumeration we can glance the following information about the services:

**REST API**

- This part allows for the retrieval, update and deletion of records of crafted brews. 
- There are access control checks for some of it's functionality based on password and username, which retrieves a signed token from the application. This token is a json web token and is used in the header 'X-Craft-API-Token'.
- One part of it's brew functionality is weak to code injection, but it is behind a token check.
- The api has been created in flask.
- The api does not seem to be running in debug mode
- The api stores it's data into a mysql database
- There are tests left from the devs in some of the folders of the api. Might contain useful information.
- The login functionality is based on basic authentication
- All information (secrets, database connectivity, etc...) for configuration is stored in craft_api.settings, to which we do not have access for now.
- The queries are crafted using flask-sqlalchemy legacy query functions such as             ` User.query.filter(User.username == auth.username, User.password == auth.password).one()`
- The original server defines it's working port at 8888, but we are using 443, so maybe there is a reverse proxy here (also since it uses `from werkzeug.contrib.fixers import ProxyFix`, i can deduce there is one and uses werkzeug as middleware) -> nginx/1.15.8

**GOGS SERVER**

- The server is a gogs instance version `0.11.86.0130`
- There is an administration account (and other users)
- There are some files that have not been uploaded to the git server
- This gogs is built on go 1.11.5
- We have the credentials from gogs `'dinesh', '4aUh0A8PbVJxgd'`, maybe we can do password stuffing in the api -> the credentials work in the api
