


class Point():
    def __init__(self, x, y):
        self.x, self.y = x,y

    def __sub__(self, target):
        return (abs(self.x - target.x),
                 abs(self.y - target.y))

class Geometry():
    def __init__(self, points = None):
        if points == None:
            self._points = []
        else:
            self.points = points

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points):
        for point in points:
            if not isinstance(point, Point):
                raise ValueError("Musí být typu Point!")
        self._points = points

    def move(self, start = None, target = None):
        pass
    



# Unittesting -
if __name__ == "__main__":
    # Kontrola třídy Point
    P1 = Point(1,1)
    P2 = Point(3,2)
    assert P1 - P2 == (2, 1), "Odčítání."

    # Kontrola třídy Geometry
    assert Geometry([   Point(1,2), 
                        Point(3,3)]), "Vše v pořádku"
    try:
        assert  Geometry([(1,2)]),  "Musí vyvolat výjimku ValueError!"
        raise AssertionError("Výjimka nevyvolána?!")
    except ValueError:
        pass # "OK"

    
    

                
