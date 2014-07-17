def swapsort(rods):
    rods = list(rods)
    i = 0
    res = []
    while i < len(rods) - 1:
        if rods[i] > rods[i+1]:
            res.append(str(i)+str(i+1))
            rods[i], rods[i+1] = rods[i+1], rods[i]
        else:
            i +=1
    res = ",".join(res)
    if sorted(rods) == rods:
        return res
    else:
        return res + "," + swapsort(rods)
        






print(swapsort((6, 4, 2)))# == "01,12,01"
print(swapsort((1, 2, 3, 4, 5)))# == ""
print(swapsort((1, 2, 3, 5, 3)))# == "43"
