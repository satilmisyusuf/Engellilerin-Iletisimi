from gtts import gTTS
import os
tts = gTTS(text='Merhaba benim adım münir karslı bu benim ilk konuşmam', lang='tr')
#tts.save("good.mp3")
os.system("mpg321 good.mp3")
