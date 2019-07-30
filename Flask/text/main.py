from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)



@app.route('/')
def sessions():
    return render_template('session.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
