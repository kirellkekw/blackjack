from random import randint

# configurable variables
WIDTH = 50
HEIGHT = 30
mine = 40

#other variables
CELLCOUNT = WIDTH * HEIGHT
minecount = CELLCOUNT
game_over = False

#array initialization, all are 1 at start
grid = [["X" for _ in range(WIDTH)] for _ in range(HEIGHT)]       # X is for mines, 0 is for empty cells
visible_grid = [[9 for _ in range(WIDTH)] for _ in range(HEIGHT)] # 9 for non revealed, 0 for empty neighbors

def print_grid(grid): #prints grid
    global WIDTH, HEIGHT
    #final = "|"
    final = "  "
    for _ in range(WIDTH):
        final += f"{_%10}  "
    final += "\n "
    final += "_" * ((WIDTH * 3 ) + 2)
    final += "\n"
    for a in range(0, HEIGHT):
        final += f"{a%10}|"
        line = ""
        for b in range(0, WIDTH):
            line += f"{grid[a][b]}  "
        line = line.replace('0', '.')
        line = line.replace("9", "#")
        final += str(line)
        final += "|\n"
    final += "_" * ((WIDTH * 3 ) + 1)
    print(final)

def exception_check(a, b): # returns 1 for corner, 2 for side, 0 for default
    global WIDTH, HEIGHT
    #print(f"exception check on {a}, {b}")
    if (a, b) in [(0, 0), (0, WIDTH-1), (HEIGHT-1, 0), (HEIGHT-1, WIDTH-1)]:
        return 1 # for corner

    elif (a in [0, HEIGHT-1]) or (b in [0, WIDTH-1]):
        return 2 # for side 

    return 0

def board_init(): #initializes game board from zero
    global minecount, grid
    #print("board init")
    while minecount != mine:
        randomWIDTH = randint(0, WIDTH-1)
        randomheight = randint(0, HEIGHT-1)
        selectedcell = grid[randomheight][randomWIDTH]
        if selectedcell == "X":
            grid[randomheight][randomWIDTH] = "0"
            minecount -= 1

def neighbor_check(a, b): # returns neighbor mine count of given cell
    global grid
    mine_n = 0
    exception = exception_check(a, b)
    #print(f"neighbor check on {a}, {b}, exception {exception}")
    if exception == 1: # corner

        if (a, b) == (0, 0):  # top left
            for cell in [grid[0][1], grid[1][1], grid[1][0]]:
                if cell == "X":
                    mine_n += 1

        elif (a, b) == (HEIGHT-1, 0):  # bottom left
            for cell in [grid[HEIGHT-2][0], grid[HEIGHT-2][1], grid[HEIGHT-1][1]]:
                if cell == "X":
                    mine_n += 1

        elif (a, b) == (0, WIDTH-1):  # top right
            for cell in [grid[0][WIDTH-2], grid[1][WIDTH-2], grid[1][WIDTH-1]]:
                if cell == "X":
                    mine_n += 1

        elif (a, b) == (HEIGHT-1, WIDTH-1):  # bottom right
            for cell in [grid[HEIGHT-2][WIDTH-1], grid[HEIGHT-1][WIDTH-2], grid[HEIGHT-2][WIDTH-2]]:
                if cell == "X":
                    mine_n += 1
        else:
            print("critical error in corner check")
    elif exception == 2: # side

        if a == 0:  # top side
            for cell in [grid[0][b+1], grid[0][b-1], grid[1][b], grid[1][b+1], grid[1][b-1]]:
                if cell == "X":
                    mine_n += 1

        elif b == 0:  # left side
            for cell in [grid[a+1][0], grid[a-1][0], grid[a][1], grid[a+1][1], grid[a-1][1]]:
                if cell == "X":
                    mine_n += 1

        elif a == HEIGHT-1:  # bottom side
            for cell in [grid[a][b-1], grid[a][b+1], grid[a-1][b], grid[a-1][b+1], grid[a-1][b-1]]:
                if cell == "X":
                    mine_n += 1

        elif b == WIDTH-1:  # right side
            for cell in [grid[a+1][b], grid[a-1][b], grid[a][b-1], grid[a+1][b-1], grid[a-1][b-1]]:
                if cell == "X":
                    mine_n += 1
        else:
            print("critical error in side check")
    else:
        for cell in [grid[a-1][b-1], grid[a-1][b], grid[a-1][b+1], grid[a][b-1], grid[a][b+1], grid[a+1][b-1], grid[a+1][b], grid[a+1][b+1]]:
            if cell == "X":
                mine_n += 1
    return mine_n

def revealcell(a, b): # reveals given cell only
    global visible_grid
    #print(f"reveal cell on {a}, {b}")
    exception_code = exception_check(a, b)
    visible_grid[a][b] = neighbor_check(a, b)

