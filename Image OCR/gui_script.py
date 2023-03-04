import pyautogui as gui

gui.click(90,750,duration=1.5) 
#cursor moves to search bar(for windows 10) 
#and clicks the icon with a duration of 1.5sec
gui.typewrite('cmd',interval=0.2)
#types `cmd` in search bar with interval of 0.2sec between each character
gui.press('enter')

gui.click(300,300,duration=1.5)
gui.press('f11')
gui.typewrite('cd TL',interval=0.1)
gui.press('enter')

gui.click(300,300)
gui.typewrite('python 190010041.py',interval=0.1)
gui.press('enter')