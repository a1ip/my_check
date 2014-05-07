from pprint import pprint
def checkio(data):
    def check(x,y,value):
        data[y][x] = 0
        count = 1
        for pos in ((-1,0),(0,-1),
                    (0,1), (1,0)):
            try:
                x1 = x + pos[0]
                y1 = y + pos[1]
                if x1 < 0 or y1 <0: continue
                if data[y1][x1] == value:
                    count += check(x1,y1,value)
            except IndexError:
                pass
        return count

    result = [0,0]
    for y in range(len(data)):
       for x in range(len(data[0])):
           val = data[y][x]
           if val != 0:
               temp = [check(x,y,val), val]
               result = (temp if temp[0] > result[0]
                         else result)
        
    return result





if __name__ == "__main__":
    mapa = [
    [2, 1, 2, 2, 2, 4],
    [2, 5, 2, 2, 2, 2],
    [2, 5, 4, 2, 2, 2],
    [2, 5, 2, 2, 4, 2],
    [2, 4, 2, 2, 2, 2],
    [2, 2, 4, 4, 2, 2]]
    pprint(mapa)
    pprint(checkio(mapa))
            
