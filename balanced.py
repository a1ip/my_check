class Balanced():
    _smaller = _bigger = 0
    def __init__(self,
                 first = 0,
                 second = 0):
        self.add(first)
        self.add(second)

    @staticmethod
    def _get_value(obj):
        return (obj.total if
                isinstance(obj, Balanced) else
                obj)
            
        
    # only reversed sorted input seems to work
    def add(self, another):
        value = self._get_value(another)
        if self._bigger == 0:
            self._bigger = another 
        elif value > self.total:
            self._smaller = Balanced(self._bigger,
                                   self.smaller)
            self._bigger = another
        # doplnit stav kdy je another větší než bigger
        elif value > self.bigger:
            raise NotImplementedError()
        elif (value + self.smaller) > self.bigger:
            self._smaller, self._bigger = (self.bigger,
                                       Balanced(another,
                                                self._smaller))
            
        else:
            self._smaller = Balanced(self._smaller, another)

            
            
          
    @property
    def bigger(self):
        return self._get_value(self._bigger)

    @property
    def smaller(self):
        return self._get_value(self._smaller)

    @property
    def total(self):
        return self.bigger + self.smaller 





vals = [12, 30, 30, 32, 42, 49]
b = Balanced()
for v in sorted(vals, reverse=True): b.add(v)

print(b.bigger - b.smaller)

assert b.total == sum(vals), "Součet"
#assert b.bigger == 4, "bigger size"
#assert b.smaller == 3, "smaller size"
