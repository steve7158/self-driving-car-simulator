import socketio
import eventlet
from flask import Flask
app=Flask(__name__)

sio=socketio.Server()

@sio.on('connect')
def connect(sid, environ):
    print('connected')

if __name__=='__main__':
    # return app.run(debug=True)
    app=socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
