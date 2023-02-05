import speech_recognition as sr
import pyaudio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Mời bạn nói: ")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio,language="vi-VI")
    print(text)
except:
    print("không nghe")