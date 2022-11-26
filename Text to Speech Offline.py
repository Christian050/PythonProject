# import pyttsx3
# engine = pyttsx3.init() # engine for voice
# voices = engine.getProperty('voices') # voice
# engine.setProperty('voices',voices[0].id)
# # print(voices[0].id)
# engine.setProperty('rate', 120) # speed of voice
# engine.say('Hello Moses, I dont want a fucking slap')
# engine.runAndWait()

# or
import pyttsx3 as tts
voice = tts.init()
female_voice = voice.getProperty('voices')
voice.setProperty('rate', 150)
voice.setProperty('voice', female_voice[1].id)
# print(female_voice[1].id)


test_ = 'This is a test voice'
voice.say(test_)
voice.runAndWait()
voice.stop()
