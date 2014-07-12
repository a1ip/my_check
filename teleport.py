def checkio(ports, path="1"):
    last = path[-1]
    if last == "1" and set(path) == set("12345678"):
        return path
    elif last not in ports:
        raise ValueError("No more to go!")
    ports = ports.split(",")
    for port in ports:
        if last in port:
            try:
                p = ports[:]
                p.remove(port)
                return checkio(",".join(p),
                               path + port.replace(last,""))
            except ValueError:
                continue
    raise ValueError("Iteration failed!")
    
                               
            
    
    
                  
                         
    



print(checkio("12,23,34,45,56,67,78,81"))
print(checkio("12,28,87,71,13,14,34,35,45,46,63,65"))# == "1365417821"
print(checkio("12,15,16,23,24,28,83,85,86,87,71,74,56"))# == "12382478561"
print(checkio("13,14,23,25,34,35,47,56,58,76,68"))# == "132586741"
print(checkio("13,14,23,25,34,35,47,56,58,76,68"))
            

    
    
    
        





