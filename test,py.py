#Příklad využití anotace funkce
def secti(x:int, y:int)->int:
    """
    Vrací součet x a y
    """
    return x + y


#Tento kód je OK
secti(5, 6)
#Ale tento také! Anotace si nevynucuje typovou správnost!
secti(2, 1.1)

help(secti)






class Lazy():
    _numbers = []
    _count = None
    def add(self, number):
        self._numbers.append(number)
        self._count = None

    @property
    def count(self):
        if self._count == None:
            print("Přepočítává se...")
            self._count = sum(self._numbers)
        return self._count


l = Lazy()
print(l.count) #Výsledek 0, přepočítaný
l.add(10)
l.add(5)
print(l.count) #Výsledek 15, přepočítaný
print(l.count) #Výsledek 15, nepřepočítaný
l.add(1)
print(l.count)
print(l.count)
            
        
        
    
