from cut import cut

def checkio(houses):
    count = 0
    for x,deep,y,_,height in houses:
        points = {(x,y)}
        for X,Y in (X,Y for X,Deep,Y,_,Height in houses if
                    deep > Deep and height <= Height):
            
        
        

        

                





print(checkio([
        [1, 1, 4, 5, 3.5],
        [2, 6, 4, 8, 5],
        [5, 1, 9, 3, 6],
        [5, 5, 6, 6, 8],
        [7, 4, 10, 6, 4],
        [5, 7, 10, 8, 3]
        ]))# == 5 #"First"
print(checkio([
        [1, 1, 11, 2, 2],
        [2, 3, 10, 4, 1],
        [3, 5, 9, 6, 3],
        [4, 7, 8, 8, 2]
        ]))# == 2 #"Second"
print(checkio([
        [1, 1, 3, 3, 6],
        [5, 1, 7, 3, 6],
        [9, 1, 11, 3, 6],
        [1, 4, 3, 6, 6],
        [5, 4, 7, 6, 6],
        [9, 4, 11, 6, 6],
        [1, 7, 11, 8, 3.25]
        ]))# == 4 #"Third"
