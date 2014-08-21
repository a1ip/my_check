import constants as CONST

EAST, NORTH_EAST, NORTH = "Východ", "Severovýchod", "Sever"


DIRECTIONS = {0: EAST,
              45: NORTH_EAST,
              90: NORTH}



class Piece():
    def __init__(self,
                 name:str, *,
                 direction = CONST.RIGHT):    # North
        self.name = name
        self.direction = direction
        pass
    def __repr__(self):
        direction = DIRECTIONS[self.direction]
        return "{} míří na {}".format(self.name,
                                      direction)



    def turn(self, way: "angle in range "):
        self.direction += way
        return 1
    def attack(self):
        pass
    def go(self, steps = 1):
        pass






def test():
    print("zadej neco:")
    input()
    return True

def show_friends(game):
    pass

commands = {"end": lambda: False,
            "test": test}


from playboard import Playboard

class Game():
    def __init__(self,
                 playboard: Playboard,
                 friends: dict,
                 enemies: dict):
        self.friends = friends
        self.enemies = enemies
        self.playboard = Playboard
        self.start()

    def start(self):
        again = True
        while again:
            print("Your choice?".upper())
            again = commands[input().lower()]()
            print(10 * "x " + CONST.NEW_LINE)
        print(CONST.NEW_LINE +
              "End of game".upper())




friendly_pieces = {i:Piece("f" + str(i)) for i in range(3)}
enemy_pieces = {i:Piece("e" +str(i)) for i in range(3)}




game = Game(Playboard(width = 10,
                      height = 10),
            friendly_pieces,
            enemy_pieces)



