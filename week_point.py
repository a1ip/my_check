"""
    Summary:
    Calculate sum of every column and row.
    Go through matrix and sum intersected
    column and row.
    If this value is smaller then minimum,
    save coordinates of position as result.
"""
 
def weak_point(matrix):
    rows = {i: sum(row) for i, row in enumerate(matrix)}
    columns = {i: sum(column) for i, column in
                enumerate(zip(*matrix))}
    result = None   # This line is not necessary, but code is clearer
    minimum = 1000  # Every next value is expected to be smaller.
    for y, row in enumerate(matrix):
        for x, col in enumerate(row):
            value = rows[y] + columns[x]
            if  value < minimum:
                minimum = value
                result = [y,x]
    return result




assert weak_point([[7, 2, 7, 2, 8],
            [2, 9, 4, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]]) == [3, 3]

assert weak_point([[7, 2, 4, 2, 8],
            [2, 8, 1, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]]) == [1, 2]
        
