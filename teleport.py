import random

def helper(one, more):
    if set(one) & set(more):
        return "".join(set(more)-set(one))
    return ""

def checkio(values):
    val=values.split(",")
    val=random.sample(val,len(val))
    ones = list(x for x in val if x.find("1")>-1)
    popped=ones.pop()
    firstPos="1"
    nextPos=helper(firstPos, popped)
    val.remove(popped)
    route=list(firstPos)
    count=0

    while(len(val)>1):
        count+=1
        if count>len(val)*1000:
            print(val)
            break
            #return checkio(values)
        popped=random.choice(val)
        pos=helper(nextPos, popped)
        if pos:
           
            if popped in ones and len(ones)>1:
                ones.remove(popped)
            elif popped in ones:
                continue
           
            route.append(nextPos)
            nextPos=pos
            val.remove(popped)
            
    
    #route.append(helper("1",val[0]))  
    route.append("1")
    #print(route)
    return str(route)






checkio("12,28,87,71,13,14,34,35,45,46,63,65")
checkio("12,28,87,71,13,14,34,35,45,46,63,65")
checkio("12,28,87,71,13,14,34,35,45,46,63,65")
#checkio("12,23,34,45,56,67,78,81") == "123456781"
"""
checkio("12,28,87,71,13,14,34,35,45,46,63,65") == "1365417821"
checkio("12,15,16,23,24,28,83,85,86,87,71,74,56") == "12382478561"
checkio("13,14,23,25,34,35,47,56,58,76,68") == "132586741"
"""
