
def evaluate(neg):
    return (0
            if not neg
            else neg[0] +
            max(evaluate(neg[1:]),
                 evaluate(neg[2:])))
    
def checkio(data):
    count = 0
    neg = list() # list of negative numbers
    data.append(0) #border conditions
    for d in data:
        if d > -1:
            count += d
            if neg: # sequence of negatives is stopped
                count += evaluate([0] + neg)
                neg.clear()
        else:
            neg.append(d)
    return count
            
        
        
        
    
    
    

    
    





checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27])

print(checkio([5, -3, -1, 2])) #== 6
print(checkio([5, 6, -10, -7, 4]))# == 8
checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]) == 393
print(checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27]))# == 125

