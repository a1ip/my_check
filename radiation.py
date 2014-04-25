def checkio(data):
    li = []
    for i in data:
        li.extend([str(j) for j in i])
    s = "".join(li)    
    #s = "".join([str(i) for i in data])
    d = {x: s.count(x) for x in set(li)}
    print(list(d))
    






res = checkio([
    [2, 1, 2, 2, 2, 4],
    [2, 5, 2, 2, 2, 2],
    [2, 5, 4, 2, 2, 2],
    [2, 5, 2, 2, 4, 2],
    [2, 4, 2, 2, 2, 2],
    [2, 2, 4, 4, 2, 2]]) # == [19, 2]

print(res)
