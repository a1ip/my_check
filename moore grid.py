
def count_neighbours(grid, y, x):
    scope = (-1,0,1)
    around = ((y,x) for y in scope for x in scope if x or y)
    count = 0
    for b,a in around:
        b += y
        a += x
        if (0 <= b < len(grid) and
            0 <= a < len(grid[0]) and
            grid[b][a]):
            count += 1
    return count
    



assert count_neighbours(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 1, 2) == 3
assert count_neighbours(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 0, 0) == 1    
