from itertools import product

fields = range(8)
whites = {(x, 1 if x%2 else 0) for x in fields}
white_queens = set()
blacks = {(x, 7 if x%2 else 6) for x in fields}
black_queens = set()

def generate():
    playboard = dict()
    for pos in product(fields, fields):
        playboard[pos] = ("W" if pos in whites else
                          "B" if pos in blacks else
                          "WQ" if pos in white_queens else
                          "BQ" if pos in black_queens else
                          " " if sum(pos)%2 else ".")
    return playboard



def move(color, where):
    try:
        old, new = ((int(x), int(y)) for x,y in where.split("x"))
        color.remove(old)
        color.add(new)
        return True
    except:
        return False
    

def render():
    playboard = generate()
    for y in fields:
        print("".join(" {} ".format(playboard[(x,y)]) for x in fields))
    print(20*"*")



if __name__ == "__main__":
    render()
    move(whites, "00x33")
    
    render()
