from itertools import product
def checkio(area):
    width, height = len(area[0]), len(area)         # 1    
    good_land = set("GS")
    results = {0}
    c1 = c2 = c3 = 0
    for x,y in product(range(width, 0, -1),         # 2
                       range(height, 0, -1)):
        c1 += 1
        if max(results) >= x * y:                   # 3
            continue
                                                    # 4
        for x_start, y_start in product(range(width - x + 1),
                                        range(height - y + 1)):
            c2 += 1
            if next((False for x_pos, y_pos in
                   product(range(x_start, x_start + x),
                           range(y_start, y_start + y))
                    if area[y_pos][x_pos] not in good_land), True):  
                results.add(x * y) 
                break                               # 6
    print (c1 * c2) 
    return max(results)

##1. Variables definition
##2. Creating rectangles from the biggest to the smallest ones
##3. If size (x * y) of rectangles is already in results, just continue
##4. Shift rectangle in all possible position
##5. If rectangle contains only G or S, add its size to results
##6. Skip to another size, this one is not necessary to evaluate anymore
            


        




assert checkio(['G']) == 1
assert checkio(['GS','GS']) == 4
assert checkio(['GT','GG']) == 2
assert checkio(['GGTGG','TGGGG',
                'GSSGT','GGGGT',
                'GWGGG','RGTRT',
                'RTGWT','WTWGR']) == 9
