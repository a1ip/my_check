# Check description of steps below the code :)
AROUND = ((-1, -1), (-1, 0), (-1, 1),(0, -1),
          (0, 1), (1, -1), (1, 0), (1, 1))
CELLS = AROUND + ((0,0),)

def life_counter(seed, ticks):
    life = {(x,y) for x in range(len(seed[0])) for
            y in range(len(seed)) if seed[y][x] == 1}
    locate = lambda pos1, pos2:(pos1[0]+pos2[0],
                                  pos1[1]+pos2[1])
    for __ in range(ticks):
        new_life = set()
        for living in life:
            for pos in (locate(living, cell) for
                        cell in CELLS):
                count = sum((locate(pos, cell) in life) for
                            cell in AROUND)
                if count == 2:
                    if pos in life: new_life.add(pos)
                elif count == 3:
                    new_life.add(pos)
                else:
                    pass
        life = new_life         
    return len(life)

"""
STEPS DESCRIPTION
1. Convert data to set of positions of living cells
2. Evaluating every living cell + all its neighbours (9 cells together)
3. All 9 cells (CELLS) are checked for count of surrounding living cells(AROUND).
4. Based of evaluation, still living or newly born cells are added to new set.
5. New set is switched for the old one.
6. Next iterations starts at point 2
7. Desired number is returned as length of set life.

AROUND - surrounding of cell
CELLS - The same as AROUND including cell itself
locate - helper function to calculate desired position

"""
    
    

        
                



print(life_counter(((0, 1, 0, 0, 0, 0, 0),
                         (0, 0, 1, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0)), 4)) 

