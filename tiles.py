from math import ceil, sqrt
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
    root = sqrt(2)
    solid = 0
    partial = 0
    # from top to bottom
    for y in range(tiles, 0, -1):
        # from right to left
        for x in range(tiles, 0, -1):
            if x <= y: break #stop when diagonal
            diagonala = (pow(x,2) + pow(y,2)) 
            # partial checking and counting
            if (diagonala > radius ** 2 and
                 pow((x-1),2) + pow((y-1),2) < pow(radius,2)):
                partial += 8
            # solid checking and counting
            elif diagonala <= pow(radius,2):
                solid += (x - y) * 8
                break # next line
    return [solid + (4 * int(radius//root)),
            partial + 4]


#konkurence
from math import sqrt, ceil
 
def checkio2(r):
    return [4*sum(int(sqrt(r*r-x*x)) for x in range(1,int(r)+1)), 8*ceil(r)-4]


from math import floor, ceil, sqrt
 
def checkio3(radius):
    """count tiles"""
    full = 0
    total = 0
    # Count only one quadrant, and multiply by 4.
    # Loop through rows "r"
    leftheight = radius
    for r in range(int(ceil(radius))):
        if radius > r+1:
            rightheight = sqrt(radius**2 - (r+1)**2)
        else:
            rightheight = 0
        full += int(rightheight)
        total += int(ceil(leftheight))
        leftheight = rightheight
    #print(radius, "->", [4*full, 4*(total-full)])
    return [4*full, 4*(total-full)]

print(checkio3(80))
if __name__ == "__main__":
    assert checkio(4) == [32,28]
    assert checkio(2.1) == [4,20], "spatne"
    assert checkio(2.5) == [12, 20]
    assert checkio(3) == [16, 20]
    assert checkio(2.2) == [4,20]

    from timeit import timeit
    print("The time is: {: f} s". format(
        timeit("checkio(100)",
        number = 1000,
        setup="from __main__ import checkio")))

    print("The time is: {: f} s". format(
        timeit("checkio2(100)",
        number = 1000,
        setup="from __main__ import checkio2")))

    print("The time is: {: f} s". format(
        timeit("checkio3(100)",
        number = 1000,
        setup="from __main__ import checkio3")))








    
