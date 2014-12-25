from random import randint
from itertools import product
class Game(dict):
    def __init__(self, width: int,
                 height: int, visibility: int):
        self.width = width
        self.height = height
        self.visibility = visibility
        self.player = 0,0
        self.objects = {self.player:"#",              
                        (width-1,
                         height-1): "@"}   # doors
        for i in range(10):
            is_in = True
            while is_in:
                pos  = randint(width), randint(height)
                if pos not in self.objects:
                    self.objects[pos] = str(i)
                    is_in = False

    def render(self):
        x,y = self.player
        vis = self.visibility
        for i in range(max(x-vis,0),
                       min(x+vis, self.width)):
            pass
        
                    
                                           
            
        

        
