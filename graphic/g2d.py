from collections import namedtuple

Point = namedtuple("Point", ("x","y"))

class Object():
    def __init__(self, name = "Object"):
        pass


import weakref as wr

class Reference():
    _count = 0

    def __init__(self):
        print("Začátek objektu.")
        Reference._count += 1
        self.number = Reference._count

    def __del__(self):
        print("Konec objektu.")
        Reference._count -= 1

    def __repr__(self):
        return "Ref: {}".format(self.number)
        

    @staticmethod
    def get_count():
        return Reference._count


if __name__ == "__main__":
    r1 = Reference()
    r2 = Reference()
    r3 = Reference()
    assert Reference.get_count() == 3, "Počet instancí 3, což je v pořádku"
    del(r3)
    assert Reference.get_count() == 2, "Počet instancí 2, také dobře."
    #Teď si vytvořím list zbylých referencí
    seznam = [wr.ref(r1), wr.ref(r2)]
    #...a pokusím se smazat r2,
    # ve skutečnosti se ale nevolá funkce __del__ (jak bych předpokládal!)
    del(r2)
    # Takže jsem jen zrušil název proměnné
    # proto zůstal jeden odkaz na bývalou r2  v seznamu
    print(seznam)
    #Doufal jsem ve vypsání [Ref: 1, None]  :)
    #Ale __del__ prostě neproběhl
    assert Reference.get_count() == 1, "Já bych chtěl, prosím, jen r1 :)"
    



    
        
