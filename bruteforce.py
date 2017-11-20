from pyautogui import press, typewrite, hotkey
import time 

time.sleep(1.5)    

for x in range(0000,9999):
	y = str(x)
	typewrite(y) .    #simulates keyboard input
	hotkey('enter')   #simulates "enter" key 

