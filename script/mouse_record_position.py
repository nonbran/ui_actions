from datetime import datetime as dt
from pynput.mouse import Button, Controller
from time import sleep

mouse = Controller()

while 1:
    print(f'at {dt.now()}the mouse is located at {mouse.position}')
    sleep(1)
