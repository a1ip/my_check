from random import randint
def ruleta(pocet_kol, penize, poradi):
    jednicka = 0
    for i in range(pocet_kol):
        if penize <= 0: return 0
        nahodne_cislo = randint(0,1)
        if (jednicka > poradi and
            nahodne_cislo == 0):
            penize -= 1
            jednicka = 0
        elif (jednicka <= poradi and
              nahodne_cislo == 0):
            jednicka += 1
        elif (jednicka > poradi and
              nahodne_cislo == 1):
            penize += 1
            jednicka = 0
        else:
            jednicka = 0
                
    return penize


if __name__ == "__main__":
    for i in range(10):
        opakovani = 10
        pocet_kol = 10000
        penize = 100
        poradi = 10
        print(
        sum(ruleta(pocet_kol, penize, poradi) for
            x in range(opakovani)) / opakovani)
    
