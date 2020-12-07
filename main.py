import pyautogui, time
import webbrowser
from pyttsx3 import *

webbrowser.open("https://www.practically.com")
time.sleep(10)
var1 = pyautogui.locateCenterOnScreen('var1.png')
pyautogui.moveTo(var1)
pyautogui.click()
time.sleep(1)

pass_blank = pyautogui.locateCenterOnScreen('login_id_blank.png')
pyautogui.moveTo(pass_blank)
pyautogui.click()
pyautogui.write('bpt0257')
pass_fill = pyautogui.locateCenterOnScreen('password_blank.png')
pyautogui.moveTo(pass_fill)
pyautogui.click()
pyautogui.write('pass@123')
var2 = pyautogui.locateCenterOnScreen('var2.png')
pyautogui.moveTo(var2)
pyautogui.click()
time.sleep(2)
var3 = pyautogui.locateCenterOnScreen('var3.png')
pyautogui.moveTo(var3)
pyautogui.click()
time.sleep(5)
speak('class joined')

    

