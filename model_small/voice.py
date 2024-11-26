import pyttsx3
import sounddevice as sd

engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

def speaker(text):
    engine.say(text)
    engine.runAndWait()
