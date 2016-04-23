# Chapman Robotics Website

##Feature
###Current

###Planned

##Installing

###Required Libraries

system libraries

```
Redis
Python
```

npm libraries

```
npm install -g gulp-cli
```

pip libraries

```
pip install flask
pip install flask-sqlalchemy
pip install Flask-KVSession
pip install Redis
pip install requests
pip install psutil <-- unused
pip install alembic
```

###Install

####Configuration

under `src/server/app/config.py.sample` is the sample configuration file for the server

```
cp config.py.sample config.py
```

```
import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

IP = "192.168.0.14"

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True

RECAPTCHA_PRIVATE_TOKEN = "qnbauwbefliuabwel"
RECAPTCHA_PUBLIC_TOKEN = "qnbauwbefliuabwel"

PASSWORD_HASH="auwnpanwe8fawefh05sfgs"

SECRET_KEY = "aps8fp9a8wnef8ansdfa"
PERMANENT_SESSION_LIFETIME = datetime.timedelta(hours = 1)

GOOGLE_ANALYTICS_CODE = ""
```

`SQLALCHEMY_DATABASE_URI` this is the configuration url for sqlAlchemy to connect to a database. The current configuration creates a local sqlite database.

NOTE: for `sqlite:\\`  migrating backwards with the current configuration might become problematic due to the way sqlite works. i.e removing columns isn't possible. scale is a limitation of sqlite.

more information can be found here: http://docs.sqlalchemy.org/en/latest/core/engines.html

`PASSWORD_HASH` and `SECRET_KEY` are used to prevent a brute force attack

`PERMANENT_SESSION_LIFETIME` determins how long a session lasts

`RECAPTCHA_PRIVATE_TOKEN` and `RECAPTCHA_PUBLIC_TOKEN` register a recaptcha from [here](http://www.google.com/recaptcha/intro/index.html) and provide both a public and private token

`GOOGLE_ANALYTICS_CODE` register a google analytic id from [here](http://www.google.com/analytics/)

`THREADS_PER_PAGE` determins how many threads are used

####Inital Install

```
npm install
gulp build
```
gulp build is used to copy over and build the necessary static content for the website

####Site Configuration

It's recommend to configure the site using [gunicorn](http://gunicorn.org/) using ngnix as a proxy.

more information about deployment can be found here: http://docs.gunicorn.org/en/latest/deploy.html

##Modifying

```
gulp run
gulp run-shell
```

gulp run will start website and output the information.

gulp-shell will start the website but allow for shell commands to be input into the server.


```
gulp watch
```

gulp watch will watch for changes in the associated resource folder and
update the changes to the website. This should make it easy to modify the site and refresh the associated pages to see
the updated changes.

Note: you may have to disable browser caching. 

For chrome and firefox, F12 is used to open the developer console. under Network in chrome there should be a checkbox to disable
the cache.


#Licence
MIT
