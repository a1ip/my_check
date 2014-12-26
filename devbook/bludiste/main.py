from turtle import Turtle
from maze import *

SPEED = 1000   #Rychlost vykreslování

def draw_line(t: Turtle, start, end,*,
              color="white", size=1):
    t.pensize(size)
    t.pencolor(color)
    t.penup()
    t.goto(*start)
    t.pendown()
    t.goto(*end)
    

t=Turtle()          
scr = t.screen
scr.bgcolor("blue")
# Nastavíme souřadnicový systém.
scr.setworldcoordinates(-DISTANCE, -DISTANCE,
                        SIZE+DISTANCE, SIZE+DISTANCE)
scr.tracer(SPEED,0)
t.hideturtle()

# Body musí být násobky DISTANCE a samozřejmě ležet v rozsahu šířky a výšky.
# Například takto:
start_point = 0,0
end_point= WIDTH, HEIGHT 

# Není potřeba rozbalovat do setu.
# Tady jen kvůli 3d efektu, protože potřebuji vykreslit bludiště dvakrát.
# Vykresluje náhodně
maze = set(generate_maze(start=start_point))

# Pro zajímavost, jiný styl vykreslení :)
# maze = sorted(set(generate_maze(start=start_point)))


#Vykreslí posunutou šedou a pak bílou, 3d efekt
for (start, end) in maze:
    offset = 0.5,0.5
    draw_line(t, add_point(start,offset),
                 add_point(end,offset),
                 color="black", size=DISTANCE//2)
for (start, end) in maze:
    draw_line(t, start, end,
              color="gray", size=DISTANCE//2)
#Označí začátek a start    
for point in (start_point, end_point):
    t.up()
    t.goto(*point)
    t.down()
    t.dot("red")


# A pokud se nám chce, najdeme si cestu.    
g = create_graph_of_maze(maze)
p = find_path(start_point, end_point, graph=g)
for start,end in zip(p[:-1], p[1:]):
    draw_line(t, start, end, color="red", size=3)

# Ukončení vykreslení želvy, pokud řádek chybí
# bůhví proč nevykreslí poslední hranu cesty.
# Nejspíš souvisí s nastavením traceru
t.up()
# t.goto(0,0)
    
    



    
        



            
            
