from itertools import permutations as p
# possible Knight moves
moves = [(x,y) for x,y in p([-2,-1,1,2], 2)
         if abs(x) != abs(y)]

# helper function "b1" -> (2,1)
conv = lambda pos: (ord(pos[0])-96, int(pos[1]))

# allowed coordinates {(1,1), ..., (8,8)}
CHECKBOARD = {(x,y) for x in range(1,9)
              for y in range(1,9)}

def checkio(check,              #starting input e.g. "b1-d5"
            start: set = None,   
            end: set = None,
            count = 0):         # Knight moves counter 
    if check:                   # Only first call, then not used
        start = {conv(check[:2])} # conversion to coordinates tuple
        end = {conv(check[-2:])}
    elif start & end:           # solution is found and returned
        return count            # N.B.: if "b1-b1" 0 moves is returned
    count += 1
    pos = set() #helper set
    for x_s, y_s in start:
        for x_m, y_m in moves:
            pos |= {(x_s+x_m,
                   y_s+y_m)}
    start |= pos & CHECKBOARD  # only coord of checkboard are added        
    return checkio(False,      # No need anymore
                   end,        # !!! end is switched for start !!!
                   start,      # a vice versa
                   count)   

        
            






        





if __name__ == "__main__":
    assert checkio("b1-d5") == 2, "First"
    assert checkio("a6-b8") == 1, "Second"
    assert checkio("h1-g2") == 4, "Third"
    assert checkio("h8-d7") == 3, "Fourth"
    assert checkio("a1-h8") == 6,  "Fifth"
