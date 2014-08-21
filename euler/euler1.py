#5 blbe řešení
nums = [i for i in range(2,21)]
num = 931170240
while num:
    if all((not num%i) for i in nums):
        print("res:{}".format(num))
    num -= 1
    if not num%10**6: print (num)
    


        
        
        
    
    
