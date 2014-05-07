from pprint import pprint
from random import shuffle
from itertools import cycle
def checkio(ports):
    exits = ports.count("1") - 1
    checks = list("2345678")
    routes = ports.split(",")
    shuffle(routes)
    path = "01"

    count = 50
    while(count):
        shuffle(routes)
        count -= 1
        route = routes[0]
        pos = path[-1]
        if pos in route:
            way = route.replace(pos,"")
            if way != path[-2]:
                path += way
                routes.remove(route)
               
        
        
    print(path)
                    
        
        

    

    
    


print(
    
    checkio("12,28,87,71,13,14,34,35,45,46,63,65")
    )
            
            

    
    
    
        






checkio("12,28,87,71,13,14,34,35,45,46,63,65"),
checkio("12,23,34,45,56,67,78,81")
checkio("12,28,87,71,13,14,34,35,45,46,63,65") 
checkio("12,15,16,23,24,28,83,85,86,87,71,74,56") 
checkio("13,14,23,25,34,35,47,56,58,76,68") 

