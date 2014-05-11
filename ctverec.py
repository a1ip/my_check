from pprint import pprint


"""
If you feel like this
you can check this solution:
http://www.checkio.org/mission/calculate-islands/publications/hanpari/python-3/readability-counts/share/f06121dd1339a4669d3d0e6e82a6264b/
to compare two different approach.
Both solutions are similar with one
exception: the previous one is using
matrix transform from list
to dictionary based on Guidos comment:
http://www.checkio.org/mission/open-labyrinth/publications/Miaou/python-3/dijkstras-forever/

You can judge by yourself
if readability was approved or not.
Feel free to express your opinion in comments below.
"""

def checkio(data):
    width = len(data[0])
    height = len(data)
    result = [0,0]
    def check(x,y,value):
        """
        using recursion the function 
        is counting all valid fields
        (equals to value)until
        they are present. Valid field
        is disabled as 0 and function returns
        count of all found valid field.
        """
        data[y][x] = 0
        count = 1
        for pos in ((-1,0),(0,-1),
                    (0,1), (1,0)):
            x1 = x + pos[0]
            y1 = y + pos[1]
            if  (x1 < 0 or
                 x1 >= width  or
                 y1 < 0 or
                 y1 >= height):
                continue
            if data[y1][x1] == value:
                count += check(x1,y1,value)
        return count
    for y in range(height):
       for x in range(width):
           val = data[y][x]
           if val != 0:
               temp = [check(x,y,val), val]
               result = (temp if
                         temp[0] > result[0]
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
            
