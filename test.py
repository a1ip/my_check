# tahy konem
from itertools import permutations as p
l = [(x,y) for x,y in p([-2,-1,1,2], 2) if abs(x) != abs(y)]
print(l)

