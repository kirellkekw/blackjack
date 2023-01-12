import random as rn
import time


height = 20     # horizontal lenght
width = 20      # vertical lenght
delay = 0.1     # time between iterations in seconds
random = False  # for randomized grid, cannot work with glider
glider = True   # to add a glider to empty grid, cannot work with random

if random:
    grid = [[rn.randint(0, 1) for _ in range(width)] for _ in range(height)]  # for randomized grid

elif glider:
    grid = [[0] * width for _ in range(height)]  # for empty grid
    grid[7][2] = 1
    grid[8][3] = 1
    grid[9][2] = 1
    grid[9][3] = 1
    grid[9][1] = 1  # for glider

iter = 0        # iteration counter

next_grid = [[0] * width for _ in range(height)]

def print_grid():
    global next_grid
    final = ""
    for block in grid:
        line = ""
        for cell in block:
            line += f"{cell}  "
        line = line.replace('0', '.')
        line = line.replace("1", "#")
        final += line
        final += "\n"
    print(final)



print_grid()
print(f"iteration 0\n---------------------------------")


def alivecheck(num, alive):
    if alive:
        if num in [2, 3]:
            return 1
        return 0
    else:
        if num == 3:
            return 1
        return 0


def statecheck(a, b):

    global grid
    corner = False
    side = False
    alive_n = 0
    if grid[a][b] == 1:
        alivestatus = True
    else:
        alivestatus = False

    if (a, b) in [(0, 0), (0, width-1), (height-1, 0), (height-1, width-1)]:
        corner = True
    elif (a in [0, height-1]) or (b in [0, width-1]):
        side = True

    if corner:
        #print("corner detected")

        if (a, b) == (0, 0):  # top left
            for cell in [grid[0][1], grid[1][1], grid[1][0], grid[height-1][width-1], grid[height-1][0], grid[0][width-1], grid[1][width-1], grid[height-1][1]]:
                if cell == 1:
                    alive_n += 1

        elif (a, b) == (height-1, 0):  # bottom left
            for cell in [grid[height-2][0], grid[height-2][1], grid[height-1][1], grid[0][0], grid[height-1][width-1], grid[0][width-1], grid[height-2][width-1], grid[0][1]]:
                if cell == 1:
                    alive_n += 1

        elif (a, b) == (0, width-1):  # top right
            for cell in [grid[0][width-2], grid[1][width-2], grid[1][width-1], grid[0][0], grid[height-1][width-1], grid[height-1][0], grid[1][0], grid[height-1][width-2]]:
                if cell == 1:
                    alive_n += 1

        elif (a, b) == (height-1, width-1):  # bottom right
            for cell in [grid[height-2][width-1], grid[height-1][width-2], grid[height-2][width-2], grid[0][0], grid[height-1][0], grid[0][width-1], grid[height-2][0], grid[0][width-2]]:
                if cell == 1:
                    alive_n += 1
        else:
            print("critical error in corner check")

        return alivecheck(alive_n, alivestatus)

    elif side:
        #print("side detected")

        if a == 0:  # top side
            for cell in [grid[0][b+1], grid[0][b-1], grid[1][b], grid[1][b+1], grid[1][b-1], grid[height-1][b], grid[height-1][b+1], grid[height-1][b-1]]:
                if cell == 1:
                    alive_n += 1

        elif b == 0:  # left side
            for cell in [grid[a+1][0], grid[a-1][0], grid[a][1], grid[a+1][1], grid[a-1][1], grid[a][width-1], grid[a+1][width-1], grid[a-1][width-1]]:
                if cell == 1:
                    alive_n += 1

        elif a == height-1:  # bottom side
            for cell in [grid[a][b-1], grid[a][b+1], grid[a-1][b], grid[a-1][b+1], grid[a-1][b-1], grid[0][b], grid[0][b+1], grid[0][b-1]]:
                if cell == 1:
                    alive_n += 1

        elif b == width-1:  # right side
            for cell in [grid[a+1][b], grid[a-1][b], grid[a][b-1], grid[a+1][b-1], grid[a-1][b-1], grid[a][0], grid[a+1][0], grid[a-1][0]]:
                if cell == 1:
                    alive_n += 1
        else:
            print("critical error in side check")

        return alivecheck(alive_n, alivestatus)
    else:

        for cell in [grid[a-1][b-1], grid[a-1][b], grid[a-1][b+1], grid[a][b-1], grid[a][b+1], grid[a+1][b-1], grid[a+1][b], grid[a+1][b+1]]:
            if cell == 1:
                alive_n += 1

    return alivecheck(alive_n, alivestatus)


while True:
    x = 0
    for block in grid:
        y = 0
        for cell in block:
            next_grid[x][y] = statecheck(x, y)
            y += 1
        x += 1

    print_grid()

    grid = next_grid

    next_grid = [[0] * width for _ in range(height)]
    iter += 1
    print(f"iteration {iter}\n---------------------------------")
    time.sleep(delay)
