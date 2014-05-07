def checkio(m):
    return all([not (m[i][j] + m[j][i]) for
                i in range(len(m)) for
                j in range(len(m))])

ch = checkio([
    [ 0,  1,  2],
    [-1,  0,  1],
    [-2, -1,  0]]) 

print(ch)
                   
