from flask import Flask, render_template
from flask_socketio import SocketIO,emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'donottellanyoneaboutthis'

#socketio wrapper for the app
socketio = SocketIO(app,async_mode = 'eventlet')

@app.route('/')
def home():
    return render_template('home.html')

#event for broadcasting message to everyone...
@socketio.on('my event')
def handel_message(json):
    print(json)
    socketio.emit('my response',json)

if __name__ == '__main__':
    socketio.run(app,debug = True)