def cut(x,y,X,Y):
    if x>=X and Y>=y:   # All vanish
        return ()
    elif X>x and y>Y:   # Divide into the two lines
        return (x,X),(Y,y)
    elif Y<x or y<X:    # Line not changed
        return x,y
    elif X<=x and Y<y:   # Cut from left
        return Y,y
    elif X>x and Y>=y:   # Cut from right
        return x,X
    else:
        # Something I didnt expect
        raise NotImplementedError(x,y,X,Y)



test = lambda x: ("Vetsi" if x>0 else
                  "Mensi" if x<0 else
                  "Rovnos")
            
            
            



x,y = 3,6
assert cut(x,y, 1,8) == (), "Prázdno"
assert cut(x,y, 4,5) == ((x,4),(5,y)), "Rozpůlení"
assert cut(x,y, 1,2) == (x,y), "Prázdno vsechno mimo"
assert cut(x,y, 1,4) == (4,y), "Zleva ořez"
assert cut(x,y, 5,10) == (x,5), "Zprava ořez"
assert cut(x,y, 1,3) == (x,y), "Zleva přiražené"
assert cut(x,y, 6,10) == (x,y), "Zprava přiraené"
assert cut(x,y, 3,4) == (4,y), "Zleva ořez"
assert cut(x,y, 5,6) == (x,5), "Zprava ořez"

assert test(5)=="Vetsi", "vetsi"
assert test(-2)=="Mensi", "Mensi"
assert test(0) == "Rovnos", "Rovno"

