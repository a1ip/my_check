def list_to_dict(matrix):
    """
    Convert list matrix to dict matrix

    EXPLANATION 
    Based on this comment from Guido:
    http://www.checkio.org/mission/open-labyrinth/publications/Miaou/python-3/dijkstras-forever/#comment-outer-5200

    Especially:
    "BTW, checkio seems to have a lot of problems
    involving matrixes represented as lists of lists.
    The notation grid[i][j] looks kind of messy;
    if you were to use a single dict with tuples (i, j)
    as keys you could make the code look a little cleaner
    since you could write grid[i, j] instead.
    (Although the key tuples would end up being more expensive.)"
    (Guido van Rossum) 

    IMPROVED READABILITY?
    If you feel like this you are encouraged
    to express your opinion if such step improved readability or not.
    
    DOCTEST
    >>> matrix = [[1,2,3,4,5],\
                 [2,2,6,4,7]]
    >>> list_to_dict(matrix)
    {(0, 1): 2, (1, 2): 6, (0, 0): 1, (1, 3): 4, (0, 4): 5, (1, 0): 2, (0, 3): 4, (0, 2): 3, (1, 4): 7, (1, 1): 2}
    
    """
    
    result = dict()
    x = 0
    for element in matrix:
        for y, val in enumerate(element):
            result[x,y] = val
        x += 1
    return result


            
            





if __name__ == "__main__":
    import doctest
    doctest.testmod()
