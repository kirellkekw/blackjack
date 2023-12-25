from random import randint

from colorama import Fore

from os import name, system

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# configurable variables
WIDTH = 30
HEIGHT = 16
mine = 99


#other variables
CELLCOUNT = WIDTH * HEIGHT
minecount = CELLCOUNT
game_over = False
game_win = False

#array initialization, all are 1 at start
GRID = [["X" for _ in range(WIDTH)] for _ in range(HEIGHT)]       # X is for mines, 0 is for empty cells
visible_grid = [[9 for _ in range(WIDTH)] for _ in range(HEIGHT)] # 9 for non revealed, 0 for empty neighbors

def printGrid(grid): #prints grid
    global WIDTH, HEIGHT
    clear()

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
    final += " |"
    final += "_" * (WIDTH * 3 )+"|"
    for cell in final:
        if cell == "1":
            print(Fore.LIGHTBLUE_EX + cell, end= "")
        elif cell == "2":
            print(Fore.GREEN + cell, end= "")
        elif cell == "3":
            print(Fore.RED + cell, end= "")
        elif cell == "4":
            print(Fore.BLUE+ cell, end= "")
        elif cell == "5":
            print(Fore.MAGENTA + cell, end= "")
        elif cell == "6":
            print(Fore.CYAN + cell, end= "")
        elif cell == "7":
            print(Fore.WHITE + cell, end= "")
        elif cell == "8":
            print(Fore.LIGHTCYAN_EX + cell, end= "")
        elif cell == "#":
            print(Fore.WHITE+ cell, end= "")
        elif cell == ".":
            print(Fore.YELLOW+ cell, end= "")
        elif cell == "|":
            print(Fore.LIGHTRED_EX+ cell, end= "")
        elif cell == "_":
            print(Fore.LIGHTRED_EX+ cell, end= "")
        elif cell == "x":
            print(Fore.LIGHTMAGENTA_EX+ "X", end= "")    
        else:
            print(Fore.RESET + cell,end="")
    print(Fore.RESET+"\n")
    #print(final)

def exceptionCheck(a, b): # returns 1 for corner, 2 for side, 0 for default
    global WIDTH, HEIGHT
    #print(f"exception check on {a}, {b}")
    if (a, b) in [(0, 0), (0, WIDTH-1), (HEIGHT-1, 0), (HEIGHT-1, WIDTH-1)]:
        return 1 # for corner

    elif (a in [0, HEIGHT-1]) or (b in [0, WIDTH-1]):
        return 2 # for side 

    return 0

def boardInit(): #initializes game board from zero
    global minecount, GRID
    #print("board init")
    while minecount != mine:
        randomWIDTH = randint(0, WIDTH-1)
        randomheight = randint(0, HEIGHT-1)
        selectedcell = GRID[randomheight][randomWIDTH]
        if selectedcell == "X":
            GRID[randomheight][randomWIDTH] = "0"
            minecount -= 1

def neighborCheck(a, b): # returns neighbor mine count of given cell
    global GRID
    mine_n = 0
    exception = exceptionCheck(a, b)
    #print(f"neighbor check on {a}, {b}, exception {exception}")
    if exception == 1: # corner

        if (a, b) == (0, 0):  # top left
            for cell in [GRID[0][1], GRID[1][1], GRID[1][0]]:
                if cell == "X":
                    mine_n += 1

        elif (a, b) == (HEIGHT-1, 0):  # bottom left
            for cell in [GRID[HEIGHT-2][0], GRID[HEIGHT-2][1], GRID[HEIGHT-1][1]]:
                if cell == "X":
                    mine_n += 1

        elif (a, b) == (0, WIDTH-1):  # top right
            for cell in [GRID[0][WIDTH-2], GRID[1][WIDTH-2], GRID[1][WIDTH-1]]:
                if cell == "X":
                    mine_n += 1

        elif (a, b) == (HEIGHT-1, WIDTH-1):  # bottom right
            for cell in [GRID[HEIGHT-2][WIDTH-1], GRID[HEIGHT-1][WIDTH-2], GRID[HEIGHT-2][WIDTH-2]]:
                if cell == "X":
                    mine_n += 1
        else:
            print("critical error in corner check")
    elif exception == 2: # side

        if a == 0:  # top side
            for cell in [GRID[0][b+1], GRID[0][b-1], GRID[1][b], GRID[1][b+1], GRID[1][b-1]]:
                if cell == "X":
                    mine_n += 1

        elif b == 0:  # left side
            for cell in [GRID[a+1][0], GRID[a-1][0], GRID[a][1], GRID[a+1][1], GRID[a-1][1]]:
                if cell == "X":
                    mine_n += 1

        elif a == HEIGHT-1:  # bottom side
            for cell in [GRID[a][b-1], GRID[a][b+1], GRID[a-1][b], GRID[a-1][b+1], GRID[a-1][b-1]]:
                if cell == "X":
                    mine_n += 1

        elif b == WIDTH-1:  # right side
            for cell in [GRID[a+1][b], GRID[a-1][b], GRID[a][b-1], GRID[a+1][b-1], GRID[a-1][b-1]]:
                if cell == "X":
                    mine_n += 1
        else:
            print("critical error in side check")
    else:
        for cell in [GRID[a-1][b-1], GRID[a-1][b], GRID[a-1][b+1], GRID[a][b-1], GRID[a][b+1], GRID[a+1][b-1], GRID[a+1][b], GRID[a+1][b+1]]:
            if cell == "X":
                mine_n += 1
    return mine_n

