def checkio(num):
    # STEP 1 - finding digits
    i = 2
    res = []
    while i:
        if num % i == 0:
            num /= i
            res.append(i)
        else:
            if i < 9:
                i+=1
            else:
                if num > 9:
                    return 0
                else:
                    i = 0
                    num = 0
    
    # STEP 2 - preparing result
    result = [1]
    while res:
        p = res.pop(0)
        if p * result[0] < 10:
            result[0] *= p
        else:
            result.insert(0,p)
    
    # STEP 3 - preparing number to return
    result = sorted(result)
    i = len(result)-1
    while result:
        num += result.pop(0)*10**i
        i -= 1

    return num
        
        
        

print(checkio(10))

