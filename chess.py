start = set()
end = set()
sep = "-"

# "b1" -> (2,1)
convert = lambda pos: (ord(pos[0])-96, int(pos[1]))

def find_moves(fro):
    pass


        


# tah konem
from itertools import permutations as p
l = [(x,y) for x,y in p([-2,-1,1,2], 2) if abs(x) != abs(y)]


if __name__ == "__main__":
    checkio("b1-d5") == 2, "First"
    checkio("a6-b8") == 1, "Second"
    checkio("h1-g2") == 4, "Third"
    checkio("h8-d7") == 3, "Fourth"
    checkio("a1-h8") == 6, "Fifth"
