import itertools as i

def golf2(x, d=1):
       if d in sum(([sum(y) for y in i.combinations(x,z)] for z in range(1,len(x)+1)),[]):
              return golf(x,d+1)
       else:
              print(d)
              return d
       
import itertools as i
golf=lambda x,d=1:golf(x,d+1)if d in sum(([sum(y)for y in i.combinations(x,z)]for z in range(12)),[])else d





def golf4(x):
       s=[sum(x)]
       while len(x):
              for i in x:
                     s+=[sum(x)-i]
              x.pop()
       print(s)       
       for i in range(1,99):
              if i not in s: return i
              
              
       



print(golf4([10, 2, 2, 1]))

assert golf([10, 2, 2, 1]) == 6
assert golf([1, 1, 1, 1]) == 5
assert golf([1, 2, 3, 4, 5]) == 16