def revealCell(a, b): # reveals given cell only
    global visible_grid
    #print(f"reveal cell on {a}, {b}")
    exception_code = exceptionCheck(a, b)
    visible_grid[a][b] = neighborCheck(a, b)

def revealCellNeighbors(a, b): # reveals all neighbors of given cell
    global visible_grid, WIDTH, HEIGHT

    exception = exceptionCheck(a, b)
    #print(f"revealcellneighbors on {a}, {b}, exception {exception}")
    if exception == 1: # corner

        if (a, b) == (0, 0):  # top left
            revealCell(0, 1)
            revealCell(1, 1)
            revealCell(1, 0)
        elif (a, b) == (HEIGHT-1, 0):  # bottom left
            revealCell(HEIGHT-2, 0)
            revealCell(HEIGHT-1, 1)
            revealCell(HEIGHT-1, 1)
        elif (a, b) == (0, WIDTH-1):  # top right
            revealCell(0, WIDTH-2)
            revealCell(1, WIDTH-2)
            revealCell(1, WIDTH-1)
        elif (a, b) == (HEIGHT-1, WIDTH-1):  # bottom right
            revealCell(HEIGHT-2, WIDTH-1)
            revealCell(HEIGHT-2, WIDTH-2)
            revealCell(HEIGHT-1, WIDTH-2)
        else:
            print("critical error in corner check")

    elif exception == 2: # side

        if a == 0:  # top side
            revealCell(0, b+1)
            revealCell(0, b-1)
            revealCell(1, b)
            revealCell(1, b+1)
            revealCell(1, b-1)

        elif b == 0:  # left side
            revealCell(a+1, 0)
            revealCell(a-1, 0)
            revealCell(a, 1)
            revealCell(a+1, 1)
            revealCell(a-1, 1)

        elif a == HEIGHT-1:  # bottom side
            revealCell(a, b-1)
            revealCell(a, b+1)
            revealCell(a-1, b)
            revealCell(a-1, b+1)
            revealCell(a-1, b-1)

        elif b == WIDTH-1:  # right side
            revealCell(a+1, b)
            revealCell(a-1, b)
            revealCell(a, b-1)
            revealCell(a+1, b-1)
            revealCell(a-1, b-1)
        else:
            print("critical error in side check")
   
    else:
            revealCell(a-1, b-1)
            revealCell(a-1, b)
            revealCell(a-1, b+1)
            revealCell(a, b-1)
            revealCell(a, b+1)
            revealCell(a+1, b-1)
            revealCell(a+1, b)
            revealCell(a+1, b+1)

def revealedNeighborCheck(a, b): # checks if all neighbors of given cell are revealed, returns bool
    global visible_grid, WIDTH, HEIGHT
    exception = exceptionCheck(a, b)
    
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
                
def checkMapForSafezone(): # checks visible map for 0's recursively
    global visible_grid, GRID, WIDTH, HEIGHT
    temp_grid = visible_grid # to check if a change happened in grid

    for a in range(0, HEIGHT-1):
        for b in range(0,WIDTH-1):
            if visible_grid[a][b] == 0 and not revealedNeighborCheck(a, b): # must be tweaked to avoid infinite recursion and exception handling
                revealCellNeighbors(a, b)

def cellCheck(a, b): # event of checking a cell
    global GRID, visible_grid, game_over
    #print(f"cell check on {a}, {b}")
    if GRID[a][b] == "X": # game ends
        game_over = True
    
        for a in range(0,HEIGHT):
            for b in range(0,WIDTH):
                if GRID[a][b] == "X":
                    visible_grid[a][b] = "x" # "💣"
    
    
    else:                 # main game sequence
        mine_n = neighborCheck(a, b)
        
        visible_grid[a][b] = mine_n # reveals cell in visible grid
        
        if mine_n == 0: # if selected cell doesnt have any mine neighbors
            revealCellNeighbors(a, b)

def gameCheck(): # checks if game is complete, returns true if complete  
    global GRID, visible_grid, WIDTH, HEIGHT
    #print(f"game check")
    for a in range(HEIGHT):
        for b in range(WIDTH):
            if GRID[a][b] == "0" and visible_grid[a][b] == 9:
                return False
    return True



boardInit() # prepares game board

while not game_over:
    printGrid(visible_grid)
    x = int(input("Please enter x coordinate to check: "))
    y = int(input("Please enter y coordinate to check: "))
    cellCheck(y, x)
    for _ in range(WIDTH):
        checkMapForSafezone()
    if gameCheck(): # if all empty cells are opened
        game_over = True
        game_win = True
        break
if game_win:
    printGrid(visible_grid)
    print(Fore.GREEN + "You won!")
else:
    printGrid(visible_grid)
    print(Fore.RED + "You lost!")