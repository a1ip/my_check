
def golf(n):
 s=[]
 k=2
 while(1):
  for i in range(k,10**3,k):
   if i not in s: s.append(i)
  k+=1
  if k not in s and k>n and int(str(k)[::-1])==k:return k
        
    
    




                







if __name__ == "__main__":
    print(golf(2))# == 3
    print(golf(13))# == 101
    print(golf(101))# == 131
