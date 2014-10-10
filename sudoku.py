from itertools import product, chain
from pprint import pprint

def checkio(sudoku): 
    for x,y in product(range(9),
                       range(9)):
        value = sudoku[y][x]
        if value:
            sudoku[y][x] = {value}
        else:
            sudoku[y][x] = {n for n in range(1,10)}
  
    # make_cell = lambda x,y:(cell for cell in product())
    # cells = (cell for cell in product(range(3), range(3)))
    # udělat lambda funkci
    pprint(sudoku)
    r = range(0,9,3)
    for nine in chain((line for line in sudoku),
                      (column for column in zip(*sudoku))):
                      #*(make_cell(x,y) for x,y in product(r, r))):
        # špatně
        firm_pos = {num for num in nine if len(num) == 1}
        for position in nine:
            if len(position) > 1:
                position -= firm_pos

    pprint(sudoku)
    for x,y in product(range(9),
                       range(9)):
        sudoku[y][x] = sudoku[y][x].pop()
    
    return sudoku


checkio([[5, 0, 0, 7, 1, 9, 0, 0, 4],
         [0, 0, 1, 0, 3, 0, 5, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 5, 9, 7, 2, 6, 4, 0],
         [0, 0, 0, 6, 0, 1, 0, 0, 0],
         [0, 2, 6, 3, 8, 5, 9, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 3, 0, 5, 0, 2, 0, 0],
         [8, 0, 0, 4, 9, 7, 0, 0, 6]]) == [[5, 6, 8, 7, 1, 9, 3, 2, 4],
                                           [9, 7, 1, 2, 3, 4, 5, 6, 8],
                                           [2, 3, 4, 5, 6, 8, 7, 9, 1],
                                           [1, 8, 5, 9, 7, 2, 6, 4, 3],
                                           [3, 9, 7, 6, 4, 1, 8, 5, 2],
                                           [4, 2, 6, 3, 8, 5, 9, 1, 7],
                                           [6, 1, 9, 8, 2, 3, 4, 7, 5],
                                           [7, 4, 3, 1, 5, 6, 2, 8, 9],
                                           [8, 5, 2, 4, 9, 7, 1, 3, 6]]

    
            
        
        
