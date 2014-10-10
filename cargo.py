from itertools import permutations 
def checkio(cargo):
    total = sum(cargo)
    half = cargo//2
    res = 0
    for per in permutations(cargo):
        load = 0
        for p in per:
            if load > half:
                check = total - load
                res = check if check < res else res
            elif load == half:
                return 
            else:
                
                
            
        





checkio([10,10]) == 0
checkio([10]) == 10
checkio([5, 8, 13, 27, 14]) == 3
checkio([5,5,6,5]) == 1
checkio([12, 30, 30, 32, 42, 49]) == 9
checkio([1, 1, 1, 3]) == 0
