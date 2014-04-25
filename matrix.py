def check_pattern(mat):
    for i in mat:
        print(i)
    print("***********************")
    check = lambda x: len(set(x))==1 #checking 4 same numbers
    if check((          #diagonal- from topleft to rightdown
        mat[0][0],
        mat[1][1],
        mat[2][2],
        mat[3][3])) or \
        check((         #diagonal- from topright to leftdown
        mat[0][3],
        mat[1][2],
        mat[2][1],
        mat[3][0])):
        return True
    l = []
    for i in range(4):
        if check(mat[i][0:4]): #check of lines
            return True
        for j in range(4):
            l.append(mat[j][i]) #check of columns
        if check(l):
            return True
        l=[]
    return False


def checkio(mat):
    l=[]
    for y in range(len(mat[0])-4):
        for x in range(len(mat)-4):
            for i in range(4):
                l.append(mat[x+i][y:y+4])
            if check_pattern(l):
                return True
            l=[]
    else:
        return check_pattern(mat)
    return False
        
    

            



x = checkio([[1,2,1,1],
             [1,1,4,1],
             [1,3,1,6],
             [1,7,2,5],
             [1,7,2,5]])

print(x)







