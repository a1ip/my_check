def checkio(stairs):
    result = sum([i for i in stairs if i >0])
    stairs = [i for i in stairs if i < 0] 
    length = len(stairs)
    test = 0
    test1 = 0
    last = 0
    step = 0
    for i in range(0,length,2):
        if step > 1:
            test += 
        

    print(test)
    print(test1)
    return result + (test if test > test1 else test1) 
        
    








Li = [1,2,3,-4,-6,-10, -7,8,-9]
print(checkio(Li))

assert checkio([1,2])==3
assert checkio([-1,-2,-3]) == -2
assert checkio([5, -3, -1, 2]) == 6
assert checkio([5, 6, -10, -7, 4]) == 8
assert checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]) == 393
assert checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27]) == 125
