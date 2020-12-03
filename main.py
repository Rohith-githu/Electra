import pyautogui, time
import webbrowser
from pyttsx3 import *
def join_class() :
    webbrowser.open("https://www.practically.com")
    time.sleep(8)
    var1 = pyautogui.locateCenterOnScreen('var1.png')
    pyautogui.moveTo(var1)
    pyautogui.click()
    time.sleep(1)
    var2 = pyautogui.locateCenterOnScreen('var2.png')
    pyautogui.moveTo(var2)
    pyautogui.click()
    time.sleep(2)
    var3 = pyautogui.locateCenterOnScreen('var3.png')
    pyautogui.moveTo(var3)
    pyautogui.click()
    time.sleep(5)
    speak('class joined')

join_class()
    

