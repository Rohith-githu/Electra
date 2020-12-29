from lib import *
import pyttsx3

def say(text):
	import win32com.client as mouth
	voice = mouth.Dispatch("SAPI.SpVoice")
	voice.Speak(text)

def sp(audio):
    print(audio)
    say(audio)
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12 :
        print('Good morning!')
        say('Good morning sir, what can i help you with')
    elif hour >= 12 and hour < 16 :
        print('Good afternoon!')
        say('Good afternoon sir, what can i help you with')
    elif hour >= 16 and hour < 20 :
        print('Good Evening!')
        say('Good Evening sir, what can i help you with')
    else :
        sp('Ohh it\'s not a time to work with PC')
def takeCommand() :
    # take's input from microphone to execyte the command
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print('Listening...')
        audio = r.listen(source)
        r.pause_threshold = 1
    try :
        print('recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'You said : {query}\n')
    except Exception as e :
        print(e)
        print('Please say that again...')
        return 'None'
    return query

def refresh_web_page():
    pyautogui.hotkey('ctrl','r')

def switch_tab():
    pyautogui.hotkey('ctrl', 'tab')

def full():
    pyautogui.hotkey('f11')

def switch_windows():
    pyautogui.hotkey('alt', 'tab')

def notifications():
    pyautogui.hotkey('win','a')

def close_window():
    pyautogui.hotkey('alt', 'f4')
def unmute():
    pyautogui.hotkey('alt', 'a')
    pyautogui.hotkey('ctrl', 'd')
def menu():
    pyautogui.hotkey('win')
def menusearch():
    pyautogui.hotkey('win','s')
def recents():
    pyautogui.hotkey('win', 'tab')
def minimize():
    pyautogui.hotkey('win', 'm')
def click_on_screen():
    pyautogui.doubleClick()
def new_tab() :
    pyautogui.hotkey('ctrl', 't')
def write(para) :
    pyautogui.write(para)
def shutdown():
    sp('do you really want to shut this off?')
    confirmation = takeCommand().lower()
    if 'yes' in confirmation :
        sp('let\'s meet next time')
        for num in range(5):
            pyautogui.hotkey('alt', 'f4')
        os.system('shutdown /s /t 1')
    elif 'no' in confirmation :
        sp('terminating the process')
def restart():
    sp('do you really want to restart?')
    confirmation = takeCommand().lower()
    if 'yes' in confirmation :
        sp('let\'s meet in few moments')
        for num in range(5):
            pyautogui.hotkey('alt', 'f4')
        os.system('shutdown /r /t 1')
    elif 'no' in confirmation :
        sp('terminating the process')
def lock() :
    ctypes.windll.user32.LockWorkStation()
def sleep() :
    sp('do you want to sleep pc')
    confirmation_sleep = takeCommand().lower()
    if 'yes' in confirmation_sleep :
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    else :
        sp('terminating the process')
def  incignito():
    webbrowser.open(random.choice(['chrome.exe', 'msedge.exe']))
    pyautogui.hotkey('ctrl', 'shift','n')
def close_tab():
    pyautogui.hotkey('ctrl', 'f4')
