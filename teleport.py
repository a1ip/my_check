path = ""
def checkio(ports, start="1"):
    ports += ","
    if start not in ports:
        return ""
    
    for port in ports.split(","):
        if start in port:
            path = start + checkio(
                        ports.replace(port + ",", ""),
                        port.replace(start, ""))
            return path                   
##            if (path[-1] == "1" and
##                set(path) == set("12345678")):
##                return path
    else:
        return ""
                
            
    
    
        














def checkio2(ports,
            pos = "1",
            checkpoints = "2345678"):
    if "1" not in ports:
        return ""
    for port in ports.split(","):
        if pos in port:
            going = port.replace(pos, "")
            if not checkpoints and going != "1":
                return ""
            elif going == "1" and not checkpoints:
                return pos + "1"
            go = checkio(ports.replace(port+",", ""),
                         going,
                         checkpoints.replace(going, ""))
            if go:
                return pos + go
            
    return ""
            
                         
                         
    



print(checkio("12,23,34,45,56,67,78,81"))
#print(checkio("12,28,87,71,13,14,34,35,45,46,63,65"))# == "1365417821"
#print(checkio("12,15,16,23,24,28,83,85,86,87,71,74,56"))# == "12382478561"
#print(checkio("13,14,23,25,34,35,47,56,58,76,68"))# == "132586741"
print(checkio("13,14,23,25,34,35,47,56,58,76,68"))
            

    
    
    
        





