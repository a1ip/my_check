from operator import add, sub, mul, truediv
from itertools import combinations_with_replacement as cwr


INDEXES = [tuple(map(int,i)) for k in range(1,7) for
           i in cwr("123456",k)  if
           sum(int(j) for j in i) == 6]


OPER = [op for op in cwr((add,sub,mul, truediv),5)]

print(INDEXES)
print(OPER)

    
