# http://www.mathsisfun.com/algebra/matrix-determinant.html


from collections import deque
from functools import reduce
from operator import mul

def checkio(mat):
    size = len(mat)
    line = [i for i in range(size)]
    forward = deque(line)
    count = 0
    for __ in line:
        count += reduce(mul, (mat[x][y] for x,y in
                              zip(line, forward)))
        count -= reduce(mul, (mat[x][y] for x,y in
                              zip(line, reversed(forward))))
        forward.append(forward.popleft())
    print(count)
    return count
                



assert checkio([[4, 3],
                [6, 3]]) == -6, 'First example'

assert checkio([[1, 3, 2],
                [1, 1, 4],
                [2, 2, 1]]) == 14, 'Second example'
