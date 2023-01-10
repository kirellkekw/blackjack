import random as rn
import time


size = 40 # grid size
delay = 0.1 # seconds
iter = 0

#grid = [ [rn.randint(0, 1) for _ in range(size)] for _ in range(size)] # for randomized grid
grid = [[0] * size for _ in range(size)] # for empty grid

grid[2][2] = 1; grid[3][3] = 1; grid[4][2] = 1; grid[4][3] = 1; grid[4][1] = 1; # for glider


next_grid = [[0] * size for _ in range(size)]

for block in grid:
    line = ""
    for cell in block:
        line += f"{cell}  "
    line = line.replace('0', '.')
    line = line.replace("1", "#")
    print(line)
print(f"iteration 0\n---------------------------------")

def print_grid():
    global next_grid
    for block in next_grid:
        line = ""
        for cell in block:
            line += f"{cell}  "
        line = line.replace('0', '.')
        line = line.replace("1", "#")
        print(line)

def alivecheck(num, alive):
    if alive:
        if num in [2,3]:
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


    if (a,b) in [(0, 0), (0, size-1), (size-1, 0), (size-1, size-1)]:
        corner = True
    elif (a in [0, size-1]) or (b in [0, size-1]):
        side = True

    if corner:
        #print("corner detected")

        if (a,b) == (0, 0): # top left
            for cell in [grid[0][1], grid[1][1], grid[1][0], grid[size-1][size-1], grid[size-1][0], grid[0][size-1], grid[1][size-1], grid[size-1][1]]:
                if cell == 1:
                    alive_n += 1

        elif (a,b) == (size-1, 0): # bottom left
            for cell in [grid[size-2][0], grid[size-2][1], grid[size-1][1], grid[0][0], grid[size-1][size-1], grid[0][size-1], grid[size-2][size-1], grid[0][1]]:
                if cell == 1:
                    alive_n += 1

        elif (a,b) == (0, size-1): # top right
            for cell in [grid[0][size-2], grid[1][size-2], grid[1][size-1], grid[0][0], grid[size-1][size-1], grid[size-1][0], grid[1][0], grid[size-1][size-2]]:
                if cell == 1:
                    alive_n += 1

        elif (a,b) == (size-1, size-1): # bottom right
            for cell in [grid[size-2][size-1], grid[size-1][size-2], grid[size-2][size-2], grid[0][0], grid[size-1][0], grid[0][size-1], grid[size-2][0], grid[0][size-2]]:
                if cell == 1:
                    alive_n += 1
        else:
            print("critical error in corner check")

        return alivecheck(alive_n, alivestatus)

    elif side:
        #print("side detected")

        if a == 0: # top side
            for cell in [grid[0][b+1], grid[0][b-1], grid[1][b], grid[1][b+1], grid[1][b-1], grid[size-1][b], grid[size-1][b+1], grid[size-1][b-1]]:
                if cell == 1:
                    alive_n += 1


        elif b == 0: # left side
            for cell in [grid[a+1][0], grid[a-1][0], grid[a][1], grid[a+1][1], grid[a-1][1], grid[a][size-1], grid[a+1][size-1], grid[a-1][size-1]]:
                if cell == 1:
                    alive_n += 1


        elif a == size-1: # bottom side
            for cell in [grid[a][b-1], grid[a][b+1], grid[a-1][b], grid[a-1][b+1], grid[a-1][b-1], grid[0][b], grid[0][b+1], grid[0][b-1]]:
                if cell == 1:
                    alive_n += 1


        elif b == size-1: # right side
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
    next_grid = [[0] * size for _ in range(size)]
    iter += 1
    print(f"iteration {iter}\n---------------------------------")
    time.sleep(delay)