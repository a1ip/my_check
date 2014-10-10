def indices(length, total):
    for i in range(0, total - length + 1):
        yield range(i, i + length)

#returns width, height of matrix
dimensions = lambda matrix: len(matrix[0]), len(matrix)

    
    
