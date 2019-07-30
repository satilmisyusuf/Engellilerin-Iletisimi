import speech_recognition as sr
r= sr.Recognizer()
harvard = sr.AudioFile('/home/munir/Desktop/datasetsound/uc/5.wav')
with harvard as source:
    audio = r.record(source)

print(r.recognize_google(audio,show_all=False,language="tr-TR"))
