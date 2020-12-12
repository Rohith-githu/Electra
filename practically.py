import pyautogui, webbrowser
import time
from pyttsx3 import *

def join_practically() :
    time.sleep(3)
    webbrowser.open('https://www.practically.com')
    time.sleep(2)
    speak('Opened practically.com')
    time.sleep(8)
    login = pyautogui.locateCenterOnScreen('login_p.png')
    pyautogui.moveTo(login)
    pyautogui.click()
    time.sleep(1)

    login_pye = pyautogui.locateCenterOnScreen('login_pye.png')
    pyautogui.moveTo(login_pye)
    pyautogui.click()
    speak('Logged into your account')
    time.sleep(3)

    join_class = pyautogui.locateCenterOnScreen('join_class.png')
    pyautogui.moveTo(join_class)
    pyautogui.click()

    speak('Entered the class')


# join_practically()