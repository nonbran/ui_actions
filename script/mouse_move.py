from pynput.mouse import Button, Controller
from random import randint
from time import sleep

screen_x_min, screen_x_max = 1, 1919
screen_y_min, screen_y_max = 1, 1079

mouse = Controller()
for i in range(5):
    random_x_pos = randint(screen_x_min, screen_x_max)
    random_y_pos = randint(screen_y_min, screen_y_max)
    mouse.move(random_x_pos, random_y_pos)
    print(f'i moved the mouse to position x {random_x_pos} and position y {random_y_pos}!')
    sleep(.5)
