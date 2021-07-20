import pywhatkit
import pyautogui as pt
import time

limit = 50
message = "GooD MorninG"
pywhatkit.sendwhatmsg('+910000000000',message,8,10)
i = 0
time.sleep(3)
while i<int(limit):
    pt.typewrite(message)
    pt.press("enter")
    i+=1

