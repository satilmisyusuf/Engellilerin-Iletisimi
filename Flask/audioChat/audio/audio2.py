import os
import uuid
import wave
from flask import Blueprint, current_app, session, url_for, render_template
from flask_socketio import emit
from socketio_examples import socketio
import speech_recognition as sr
import socketio as sioo
import json
from gtts import gTTS
import os
from pygame import mixer


sio = sioo.Client()

sio.connect('http://192.168.1.110:5000')

result=""
bp = Blueprint('audio', name, static_folder='static',
               template_folder='templates')

@bp.route('/')
def index():
    """Return the client application."""
    return render_template('audio/main.html')


@socketio.on('start-recording', namespace='/audio')
def start_recording(options):

    #print("START RECORDING")

    """Start recording audio from the client."""
    id = uuid.uuid4().hex  # server-side filename
    session['wavename'] = id + '.wav'
    wf = wave.open(current_app.config['FILEDIR'] + session['wavename'], 'wb')
    wf.setnchannels(options.get('numChannels', 1))
    wf.setsampwidth(options.get('bps', 16) // 8)
    wf.setframerate(options.get('fps', 44100))
    session['wavefile'] = wf


@socketio.on('write-audio', namespace='/audio')
def write_audio(data):
    """Write a chunk of audio from the client."""
    #print("WRITE AUDIO")

    session['wavefile'].writeframes(data)


@socketio.on('end-recording', namespace='/audio')
def end_recording():
    """Stop recording audio from the client."""

    #print("END RECORDING")

    emit('add-wavefile', url_for('static',
                                 filename='_files/' + session['wavename']))
    session['wavefile'].close()




    soundFile='/media/psf/Home/Documents/GitKraken/Bitirme/Flask/audioChat/static/_files/' + session['wavename']
    r= sr.Recognizer()
    harvard = sr.AudioFile(soundFile)
    with harvard as source:
        audio = r.record(source)

    result=r.recognize_google(audio,show_all=False,language="tr-TR")
    #print("RESULT::::::::",result)
    sio.emit('my event',{
    'user_name':'audio',
    'message':result
    })

    del session['wavefile']
    del session['wavename']


@sio.on("my response")
def on_message(data):
    print ("Message: ",data)
    #data_dict = ast.literal_eval(data)
    y = json.dumps(data)
    y = json.loads(y)
    print(y)
    #print("last message: ",y["message"])
    if y["user_name"] != "audio":
        speech=y["message"]
        tts = gTTS(text=speech, lang='tr')
        tts.save("/media/psf/Home/Documents/GitKraken/Bitirme/Flask/audioChat/audio/good.mp3")
        #os.system("/home/munir/Desktop/Bitirme-master/Flask/audioChat/audio/good.mp3")
        mixer.init()
        mixer.music.load('/media/psf/Home/Documents/GitKraken/Bitirme/Flask/audioChat/audio/good.mp3')
        mixer.music.play()
