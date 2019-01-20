from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import speech_recognition as sr
import pyaudio
import random
import datetime
import webbrowser
import wikipedia
import urllib
now = datetime.datetime.now()
bot=ChatBot('innu')
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey','hai','hai','haiii','Hai','Haii','Haiii']
random_greeting = random.choice(greetings)
question = ['how are you','How are you doing?']
responses = ["I'm cool thank you"]
random_response = random.choice(responses)
cmd10= ['whats your name', 'what is your name','ur name', 'whats ur name','name', 'whos this',"whos's this"]
nameans= ['Innu', 'younus shaik', 'innu shaik', 'younus', 'innu baba']
cmd11= ['what is my date of birth', 'dob', 'whats my dob', 'whats my date of birth', 'date of birth']
dobans= ['14/01/1999']
cmd12= ['where do i study', 'wr do i study', 'where do u study']
studyans= ['you are persuing your engineering at sathyabama university']
cmd13= ['what is my fathers name', "what is my father's name", 'whats my dads name', "dad's name",]
dadans= ['your fathers name is shaik abdul rahiman', 'SHAIK ABDUL RAHIMAN']
cmd14= ['whats my mobile number', 'what is my mobile number', 'whats my phone number', 'what is my phone no.', 'my phone number','phone no.']
mobans= ['9491752538']
cmd15= ['whats my aadhar card no.', "what's my aadhar card no.", 'what is my aadhar card no.', 'whats my aadhar card number', 'what is my aadhar card number', 'aadhar card number', 'aadhar card no.', 'aadhar card', 'aadhar']
aadharans= ['310589008454']
cmd16= ['what is my pan card number', 'whats my pan card number', "what's my pan card number", 'whats my pan card no.', "what's my pan card no.", 'pan no.']
panans= ['IBPL80016Q']
cmd17= ['mom dads anniversary', 'mom and dads anniversary', "mom dad's anniversary"]
annivesaryans= ['1/5/1992']
var1 = ['who made you', 'who created you',]
var2 = ['I_was_created_by_YOUNUS SHAIK_right_in_his_computer.', 'SHAIK YOUNUS', 'Some_guy_whom_i_never_got_to_know.']
var3 = ['time', 'what time is it', 'what is the time', 'time','whats the time']
var4 = ['who are you', 'what is your name','whats your name']
cmd1 = ['open browser', 'open google','open chrome','google']
cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
cmd3 = ['tell a joke', 'tell me a joke', 'say something funny','joke','tell something funny']
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
cmd4 = ['open youtube', 'i want to watch a video','youtube']
cmd5 = ['tell me the weather', 'weather', 'what about the weather']
cmd6 = ['exit', 'close', 'goodbye', 'nothing']
cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?']
colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
cmd8 = ['what is you favourite colour', 'what is your favourite color']
cmd9 = [ 'thank you', 'tq']
repfr9 = ['your welcome', 'glad i could help you']
cmd18= ['open wikipedia', 'wikipedia']
while True:
    message=input('innu:').lower()
    if message.strip()!="bye":
        reply=bot.get_response(message)
        if reply.confidence>0.5:
            {}
            if message in greetings:
                print(random_greeting)
            elif message in question:
                print(random_response)
            elif message in var1:
                reply = random.choice(var2)
                print(reply)
            elif message in var3:
                print(now)
            elif message in var4:
                print('MY NAME IS YOUNUS SHAIK AN ARTIFICIAL INTELLIGENCE CREATED BY HIMSELF')
            elif message in cmd1:
##                webbrowser.open('www.google.com', new=0, autoraise=True)
                webbrowser.open('www.google.com')
##            elif message in cmd2:
##                mixer.init()
##                mixer.music.load(r"C:\Users\DELL\Music")
##                mixer.music.play()
            elif message in cmd3:
                print(random.choice(jokes))
            elif message in cmd4:
                webbrowser.open('www.youtube.com')
##            elif message in cmd5:
##                owm = pyowm.OWM('YOUR_API_KEY')
##                observation = owm.weather_at_place('Bangalore, IN')
##                observation_list = owm.weather_around_coords(12.972442, 77.580643)
##                w = observation.get_weather()
##                w.get_wind()
##                w.get_humidity()
##                w.get_temperature('celsius')
##                print(w)
##                print(w.get_wind())
##                print(w.get_humidity())
##                print(w.get_temperature('celsius'))
            elif message in cmd7:
                reply=random.choice(colrep)
                print(reply)
            elif message in cmd8:
                reply=random.choice(colrep)
                print(reply)
            elif message in cmd9:
                reply=random.choice(repfr9)
                print(reply)
            elif message in cmd10:
                reply=random.choice(nameans)
                print(reply)
            elif message in cmd11:
                reply=random.choice(dobans)
                print(reply)
            elif message in cmd12:
                reply=random.choice(studyans)
                print(reply)
            elif message in cmd13:
                reply=random.choice(dadans)
                print(reply)
            elif message in cmd14:
                reply=random.choice(mobans)
                print(reply)
            elif message in cmd15:
                reply=random.choice(aadharans)
                print(reply)
            elif message in cmd16:
                reply=random.choice(panans)
                print(reply)
            elif message in cmd17:
                reply=random.choice(anniversaryans)
                print(reply)
            elif message in cmd18:
                webbrowser.open('https://www.wikipedia.org/')
            else:
                print("I did not understand what you said")
    if message.strip()=='bye':
        print('nice to meet you,bye')
        exit()
        break
