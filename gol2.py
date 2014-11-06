LIVE, DIE = 1,0
from itertools import product
from collections import defaultdict

AROUND = tuple((x,y) for x,y in
               product((-1,0,1), repeat=2) if
               (x,y) != (0,0))

def do(board, ticks):
    if not ticks:
        return sum(board.values())
    new_life = dict()
    for (x,y), val in board.items():
        count = 0
        for i,j in AROUND:
            coord = x+i, y+j
            if coord in board.keys():
                if board[coord]:
                    count += 1 
            else:
                new_life[coord] = DIE
        coord = x,y
        if count == 0:
            board.pop(coord)
        elif count < 2:
            new_life[coord] = DIE
        elif count == 2:
            new_life[coord] = LIVE if val else DIE
        elif count == 3:
            new_life[coord] = LIVE
        elif count > 3:
            new_life[coord] = DIE
        else:
            raise ValueError("Something wrong!")
    board.update(new_life)
    return do(board, ticks-1)
        
                
def life_counter(seed, ticks):
    start = dict()
    width, length = len(seed[0]), len(seed)
    for x in range(-1, width+1):
        for y in range(-1,length+1):
            if x in range(width) and y in range(length):
                        start[(x,y)] = seed[y][x]
            else:
                        start[(x,y)] = 0
    return do(start, ticks)
    





print(life_counter(((0, 1, 0),
                         (0, 0, 1),
                         (1, 1, 1)), 50))




print(life_counter((    (0, 1, 0, 0, 0, 0, 0),
                        (0, 0, 1, 0, 0, 0, 0),
                        (1, 1, 1, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 1, 1),
                        (0, 0, 0, 0, 0, 1, 1),
                        (0, 0, 0, 0, 0, 0, 0),
                        (1, 1, 1, 0, 0, 0, 0)), 4)) #15
