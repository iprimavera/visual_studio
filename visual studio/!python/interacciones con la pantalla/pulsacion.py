import win32api
import keyboard
import time
import pyautogui

poner = False
while True:
    if keyboard.is_pressed("k"):
        if poner:
            poner = False
        else:
            poner = True
    if poner:
        pyautogui.click()
        time.sleep(0.4)
        if keyboard.is_pressed("k"):
            poner = False
        if keyboard.is_pressed("ñ"):
            break
    if keyboard.is_pressed("ñ"):
            break