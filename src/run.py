from app import app
from flask.ext.socketio import SocketIO, emit

app.config.from_object('config')

if __name__ == "__main__":
 app.run(app.config["IP"],debug=app.config["DEBUG"])