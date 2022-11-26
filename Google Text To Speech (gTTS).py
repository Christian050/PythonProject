# from gtts import gTTS
# import os
# mytext= "Welcome to Python one on one"
# language = 'en'
# myobj = gTTS(text=mytext,lang=language,slow=False)
# myobj.save("firstts.mp3")
# os.system("firstts.mp3")


from gtts import gTTS
import os
file = open('Hope.txt', "r").read().replace("\n", "")
Speech = gTTS(text=str(file), lang='en', slow=False)
Speech.save("Hope.mp3")
os.system("Hope.mp3")
