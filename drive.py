from flask_socketio import SocketIO
import eventlet
from flask import Flask

sio = SocketIO.server()
app = Flask(__name__)



@sio.on('connect')
def connect(sid, environ):
    print('Connected')
    send_control(0, 1)

def send_control(steering_angle, throttle):
    sio.emit('steer', data = {
        'steering_angle': steering_angle.__str__(),
        'throttle': throttle.__str__()
    })


if __name__ == '__main__':
    # model = load_model('model.h5')
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
    eventlet.sleep(1)


# @sio.on('connect')
# def connect(sid, environ):
#     print('Connected!!')
#     send_controls(0, 1)
#
#
# def send_controls(steering_angle, throttle):
#     print(steering_angle, throttle)
#     sio.emit('steer', data={'steering_angle':steering_angle.__str__(), 'throttle': throttle.__str__()})
# if __name__=='__main__':
#     app=socketio.Middleware(sio, app)
#     eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
