import itertools

#initilazyation
MINE = "x"
EMPTY = 0
CONNECTED = "o"
#change these 2 values
length = 5
mineAmount = 2


def transform_1D_to_2D(arr, n):
    return [arr[i:i+n] for i in range(0, len(arr), n)]

gridList = itertools.combinations(range(length**2),mineAmount)

stack = []
win,lose = 0,0
for mineIndexList in gridList:

    #initilazing the grid

    grid = [EMPTY] * length**2
    for mineIndex in mineIndexList:
        grid[mineIndex] = MINE

    grid = transform_1D_to_2D(grid,length)

    for x in range(length):
        for y in range(length):
            if grid[x][y] != MINE:
                mines = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= x + dx < length and 0 <= y + dy < length:
                            if grid[x + dx][y + dy] == MINE:
                                mines += 1
                grid[x][y] = mines
    
    # Checking if one click win is possible
    # 1) every cell with number should have adjacent empty space
    oneClickWin = True
    foundEmpty = True
    for x in range(length):
        for y in range(length):
            if grid[x][y] != EMPTY and grid[x][y] != MINE:
                foundEmpty = False
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= x + dx < length and 0 <= y + dy < length:
                            if grid[x + dx][y + dy] == EMPTY:
                                foundEmpty = True
                                break
                    if foundEmpty:
                        break
                if not foundEmpty:
                    break
        
        if not foundEmpty:
            break
    oneClickWin = foundEmpty

    # 2) if firs statement is satisfied, also every empty space should be connected to each other.
    if oneClickWin:
        breakOut = False
        for x in range(length):
            for y in range(length):
                if grid[x][y] == EMPTY:
                    stack.append((x,y))
                    while(stack):
                        current = stack.pop()
                        x,y = current[0],current[1]
                        grid[x][y] = CONNECTED
                        for dx in [-1, 0, 1]:
                            for dy in [-1, 0, 1]:
                                if 0 <= x + dx < length and 0 <= y + dy < length:
                                    if grid[x + dx][y + dy] == EMPTY:
                                        stack.append((x + dx,y + dy))
                    breakOut = True
                    break
            if breakOut:
                break

        for x in range(length):
            for y in range(length):
                if grid[x][y] == EMPTY:
                    oneClickWin = False
    if oneClickWin:
        win+=1
    else:
        lose+=1

print("possibility of one click win on a "+str(length)+"x"+str(length)+" grid with "+str(mineAmount)+" amount of mines is:\n"+str(100*(win/(win+lose)))+"%")