import os
import sys
import redis

from flask import Flask, render_template,redirect
from flask.ext.sqlalchemy import SQLAlchemy

from flask_kvsession import KVSessionExtension
from simplekv.memory.redisstore import RedisStore

from flask.ext.socketio import SocketIO, emit

store = RedisStore(redis.StrictRedis())

app = Flask(__name__)
KVSessionExtension(store, app)

app.config.from_object('config')

db = SQLAlchemy(app)
socketio = SocketIO(app)


@app.errorhandler(404)
def not_found(error):
 # route everything back to the index.html
 # Angular 2 will then resolve the 404 error not in the route
 return render_template('index.html'), 404

@app.context_processor
def inject_recaptcha():
 return dict(public_token = app.config["RECAPTCHA_PUBLIC_TOKEN"])

@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

@app.context_processor
def inject_user():
 return dict(googleTrackingCode=app.config["GOOGLE_ANALYTICS_CODE"])


# this is s sample of what a module will look like
# from app.views.solutionSubmitService import mod as solutionSubmitModule
# app.register_blueprint(solutionSubmitModule)
