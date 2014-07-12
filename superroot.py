
from math import log
def super_root(N):
    count = 10              # number of digits after float point
    inc = res = 1           # start with integers
    while count:
        if res ** res > N:
            res -= inc
            count -= 1
            inc /= 10
        else:
            res += inc
    else:
        return res
    
    
                               




print(super_root(4) == 2)
print(super_root(27) == 3)
super_root(81) == 3.504339593597054

