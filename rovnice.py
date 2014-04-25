ALLOWED=("+","-")
def simp(formula): #zjednoduší +/- operace
    seznam = list()
    prvek=""
    check=False
    for exp in formula:
        if exp in ALLOWED:
            if check:
                if prvek: 
                    seznam.append(prvek)
                check=False
                prvek=""
            prvek += exp
        elif exp.isnumeric():
            prvek+=exp
            check=True
        else:
            prvek += exp
            seznam.append(prvek)
            prvek=""
    if prvek:
        seznam.append(prvek)
    return seznam

print(simp("-x+6+2x+3x+5-x"))
    
    
