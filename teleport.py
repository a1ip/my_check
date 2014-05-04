from pprint import pprint
from random import shuffle
def checkio(ports):
    gates = dict()
    path = ["0"] #just to avoid IndexError in path[-2]
    routes = ports.split(",")
    shuffle(routes)
    checks = list("12345678")
    for gate in range(1,9):
        gate = str(gate)
        gates[gate] = [s.replace(gate, "") for
                       s in routes if
                       gate in s]
    pprint(gates)
    return None
    #to demonstrate what is checks for.
    path.append(checks.pop(0)) #append first gate "1"
    count=len(routes)+10
    while(count):
        count -= 1
        ways_to_go = gates[path[-1]]
        if len(ways_to_go):
            way = ways_to_go[0] 
        else:
            gates.pop(path[-1])
            return checkio(ports)
        if not checks and way == "1":
            path.append(way) 
            break
        if  way != path[-1] and way != path[-2]:
            path.append(way)
            ways_to_go.remove(way)
            #gates[way].remove(path[-1])
            try: 
                checks.remove(way)
            except ValueError:
                # one mission accomplished
                count = 10 #10 attempts to find exit
        else:
              ways_to_go.append(ways_to_go.pop(0)) #append first way as last
    else:
        return checkio(ports)
    return "".join(path)[1:]


print(
    
    checkio("12,28,87,71,13,14,34,35,45,46,63,65")
    )
            
            

    
    
    
        






print(checkio("12,28,87,71,13,14,34,35,45,46,63,65"),
checkio("12,23,34,45,56,67,78,81")) 
checkio("12,28,87,71,13,14,34,35,45,46,63,65") 
checkio("12,15,16,23,24,28,83,85,86,87,71,74,56") 
checkio("13,14,23,25,34,35,47,56,58,76,68") 

