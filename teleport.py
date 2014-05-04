from pprint import pprint
def checkio(ports):
    gates = dict()
    path = ["0"] #just to avoid index error in path[-2]
    ports = ports.split(",")
    checks = list("12345678")
    for gate in range(1,9):
        gate = str(gate)
        gates[gate] = [s.replace(gate, "") for
                       s in ports if
                       gate in s]
    #to demonstrate what is checks for.
    path.append(checks.pop(0)) #append first gate "1"
    #count = 0 #to prevent endless loop
    while(True):
        #count+=1
        #if count >50: break #sorry, Bryug
        ways_to_go = gates[path[-1]]
        way = ways_to_go[0]
        if not checks and way == "1":
            path.append(way) 
            break
        if  way != path[-1] and way != path[-2]:
            path.append(way)
            try: 
                checks.remove(way)
            except ValueError:
                pass
        ways_to_go.append(ways_to_go.pop(0)) #append first way as last

    #print("".join(path)[1:])
    return "".join(path)[1:]
            
            

    
    
    
        






checkio("12,28,87,71,13,14,34,35,45,46,63,65")
checkio("12,23,34,45,56,67,78,81") 
checkio("12,28,87,71,13,14,34,35,45,46,63,65") 
checkio("12,15,16,23,24,28,83,85,86,87,71,74,56") 
checkio("13,14,23,25,34,35,47,56,58,76,68") 

