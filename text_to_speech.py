import pyttsx3
engine=pyttsx3.init()
x=input("type here :")
engine.say(x)
engine.setProperty('rate',110)
engine.setProperty('volume',1)
engine.runAndWait()
