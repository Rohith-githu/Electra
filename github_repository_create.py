import webbrowser
import pyautogui
import time
from pyttsx3 import *
def repository(name) :
    webbrowser.open('https://www.github.com')
    time.sleep(7)

    new_create = pyautogui.locateCenterOnScreen('new_repo.png')
    pyautogui.moveTo(new_create)
    pyautogui.click()
    time.sleep(5)
    repo_blank = pyautogui.locateCenterOnScreen('repo_blank.png')
    pyautogui.moveTo(repo_blank)
    pyautogui.click()
    pyautogui.write(name)

    new_create = pyautogui.locateCenterOnScreen('repo_create.png')
    pyautogui.moveTo(new_create)
    pyautogui.click()

name = input('Enter the repository name :')
repository(name)
speak(f'Github repository created as {name}')