
def find_distance(first, second):
    pos = 1
    x = y = 0
    spir = dict()
    way = loop = 1
    loop +=1
    while pos <= max(first, second):
        spir[pos] = (x,y)
        for i in range(1, loop):
            y += way
            pos += 1
            spir[pos] = (x,y)
        for i in range(1, loop):
            x += way
            pos += 1
            spir[pos] = (x,y)
        way *= -1
        loop += 1
    return (abs(spir[second][0] - spir[first][0]) +
            abs(spir[second][1] - spir[first][1]))
    


print(find_distance(10, 25))
        
        

    
    
    
        
