import pyttsx3

data = input("enter text you want to convert into speech")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()