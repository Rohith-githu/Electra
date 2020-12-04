import pyautogui
import time
import webbrowser
from pyttsx3 import *
def main():
    webbrowser.open('https://meet.google.com')
    time.sleep(5)
    new = pyautogui.locateCenterOnScreen('new_meeting.png')
    pyautogui.moveTo(new)
    pyautogui.click()

    time.sleep(3)
    instant = pyautogui.locateCenterOnScreen('instant.png')
    pyautogui.moveTo(instant)
    pyautogui.click()
    time.sleep(8)
    join_btn = pyautogui.locateCenterOnScreen('join_now.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(5)
    speak('meeting joined')
    copy_btn = pyautogui.locateCenterOnScreen('copy_info.png')
    pyautogui.moveTo(copy_btn)
    pyautogui.click()
    speak('meeting info copied to clipboard')

main()