def revealcellneighbors(a, b): # reveals all neighbors of given cell
    global visible_grid, WIDTH, HEIGHT

    exception = exception_check(a, b)
    #print(f"revealcellneighbors on {a}, {b}, exception {exception}")
    if exception == 1: # corner

        if (a, b) == (0, 0):  # top left
            revealcell(0, 1)
            revealcell(1, 1)
            revealcell(1, 0)
        elif (a, b) == (HEIGHT-1, 0):  # bottom left
            revealcell(HEIGHT-2, 0)
            revealcell(HEIGHT-1, 1)
            revealcell(HEIGHT-1, 1)
        elif (a, b) == (0, WIDTH-1):  # top right
            revealcell(0, WIDTH-2)
            revealcell(1, WIDTH-2)
            revealcell(1, WIDTH-1)
        elif (a, b) == (HEIGHT-1, WIDTH-1):  # bottom right
            revealcell(HEIGHT-2, WIDTH-1)
            revealcell(HEIGHT-2, WIDTH-2)
            revealcell(HEIGHT-1, WIDTH-2)
        else:
            print("critical error in corner check")

    elif exception == 2: # side

        if a == 0:  # top side
            revealcell(0, b+1)
            revealcell(0, b-1)
            revealcell(1, b)
            revealcell(1, b+1)
            revealcell(1, b-1)

        elif b == 0:  # left side
            revealcell(a+1, 0)
            revealcell(a-1, 0)
            revealcell(a, 1)
            revealcell(a+1, 1)
            revealcell(a-1, 1)

        elif a == HEIGHT-1:  # bottom side
            revealcell(a, b-1)
            revealcell(a, b+1)
            revealcell(a-1, b)
            revealcell(a-1, b+1)
            revealcell(a-1, b-1)

        elif b == WIDTH-1:  # right side
            revealcell(a+1, b)
            revealcell(a-1, b)
            revealcell(a, b-1)
            revealcell(a+1, b-1)
            revealcell(a-1, b-1)
        else:
            print("critical error in side check")
   
    else:
            revealcell(a-1, b-1)
            revealcell(a-1, b)
            revealcell(a-1, b+1)
            revealcell(a, b-1)
            revealcell(a, b+1)
            revealcell(a+1, b-1)
            revealcell(a+1, b)
            revealcell(a+1, b+1)

def revealedneighborcheck(a, b): # checks if all neighbors of given cell are revealed, returns bool
    global visible_grid, WIDTH, HEIGHT
    exception = exception_check(a, b)
    
    if exception == 1: # corner

        if (a, b) == (0, 0):  # top left
            for cell in [visible_grid[0][1], visible_grid[1][1], visible_grid[1][0]]:
                if cell == 9:
                    return False

        elif (a, b) == (HEIGHT-1, 0):  # bottom left
            for cell in [visible_grid[HEIGHT-2][0], visible_grid[HEIGHT-2][1], visible_grid[HEIGHT-1][1]]:
                if cell == 9:
                    return False

        elif (a, b) == (0, WIDTH-1):  # top right
            for cell in [visible_grid[0][WIDTH-2], visible_grid[1][WIDTH-2], visible_grid[1][WIDTH-1]]:
                if cell == 9:
                    return False
                  
        elif (a, b) == (HEIGHT-1, WIDTH-1):  # bottom right
            for cell in [visible_grid[HEIGHT-2][WIDTH-1], visible_grid[HEIGHT-1][WIDTH-2], visible_grid[HEIGHT-2][WIDTH-2]]:
                if cell == 9:
                    return False

        else:
            print("critical error in corner check")

    elif exception == 2: # side

        if a == 0:  # top side
            for cell in [visible_grid[0][b+1], visible_grid[0][b-1], visible_grid[1][b], visible_grid[1][b+1], visible_grid[1][b-1]]:
                if cell == 9:
                    return False
                   
        elif b == 0:  # left side
            for cell in [visible_grid[a+1][0], visible_grid[a-1][0], visible_grid[a][1], visible_grid[a+1][1], visible_grid[a-1][1]]:
                if cell == 9:
                    return False   

        elif a == HEIGHT-1:  # bottom side
            for cell in [visible_grid[a][b-1], visible_grid[a][b+1], visible_grid[a-1][b], visible_grid[a-1][b+1], visible_grid[a-1][b-1]]:
                if cell == 9:
                    return False
               
        elif b == WIDTH-1:  # right side
            for cell in [visible_grid[a+1][b], visible_grid[a-1][b], visible_grid[a][b-1], visible_grid[a+1][b-1], visible_grid[a-1][b-1]]:
                if cell == 9:
                    return False
               
        else:
            print("critical error in side check")
    
    else:
        for cell in [visible_grid[a-1][b-1], visible_grid[a-1][b], visible_grid[a-1][b+1], visible_grid[a][b-1], visible_grid[a][b+1], visible_grid[a+1][b-1], visible_grid[a+1][b], visible_grid[a+1][b+1]]:
            if cell == 9:
                return False
    
    return True
                



def checkmapforsafezone(): # checks visible map for 0's recursively
    global visible_grid, grid, WIDTH, HEIGHT
    temp_grid = visible_grid # to check if a change happened in grid

    for a in range(0, HEIGHT-1):
        for b in range(0,WIDTH-1):
            if visible_grid[a][b] == 0 and not revealedneighborcheck(a, b): # must be tweaked to avoid infinite recursion and exception handling
                revealcellneighbors(a, b)

def cell_check(a, b): # event of checking a cell
    global grid, visible_grid, game_over
    #print(f"cell check on {a}, {b}")
    if grid[a][b] == "X": # game ends
        game_over = True
    else:                 # main game sequence
        mine_n = neighbor_check(a, b)
        
        visible_grid[a][b] = mine_n # reveals cell in visible grid
        
        if mine_n == 0: # if selected cell doesnt have any mine neighbors
            revealcellneighbors(a, b)

def gamecheck(): # checks if game is complete, returns true if complete  
    global visible_grid, WIDTH, HEIGHT
    #print(f"game check")
    for a in range(HEIGHT):
        for b in range(WIDTH):
            if grid[a][b] == "0":
                return False
    return True


board_init() # prepares game board
while not game_over:
    print_grid(visible_grid)
    x = int(input("Please enter x coordinate to check: "))
    y = int(input("Please enter y coordinate to check: "))
    cell_check(y, x)
    for _ in range(WIDTH):
        checkmapforsafezone()
    gamecheck()
print("You lost!")
