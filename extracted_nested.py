def flat_list(arr):
 res = []
 while arr:
   i = arr.pop()
   arr.extend(i) if isinstance(i,list) else res.insert(0,i)
 return res

def flat_list2(arr):
 res=[]
 while arr:
  try:
   i=arr.pop()
   arr.extend(i)
  except:
   res.insert(0,i)
 return res

print(flat_list([1, [2, [3, 4]]]))
#checkio([1, [2, 2, 2], 4])
#checkio([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])
