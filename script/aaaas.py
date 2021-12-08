#! /usr/bin/env python3

import speech_recognition as sr
import pyaudio


print("say something2")
r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
    print ("say something3")
    audio = r.listen(source)
    word = r.recognize_google(audio,language='th')
    print(word)
