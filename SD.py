# import sounddevice
# from scipy.io.wavfile import write
# import pyttsx3 as tts
#
# fs = 44100
# second = int(input("Enter time duration in seconds: "))
# print("Recording......n")
#
# record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
# sounddevice.wait()
#
# write("out.wav", fs, record_voice)
#
# print("Finished........nPlease check your output file")
#
# engine = tts.init()


import sounddevice as sd
from scipy.io.wavfile import write
import wav.io as wv

# sampling frequency
freq = 44100
# recording duration
duration = 5
'''Start recorder with given values of duration and sample frequency'''
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
# record audio for the given number of seconds
sd.wait()
'''This will convert the NumPy array to an audio file with the given sampling frequency'''
write("recording0.wav", freq, recording)
# Convert the NumPy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)
