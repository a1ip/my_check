
def golf2(n):
 s,k=set(),2
 while 1:
  s.update(set(i for i in range(k,n*n,k)));k+=1
  if k not in s and k>n and int(str(k)[::-1])==k:return k if n>1 else 2
  
def golfxxx(n):
 while 1:
  n+=1;
  if int(str(n)[::-1])==n and all(n%i for i in range(2,n)):return n

golf3=lambda n:min(i for i in range(n+1,6**8) if int(str(i)[::-1])==i and all(i%j for j in range(2,i)))

def golf(n):
 while 1:
  n+=1;
  if int(str(n)[::-1])==n*all(n%i for i in range(2,n)):return n


    
    
def golf10(n):
 while 1:
  n+=1
  if all(str(n)[::-1]==str(n)and n%i for i in range(2,n)):return n




def golf5(n):
 s,r=str,range
 for k in r(n+1,200):
  if s(k)[::-1]==s(k)and all(k%i for i in r(2,k)):return k

s,r=str,range
golf6=lambda n:list(i for i in r(n+1,200)if s(i)[::-1]==s(i)and all(i%j for j in r(2,i)))[0]
        


                







if __name__ == "__main__":
    assert golf(1)  == 2
    assert golf(2) == 3
    assert golf(13)  == 101
    assert golf(101) == 131
    assert golf(999999) == 1003001
