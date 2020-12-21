import subprocess
import pyautogui
import time
from commands import *
from pyttsx3 import speak
def sign_in(meeting_id, password) :
    subprocess.call("C:\\Users\\rohit\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    time.sleep(5)
    meeting_button = pyautogui.locateCenterOnScreen('join_button.png')
    pyautogui.moveTo(meeting_button)
    pyautogui.click()

    meeting_id_screen = pyautogui.locateCenterOnScreen('meeting_id_input.png')
    pyautogui.moveTo(meeting_id_screen)
    pyautogui.click()
    pyautogui.write(meeting_id)

    join_btn = pyautogui.locateCenterOnScreen('join_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(3)

    passcode = pyautogui.locateCenterOnScreen('passcode.png')
    pyautogui.moveTo(passcode)
    pyautogui.click()
    pyautogui.write(password)
    pyautogui.press('enter')
    time.sleep(3)
    say('joined meeting')

id_meeting = input("Enter the meeting id ")
password = input("Enter the password ")
sign_in(id_meeting, password)