# this script is a modified version of the perfect_circle.py script
# this draws shapes with more points each cycle
# and connects all the points to each other
# creating a cool effect

from time import sleep
import math
import pyautogui

points_to_pass = 4 # must be even number, minimum 4
cycle_for = 5 # how many cycles to do
center = (960, 540) # center of the screen, change unless you have a 1920x1080 monitor or if you want to draw somewhere else
radius = 300  # higher number = bigger drawing circle = more required resolution


sleep(3) # wait 3 seconds before starting

cycle = 1 # this might be tempting for you to change, but don't.

while cycle < cycle_for + 1:


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

    # now connect all the points to each other
    for index in range(len(points)):
        if index == len(points) - 1:
            break
        for index2 in range(index, len(points)):
            if index2 == len(points) - 1:
                break
            pyautogui.moveTo(points[index][0], points[index][1])
            pyautogui.dragTo(points[index2][0], points[index2][1])
            if index2 == len(points) - 1:
                break

    print(f"cycle {cycle} Done!")
    cycle += 1
    points_to_pass += 2
