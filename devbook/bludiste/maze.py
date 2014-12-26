from itertools import product
from random import shuffle
from operator import add


DISTANCE = 20                                   # Rozestup mezi body bludiště
WIDTH, HEIGHT = DISTANCE * 10, DISTANCE * 20    # Bludiště by mělo být násobkem DISTANCE
SIZE = max(HEIGHT, WIDTH)
ORTHO = [(DISTANCE,0), (0,DISTANCE),    # Kolmé cesty od bodu X,Y
         (-DISTANCE,0),(0,-DISTANCE)]   # vlevo, vpravo, dolů, nahoru 

def add_point(point, increment):
    """
    Pomocná funkce, která vrácí součet dvou bodů.
    >>> add_point((1,1),(2,2)) == (3,3)
    >>> True
    """
    return tuple(map(add, point, increment))
    
def generate_maze(*, start=(0,0)):
    """
    Generátor hran bludiště.
    Ze startu lze dojít do kteréhokoliv bodu bludiště,
    proto není potřeba zadávat cíl.
    """
    ways = ORTHO
    # Vytvoříme množinu bodů bludiště
    points = {(x,y) for x,y in product(range(0,WIDTH+DISTANCE,DISTANCE),
                                       range(0,HEIGHT+DISTANCE,DISTANCE))}
    # Ze bodů v starts vyrážíme do dalších bodů
    starting_points = {start}
    while points:
        ends = set()
        for point in starting_points:
            shuffle(ways)   # Zamícháme směry.
            # POkusíme se jít každým směrem.
            for way in ways:
                new_point = add_point(point, way)
                if new_point in points:
                    # Prošlý bod nás už nezajímá
                    points.remove(new_point)
                    ends.add(new_point)
                    yield point, new_point
                    break
            else:
                # Pokud neexistuje žádný volný směr (žádný break)
                # tento bod už nepotřebujeme procházet.
                ends.add(point)
        starting_points ^= ends #odebereme mrtvé body a přidáme nové.
    return


def create_graph_of_maze(edges):
    """
    Převede seznam hran na graf reprezentovaný slovníkem.
    Klíče keys jsou body.
    Hodnoty values jsou množiny bodů.
    """
    graph = dict()
    for start, end in edges:
        graph.setdefault(start,set()).add(end)
        graph.setdefault(end, set()).add(start)
    return graph


def find_path(start, end, *, graph):
    """
    Vrací seznam bodů, které je potřeba projít ze začátku do cíle.
    Hledá první cestu, ne nejrychlejší.
    Tak či tak, víc jich v bludišti stejně není :)
    Algoritmus testuje, zda z posledního bodu cesty může jít dál.
    POkud nemůže, odstraňuje body cesty tak dlouho, dokud se nedostane
    na další křižovatku.
    Zde si vybere další směr, kterým zatím neprošel.
    Pokud neexistuje žádná cesta, vyhodí se výjimka.
    """
    way = [start]
    while True:
        last_point = way[-1]
        if graph[last_point]:
            point = graph[last_point].pop()
            graph[point].remove(last_point)
            way.append(point)
            if point == end:
                return way
        else:
            way.pop()
    raise ValueError("Cesta nenalezena")

if __name__ == "__main__":
    print("Spusťte main.py.")
    
        
        
        
   
