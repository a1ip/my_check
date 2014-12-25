WAYS =((0,1),(0,-1),(1,0),(-1,0))
def can_pass(matrix, start, end):
    points_to_go = {(x,y) for x in range(len(matrix)) for
                     y in range(len(matrix[0])) if
                     matrix[x][y] == matrix[start[0]][start[1]]}
    can_I_go = {start}
    while can_I_go:
        x,y = can_I_go.pop()
        for i,j in WAYS:
            point = x+i, y+j
            if point == end:
                return True
            elif point in points_to_go:
                can_I_go.add(point)
        points_to_go.remove((x,y))
    return False
        

            
            
        




print(can_pass(((0, 0, 0, 0, 0, 0),
          (0, 2, 2, 2, 3, 2),
          (0, 2, 0, 0, 0, 2),
          (0, 2, 0, 2, 0, 2),
          (0, 2, 2, 2, 0, 2),
          (0, 0, 0, 0, 0, 2),
          (2, 2, 2, 2, 2, 2),),
         (3, 2), (0, 5)))# == True, 'First example'

print(can_pass(((0, 0, 0, 0, 0, 0),
          (0, 2, 2, 2, 3, 2),
          (0, 2, 0, 0, 0, 2),
          (0, 2, 0, 2, 0, 2),
          (0, 2, 2, 2, 0, 2),
          (0, 0, 0, 0, 0, 2),
          (2, 2, 2, 2, 2, 2),),
         (3, 3), (6, 0)))# == False



print(can_pass(((3,3,2,2,2),
          (2,2,3,3,3),
          (3,3,2,2,2),
          (3,2,2,2,3),
          (2,3,2,2,2),
          (2,3,2,3,3)),
         (5,2), (0,2)))
