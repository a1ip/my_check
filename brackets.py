def checkio(eq):
    res = [0]
    for c in eq:
        if c in ("(","[","{"):
            res.append(c)
        elif c == ")" and "("!= res.pop():
            return False
        elif c == "]" and "["!= res.pop():
            return False
        elif c == "}" and "{"!= res.pop():
            return False
    
    return res.pop() == True
            
        
s = ("(1+1+{)3}")
print(checkio(s))
