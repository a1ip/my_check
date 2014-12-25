from itertools import product
from random import choice
from operator import add, mul
from turtle import Turtle

DISTANCE = 5 
WAYS = ((-DISTANCE, 0), (0, -DISTANCE), (0, DISTANCE), (DISTANCE, 0))
_WAYS = ( (-DISTANCE, -DISTANCE),
         (-DISTANCE, DISTANCE),
         (DISTANCE, -DISTANCE),
         (DISTANCE, DISTANCE))


class Maze(Turtle):
    def __init__(self, start=(10,10), end=(160,160),
                 width=200, height=200):
        Turtle.__init__(self)
        self.hideturtle()
        self.screen.bgcolor("blue")
        self.screen.setworldcoordinates(-DISTANCE, -DISTANCE,
                                        DISTANCE+width,
                                        DISTANCE+height)

        self.screen.tracer(30,0)
        self.pensize(5)
        self.color("white", "black")
        lab = {start} 
        while True:
            new_points = set()
            for point in lab:
                x,y = map(add, point, choice(WAYS))
                if (0 <= x <= width and
                    0 <= y <= height and
                    (x,y) not in lab and
                    (x,y) not in new_points):
                    self.penup()
                    self.goto(*point)
                    self.pendown()
                    self.goto(x,y)
                    new_points.add((x,y))
            if new_points or end not in lab:
                lab |= new_points
            else:
                break
        self.mark_targets(start, end)
        self.maze_map = lab
        self.start = start
        self.end = end
        print("KONEC")

    def find_way(self):
        start, end, lab = self.start, self.end, self.maze_map
        path = [start]

    def mark_targets(self, start, end):
        self.pencolor("red")
        for x,y in  (end, start):
            self.penup()
            self.goto(x,y)
            self.pendown()
            self.begin_fill()
            self.dot(5)
            self.end_fill()
        
            
        
        
        
        



if __name__ == "__main__":
    maze = Maze()
    
    

    





    
                              
        
    
