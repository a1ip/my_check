
def golf2(n):
 s,k=set(),2
 while(1):
  s.update(set(i for i in range(k,n*n,k)));k+=1
  if k not in s and k>n and int(str(k)[::-1])==k:return k if n>1 else 2
  
def golf(n):
 while(1):
  n+=1
  if all(n%i!=0 for i in range(2,n)) and int(str(n)[::-1])==n:return n
    
    




                







if __name__ == "__main__":
    assert golf(1) == 2
    assert golf(2) == 3
    assert golf(13) == 101
    assert golf(101) == 131
    #assert golf(999999) == 1003001