# https://neal.fun/perfect-circle/

# This script will draw a perfect circle on your screen.
# Just place your cursor in the center of the circle and run the script.
# Change the points_to_pass and radius variables according to your needs.

from time import sleep
import math
import pyautogui

# more points = smoother circle = more time needed to draw the circle
points_to_pass = 68
# higher radius = bigger circle = more required resolution
radius = 420

sleep(3)

center = (960, 560)  # center of the circle


def find_circle_points(x: int, y: int, radius: int, points_to_pass: int):

    degrees_to_move = 360 / points_to_pass

    total_degrees = 0

    found_points = []

    done = False

    while not done:
        if total_degrees >= 361:
            done = True
        new_x = x + radius * math.cos(math.radians(total_degrees))
        new_y = y + radius * math.sin(math.radians(total_degrees))
        total_degrees += degrees_to_move
        found_points.append((new_x, new_y))

    return found_points


points = find_circle_points(center[0], center[1], radius, points_to_pass)
# pre calculate the points to gain some performance

pyautogui.mouseDown(points[0][0], points[0][1])
for point in points:
    pyautogui.moveTo(point[0], point[1])
    if point == points[-2]:
        pyautogui.mouseUp()
        break

pyautogui.moveTo(center[0], center[1])

print("Done!")
