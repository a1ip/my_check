
import math
def checkio(a, b, c):
    angles = list()
    a,b,c=sorted([a,b,c])
    if a+b <= c:
        return [0,0,0]
    angles.append(math.degrees(math.acos(c*(a/(a+b))/a)))
    angles.append(math.degrees(math.acos(c*(b/(a+b))/b)))
    print(angles)



checkio(3,4,5)
