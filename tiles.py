from math import ceil
def checkio(radius):
    """
    Function is optimalized
    using symmetry counting of tiles.
    Right now, I am going through 1/8th of grid
    except for values of diagonal
    which are not multiplied by 8 but only 4
    at the return.
    """
   
    tiles = ceil(radius)  #square size / 2
    root = 2 ** 0.5
    solid = 0
    partial = 0
    # from top to bottom
    for y in range(tiles, 0, -1):
        # from right to left
        for x in range(tiles, 0, -1):
            if x <= y: break #stop when diagonal
            diagonala = (x**2 + y**2) ** 0.5
            # partial checking and counting
            if  (diagonala > radius and
                 ((x-1)**2 + (y-1)**2) ** 0.5 < radius):
                partial += 8
            # solid checking and counting
            elif diagonala <= radius:
                solid += (x - y) * 8
                break # next line
    return [solid + (4 * int(radius//root)),
            partial + 4]



if __name__ == "__main__":
    assert checkio(4) == [32,28]
    assert checkio(2.1) == [4,20], "spatne"
    assert checkio(2.5) == [12, 20]
    assert checkio(3) == [16, 20]
    assert checkio(2.2) == [4,20]
