import pyautogui
from pyttsx3 import *
import speech_recognition as sr
import os
import wikipedia
import webbrowser
import datetime

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
    else :
        sp('Ohh it\'s not a time to work with PC')
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

def refresh_web_page():
    import pyautogui
    refresh = pyautogui.locateCenterOnScreen('pagerefresh.png')
    pyautogui.moveTo(refresh)
    pyautogui.click()

def whatsapp_joiner() :
    os.startfile("C:\\Users\\rohit\\Desktop\\WhatsApp Desktop.lnk")
    profile = pyautogui.locateCenterOnScreen('profile.png')
    meet_link = pyautogui.locateCenterOnScreen()
    zoom_link = pyautogui.locateCenterOnScreen()
    if meet_link is True :
        pyautogui.moveTo(meet_link)
        pyautogui.click()
    elif zoom_link is True :
        pyautogui.moveTo(zoom_link)
        pyautogui.click()
    else : 
        speak('somethimg went wrong')

