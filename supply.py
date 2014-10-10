def supply_routes(matrix):
    mapa = {(x,y): matrix[y][x] for
                    y in range(len(matrix)) for
                    x in range(len(matrix[0]))}
    print(mapa)






supply_routes(("..........",
               ".1X.......",
               ".2X.X.....",
               ".XXX......",
               ".X..F.....",
               ".X........",
               ".X..X.....",
               ".X..X.....",
               "..3.X...4.",
               "....X....."))
