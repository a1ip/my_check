from collections import defaultdict
from itertools import product
check = lambda c, n:(c[0]+n[0], c[1]+n[1])  
def life_counter(board, ticks, mydict=None):
    ticks -= 1
    neighbours = [val for val in product((-1,0,1), repeat=2)]
    neighbours.remove((0,0))
    board = {(x,y):board[y][x] for
            y in range(len(board)) for
            x in range(len(board[0]))} if board else mydict
    b = dict()
    b.update(board)
    board.clear()
    for key, value in b.items():
        #key = 6,3
        count = 0
        for val in neighbours:
            coord = check(val, key)
            if coord in b.keys():
                count += 1 if b[coord] else 0
            else:
                board[coord] = 0
        if count < 2:
            board[key] = 0
            print("die", key)
        elif count == 2:
            board[key] = 1 if value else 0
            print("living live", key, board[key])
        elif count == 3:
            board[key] = 1
            print("Always live", key)
        elif count > 3:
            board[key] = 0
            print("always die", key)
        else:
            raise ValueError("Not expected value!")

    b.update(board)
    board.clear()
    return (life_counter(None, ticks, b) if ticks > 0 else
            sum(b.values()))





print(life_counter((  (0, 1, 0, 0, 0, 0, 0),
                (0, 0, 1, 0, 0, 0, 0),
                (1, 1, 1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0, 1, 1),
                (0, 0, 0, 0, 0, 1, 1),
                (0, 0, 0, 0, 0, 0, 0),
                (1, 1, 1, 0, 0, 0, 0)), 1))
