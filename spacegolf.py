from itertools import permutations as t;import math
def golf(s,r=[]):
 for p in t(s):
  i=j=c=0
  for x,y in p:c+=math.hypot(i-x,j-y);i,j=x,y
  r+=[c]
 return min(r)


def golf(s):
 c=()
 for p in t(s):
  p=list(p)+[(0,0)]
  c+=sum(math.hypot(p[i+1][0]-p[i][0],p[i+1][1]-p[i][1]) for i in range(5)),
 return min(c)
           

    
            
        
        
    
    
        
        



print(golf({(2, 2), (2, 8), (8, 8), (8, 2), (5, 5)}))# == 23.31
print(golf({(2, 2), (4, 4), (6, 6), (8, 8), (9, 9)}))# == 12.73
print(golf({(5,1),(3,1),(9,1),(1,1),(7,1)}))#==9.41
