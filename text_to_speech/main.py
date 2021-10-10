import pyttsx3

data = input("enter text you want to convert into speech:\n")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()

#pyttsx3 is not work properly in virtual env