import pyautogui
import time
n = 0
while n<30: #as much time you want to send message
    pyautogui.sleep(4) #it will send a message every 4 seconds
    pyautogui.typewrite("Amake ekta Macbook Pro M2 Max 1TB storage er laptop kine diba?:)")
    pyautogui.press('enter')
    n+=1