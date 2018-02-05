from flask import Flask, render_template,redirect
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
 # route everything back to the index.html
 # Angular 2 will then resolve the 404 error not in the route
 return render_template('index.html'), 404

@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)


# this is s sample of what a module will look like
# from app.views.solutionSubmitService import mod as solutionSubmitModule
# app.register_blueprint(solutionSubmitModule)

# from .services.robot import main as robot_service
from app.services.questionService import mod as questionService
app.register_blueprint(questionService)
