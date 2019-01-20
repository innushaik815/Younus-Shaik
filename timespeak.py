import datetime
import pyttsx3
engine=pyttsx3.init()
now=datetime.datetime.now()
print(now)
print('curent hour is:%d'%now.hour)
engine.say('your curent time hour is:',+now.hour)
engine.setProperty('rate',110)
engine.setProperty('volume',1)
engine.runAndWait()
print('current min is:%d'%now.minute)
engine.say('minutes:',+now.minute)
engine.setProperty('rate',110)
engine.setProperty('volume',1)
engine.runAndWait()
print('current day is:%d'%now.day)
engine.say('and today is',+now.day)
engine.setProperty('rate',110)
engine.setProperty('volume',1)
engine.runAndWait()


