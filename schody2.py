
def evaluate(data):
    return 0 if not data else data[-1] + max(evaluate(data[:-1]), evaluate(data[:-2]))

def checkio(data):
    return evaluate([0] + data + [0])
            
        
        
        
    
    
    

    
    





checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27])

print(checkio([5, -3, -1, 2])) #== 6
print(checkio([5, 6, -10, -7, 4]))# == 8
checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]) == 393
print(checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27]))# == 125

