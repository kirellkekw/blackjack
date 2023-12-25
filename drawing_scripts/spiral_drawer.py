# draws a spiral with given paramaters

from time import sleep
import math
import pyautogui

radius = 420  # radius of the spiral in pixels
points_to_draw_per_rotation = 30  # how many points to draw per rotation
rotation_count = 10  # how many rotations to draw
center = (960, 540)  # center of the screen

sleep(3)

radius_decrease_per_point = radius / \
    (rotation_count * points_to_draw_per_rotation)
degrees_to_move = 360 / points_to_draw_per_rotation
total_degrees: float = 90  # start at 90 degrees to draw the spiral from the top


def find_spiral_points(center: tuple, radius: int, points_to_draw_per_rotation: int, rotation_count: int):
    global total_degrees
    points = []
    for rotation in range(rotation_count):
        for point in range(points_to_draw_per_rotation):
            new_x = center[0] + radius * math.cos(math.radians(total_degrees))
            new_y = center[1] + radius * math.sin(math.radians(total_degrees))
            points.append((new_x, new_y))
            total_degrees += degrees_to_move
            radius -= radius_decrease_per_point
            if total_degrees >= 361:
                total_degrees -= 360
            if radius <= 0:
                return points
    return points


points = find_spiral_points(
    center, radius, points_to_draw_per_rotation, rotation_count)

pyautogui.mouseDown(points[0][0], points[0][1])
for point in points:
    pyautogui.moveTo(point[0], point[1])
    if point == points[-2]:
        pyautogui.mouseUp()
        break

pyautogui.moveTo(center[0], center[1])

print("Done!")
