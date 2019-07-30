import time
import socketio

sio = socketio.Client()



@sio.on('my response')
def on_message(data):
    print('message received with ', data)

if __name__ == '__main__':

  sio.connect('http://192.168.1.109:5000')

  sio.emit( 'my event', {
            'user_name' : 'axc',
            'message' : 'rwerwrwerwe'
          } )
  sio.wait()