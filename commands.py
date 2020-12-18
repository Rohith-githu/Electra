from lib import *
def say(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', int(175))
    engine.say(text)
    engine.runAndWait()

def sp(audio):
    print(audio)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', int(175))
    engine.say(audio)
    engine.runAndWait()
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
    import pyautogui
    refresh = pyautogui.locateCenterOnScreen('pagerefresh.png')
    pyautogui.moveTo(refresh)
    pyautogui.click()

def switch_tab():
    pyautogui.hotkey('ctrl', 'tab')

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
def write(para) :
    pyautogui.write(para)
def shutdown():
    sp('do you really want to shut this off?')
    takeCommand()
    confirmation = takeCommand().lower()
    if 'yes' in confirmation :
        sp('leets meet next time')
        os.system('shutdown /s /t 1')
    elif 'no' in confirmation :
        sp('terminating the process')
    else :
        sp('can you plese say that again')
def restart():
    sp('do you really want to restart?')
    takeCommand()
    confirmation = takeCommand().lower()
    if 'yes' in confirmation :
        sp('leet\'s meet next time')
        os.system('shutdown /r /t 1')
    elif 'no' in confirmation :
        sp('terminating the process')
    else :
        sp('can you plese say that again')
def rester() :
    def job() :
        sp('locking the pc rest your eyes for sometime')
        pyautogui.hotkey("win", "l")
    schedule.every(10).minutes.do(job)
    while True :
        schedule.run_pending()
        time.sleep(1)