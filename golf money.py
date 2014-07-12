def golf(s, i=1): 
       k=sum(sorted(s[:i]))
       print(k)
       return golf(s, i+1) if k in s else k
       





print(golf([10, 2, 2, 1]))# == 6
#golf([1, 1, 1, 1]) == 5
#golf([1, 2, 3, 4, 5]) == 16
