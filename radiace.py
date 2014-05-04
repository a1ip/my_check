def checkio(matrix):
      

    for y, line in enumerate(matrix):
        print(line)
        for x, value in enumerate(line):
            
            if value:
                #print(x,y,value)
                pass
                


ch = [[0,1,0],
      [0,0,0],
      [1,1,1]]

checkio(ch)
"""
ch = checkio([
    [1, 2, 3, 4, 5],
    [1, 1, 1, 2, 3],
    [1, 1, 1, 2, 2],
    [1, 2, 2, 2, 1],
    [1, 1, 1, 1, 1]]) == [14, 1]


ch = checkio([
    [2, 1, 2, 2, 2, 4],
    [2, 5, 2, 2, 2, 2],
    [2, 5, 4, 2, 2, 2],
    [2, 5, 2, 2, 4, 2],
    [2, 4, 2, 2, 2, 2],
    [2, 2, 4, 4, 2, 2]]) == [19, 2]
    """


