from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
bot=ChatBot('innu')
engine=pyttsx3.init()
conv=open(r'C:\Users\DELL\Desktop\chat.txt').readlines()
bot.set_trainer(ListTrainer)
bot.train(conv)
while True:
    message=input('younus:').lower()
    if message.strip()!="bye":
        reply=bot.get_response(message)
        if reply.confidence>0.7:
            print('ChatBot:',reply)
            #print(reply.confidence)
            engine.say(reply)
            engine.setProperty('rate',110)
            engine.setProperty('volume',1)
            engine.runAndWait()
    if message.strip()=='bye':
        print('ChatBOt:nice to meet you,bye')
        engine.say('nice to meet you,bye')
        engine.setProperty('rate',110)
        engine.setProperty('volume',1)
        engine.runAndWait()
        break


