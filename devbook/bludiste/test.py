from itertools import product

def bludiste(*,sirka,vyska,start, cil):
    vchody = {start, cil}
    plocha = {(x,y) for x,y in product(range(1,sirka-1),
                                        range(1, vyska-1))}
    return plocha | vchody



def vykresli(plocha):
    for j in range(max(plocha, key=lambda x:x[1])[1]+1):
        radka = ""
        for i in range(max(plocha)[0]+1):
            radka += "." if (i,j) in obr else "-"
        print(radka)



    
s=10
v=10
obr = bludiste(sirka=s,
               vyska=v,
               start=(2,0),
               cil=(4,v-1))

vykresli(obr)



        
                
                
              
              
    




