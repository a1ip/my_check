from pprint import pprint
print = pprint

checkboard = {(x,y): None for x in range(1,9)
                          for y in range(1,9)}



print(checkboard)
