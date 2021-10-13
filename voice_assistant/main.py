import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia


engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[12].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    speak("wellcome back!")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    print(Time)
    Time = ("the current time is" + Time)
    speak(Time)
def wiki():
    query = "blackhole"
    result = wikipedia.summary(query, sentences=2)
    speak("accroding to wikipedia")
    speak(result)


time()
wiki()

