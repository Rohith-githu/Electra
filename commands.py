import pyttsx3
import speech_recognition as sr
import os
import wikipedia
import webbrowser
import datetime

engine = pyttsx3.init('sapi5')
def spr(amount) :
    print(amount)
    engine.say(amount)
    engine.runAndWait()
def speak(audio) :
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12 :
        print('Good morning!')
        speak('Good morning sir, what can i help you with')
    elif hour >= 12 and hour < 16 :
        print('Good afternoon!')
        speak('Good afternoon sir, what can i help you with')
    elif hour >= 16 and hour < 20 :
        print('Good Evening!')
        speak('Good Evening sir, what can i help you with')
def meaning(word) :
    dictionary = PyDictionary()
    dictionary.meaning(word)
def takeCommand() :
    # take's input from microphone to execyte the command
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print('Listening...')
        audio = r.listen(source)
    try :
        print('recognizing...')
        query = r.recognize_google(audio, language = 'en-in')
        print(f'You said : {query}\n')
    except Exception as e :
        print(e)
        print('Please say that again...')
        return 'None'
    return query