# this scripts picks a random point on a circle and moves the mouse to that point until the user stops the script

from time import sleep
import math
import pyautogui
from random import randint

radius = 350
center = (960, 540)

sleep(3)



def move_to_random_point(x: int, y: int, radius: int):
    random_angle = randint(0, 360)
    random_radius = randint(0, radius)
    new_x = x + random_radius * math.cos(math.radians(random_angle))
    new_y = y + random_radius * math.sin(math.radians(random_angle))
    pyautogui.moveTo(new_x, new_y)


pyautogui.mouseDown(center[0], center[1])
while True:
    move_to_random_point(center[0], center[1], radius)
