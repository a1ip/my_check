class Bat():
    batmap = list()
    bats = list()       #list of available bats
    _x = 0
    _y = 0
    

    def is_seen_by(self, obj):
        return True
    
    def distance_to(self, obj):  #use only for visible bats
        dist = lambda x1,x2: abs(x1-x2)**2 
        return round((dist(self.x,obj.x) + dist(self.y,obj.y))**0.5, 2)
        #odmocnina ze čtverce vzdálenosti 

    @property
    def visible_bats(self):
        if self.bats:
            return self.bats
        for b in Bat.bats:
            if b.is_seen_by(self):
                self.bats.append(b)
        return self.bats

    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y

    def set_pos(self,x,y): #SMAZAT!!!
        self._x=x
        self._y=y
        
    def start(batmap):   #beginning of code
        Bat.batmap = batmap
        return time


b1 = Bat()
b1.set_pos(1,1)
b2 = Bat()
b2.set_pos(3,3)
print(b1.distance_to(b2))


