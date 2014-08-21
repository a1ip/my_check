
def safe_pawns(pawns):
    # converts pawn to set of tuples (x,y) 
    pawns = {(ord(x)-96,                # convert "a" to 1, etc.
              int(y)) for x,y in pawns}
    # In fact, I am not sure if sum is so great here
    # Simple iteration might be a little bit faster ???
    # MEMO použít raději len() pro počet pravdivých řešení
    return sum((x-1, y-1) in pawns or   # exists pawn on left down diag?
               (x+1, y-1) in pawns      # exists pawn on right down diag?
               for x,y in pawns)
    



assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
