from flask import Flask, render_template, Response
import socketio

sio = socketio.Client()

from camera import VideoCamera

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
#socketio = SocketIO(app)
sio.connect('http://192.168.43.168:5000')

@app.route('/')
def sessions():
    return render_template('session.html')


def gen(camera):
    while True:
        frame , info= camera.get_frame()

        #print (info)

       # sio.emit( 'my event', {
        #    'user_name' : 'axc',
        #    'message' : info
        #  } )

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')





if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
