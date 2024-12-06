```bash
┌──(kali㉿kali)-[~/work/repo/craft-api]
└─$ ls -la
total 28
drwxrwxr-x 4 kali kali 4096 Feb  8  2019 .
drwxrwxr-x 3 kali kali 4096 Dec  1 12:20 ..
-rw-rw-r-- 1 kali kali   18 Feb  8  2019 .gitignore
-rw-rw-r-- 1 kali kali 1585 Feb  8  2019 app.py
drwxrwxr-x 4 kali kali 4096 Feb  8  2019 craft_api
-rwxr-xr-x 1 kali kali  673 Feb  8  2019 dbtest.py
drwxrwxr-x 2 kali kali 4096 Feb  8  2019 tests
```

```bash
┌──(kali㉿kali)-[~/work/repo/craft-api]
└─$ cat .gitignore 
*.pyc
settings.py
```

There is a settings configuration file

```python
┌──(kali㉿kali)-[~/work/repo/craft-api]
└─$ cat tests/test.py 
#!/usr/bin/env python

import requests
import json

response = requests.get('https://api.craft.htb/api/auth/login',  auth=('', ''), verify=False)
json_response = json.loads(response.text)
token =  json_response['token']

headers = { 'X-Craft-API-Token': token, 'Content-Type': 'application/json'  }

# make sure token is valid
response = requests.get('https://api.craft.htb/api/auth/check', headers=headers, verify=False)
print(response.text)
```

Now we know how to send tokens to the check functionality

```python
┌──(kali㉿kali)-[~/…/repo/craft-api/craft_api/api]
└─$ cat restplus.py 
import traceback

from flask_restplus import Api
from craft_api import settings

api = Api(version='1.0', title='Craft API',
          description='An API for IPA\'s')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500
```

This seems to be the base description of the api, and by how the application handles errors, i would bet we are not in debug mode.

```python 
┌──(kali㉿kali)-[~/…/craft_api/api/auth/endpoints]
└─$ cat auth.py       


from flask import request, jsonify, make_response
from flask_restplus import Resource
from craft_api import settings
from craft_api.api.restplus import api
from functools import wraps
from craft_api.database.models import User
import datetime 
import jwt

ns = api.namespace('auth/', description='Operations related to authentication')

secret = settings.CRAFT_API_SECRET

authorizations = {
    'apikey' : { 

        'type' : 'apiKey',
        'in' : 'header',
        'name': 'X-Craft-Api-Token'
    }
}

def auth_login():

    auth = request.authorization

    try: 
        auth_results = User.query.filter(User.username == auth.username, User.password == auth.password).one()
    except: 
        auth_results = ''
    
    if type(auth_results) is User:
        
        token = jwt.encode({'user': auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, secret)
        
        return jsonify({'token' : token.decode('UTF-8')})
    
    return make_response('Authentication failed', 401, {'WWW-Authenticate' : 'Basic realm="Craft API Login"'})

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        
        if 'X-Craft-Api-Token' in request.headers:
            token = request.headers['X-Craft-Api-Token']
        
        try:
            token_decoded = jwt.decode(token, secret)
        except:
            return {'message' : 'Invalid token or no token found.'}, 403

        return f(*args, **kwargs)

    return decorated

@ns.route('/login')
class AuthCollection(Resource):
    def get(self):
        """
        Create an authentication token provided valid username and password.
        """
        token = auth_login()
        return token


@ns.route('/check')
class AuthCollection(Resource):
    @auth_required
    def get(self):
        """
        Checks validity of an authorization token
        """
        return jsonify({'message' : 'Token is valid!'})                                                                                                    
```

The api seems to be using a db to query users for this functionality, and then it inserts this as a header for later authentication. Flask implements classes in order to manage access to the database, so i suppose that this is what it is using (flask_sqlalchemy).

```python 
┌──(kali㉿kali)-[~/work/repo/craft-api]
└─$ cat dbtest.py 
#!/usr/bin/env python

import pymysql
from craft_api import settings

# test connection to mysql database

connection = pymysql.connect(host=settings.MYSQL_DATABASE_HOST,
                             user=settings.MYSQL_DATABASE_USER,
                             password=settings.MYSQL_DATABASE_PASSWORD,
                             db=settings.MYSQL_DATABASE_DB,
                             cursorclass=pymysql.cursors.DictCursor)

try: 
    with connection.cursor() as cursor:
        sql = "SELECT `id`, `brewer`, `name`, `abv` FROM `brew` LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)

finally:
    connection.close()
```


```python   
┌──(kali㉿kali)-[~/…/repo/craft-api/craft_api/database]
└─$ cat models.py 
# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime
from craft_api.database import db

class Brew(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brewer = db.Column(db.String(80))
    name = db.Column(db.Text)
    style = db.Column(db.Text)
    abv = db.Column(db.Numeric)


    def __init__(self, brewer, name, style, abv):
        self.brewer = brewer
        self.name = name
        self.style = style
        self.abv = abv

    def __repr__(self):
        return '<Brew %r>' % self.name

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password
```

```python
┌──(kali㉿kali)-[~/…/craft_api/api/brew/endpoints]
└─$ cat brew.py       


from flask import request, jsonify, make_response
from flask_restplus import Resource
from craft_api.api.restplus import api
from craft_api.api.auth.endpoints import auth
from craft_api.api.brew.operations import create_brew, update_brew, delete_brew
from craft_api.api.brew.serializers import beer_entry, page_of_beer_entries
from craft_api.api.brew.parsers import pagination_arguments
from craft_api.database.models import Brew
from functools import wraps
import datetime 

ns = api.namespace('brew/', description='Operations related to beer.')


@ns.route('/')
class BrewCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_beer_entries)
    def get(self):
        """
        Returns list of brews.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        brews_query = Brew.query
        brews_page = brews_query.paginate(page, per_page, error_out=False)

        return brews_page

    @auth.auth_required
    @api.expect(beer_entry)
    def post(self):
        """
        Creates a new brew entry.
        """

        # make sure the ABV value is sane.
        if eval('%s > 1' % request.json['abv']):
            return "ABV must be a decimal value less than 1.0", 400
        else:
            create_brew(request.json)
            return None, 201

@ns.route('/<int:id>')
@api.response(404, 'Brew not found.')
class BrewItem(Resource):

    @api.marshal_with(beer_entry)
    def get(self, id):
        """
        Returns brew data.
        """
        return Brew.query.filter(Brew.id == id).one()

    @auth.auth_required
    @api.expect(beer_entry)
    @api.response(204, 'Brew successfully updated.')
    def put(self, id):
        """
        Updates a brew.
        """
        data = request.json
        update_brew(id, data)
        return None, 204

    @auth.auth_required
    @api.response(204, 'Brew successfully deleted.')
    def delete(self, id):
        """
        Deletes a brew.
        """
        delete_brew(id)
        return None, 204    
```

**There is a very worrisome statement in the post functionality of the brew function, as  there is no sanitation for the abv value. However to access this we need a valid json web token**


