from math import ceil
def checkio(radius):
    """
    Function could be optimalized
    using symmetry counting of tiles.
    Right now, I am going through 1/4th of grid
    but you can go only through 1/8th.
    Then, you must not multiply diagonal tiles by 8, only by 4.
    I gave up this optimalization
    to make my code less complicated.
    """
    #square size / 2
    tiles = ceil(radius)
    result = [0,0]
    for x in range(1, tiles + 1):
        for y in range(1, tiles + 1):
            # check for solid tiles
            if (((x**2)+
                (y**2))**(1/2) <= radius):
                result[0] += 4
            # check for partial tiles
            elif ((((x-1)**2)+
                ((y-1)**2))**(1/2) <= radius):
                result[1] += 4
    return result



if __name__ == "__main__":
    assert checkio(2.1) == [4,20], "spatne"
    assert checkio(2.5) == [12, 20]
    assert checkio(3) == [16, 20]
