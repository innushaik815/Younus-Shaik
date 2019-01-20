from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import speech_recognition as sr
import pyaudio
bot=ChatBot('innu')
engine=pyttsx3.init()
r=sr.Recognizer()
conv=open(r'Y:\ml pro\chat.txt').readlines()
bot.set_trainer(ListTrainer)
bot.train(conv)
while True:
    with sr.Microphone() as source:
        print('speak i am listening!!!')
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        input=r.recognize_google(audio)
        print('you asked is :'+r.recognize_google(audio))
        if input.strip()!="bye":
            reply=bot.get_response(input)
            if reply.confidence>0.7:
                print('INNU:',reply)
                #print(reply.confidence)
                engine.say(reply)
                engine.setProperty('rate',107)
                engine.setProperty('volume',1)
                engine.runAndWait()
    if input.strip()=='bye':
        print('ChatBot:nice to meet you,bye')
        engine.say('nice to meet you,bye')
        engine.setProperty('rate',107)
        engine.setProperty('volume',1)
        engine.runAndWait()
        break


