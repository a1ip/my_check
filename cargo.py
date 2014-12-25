def cargo(data, half):
    if sum(data) <= half:
        return 0
    result = list()
    for i in range(len(data)):
        copy = data.copy()
        val = copy.pop(i)
        result.append(val + cargo(copy, half) )   
    return (min(result))

checkio = lambda data: cargo(sorted(data), sum(data)//2)*2-sum(data)





test = [1,5,6,8]


assert cargo(test, 10)==11          #22-20
assert cargo([1,2,1,2], 3) == 3     #2*3-6
assert cargo([1,1,1,17], 10) == 17  #2*17-20
assert cargo([10],10) == 0          #2*0-10


assert checkio([10,10]) == 0
assert checkio([10]) == 10
assert checkio([5, 8, 13, 27, 14]) == 3
assert checkio([5,5,6,5]) == 1
assert checkio([12, 30, 30, 32, 42, 49]) == 9
assert checkio([1, 1, 1, 3]) == 0
