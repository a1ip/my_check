from itertools import combinations_with_replacement as cwr
from math import factorial 

def probability(dices,
                sides,
                value):
    return round((
                sum(factorial(len(set(shot))) for
                shot in cwr(range(1,sides), dices) if
                sum(shot) == value) /
                sides ** dices), 4)







print(probability(2, 6, 3))# == 0.0556  # 2 six-sided dice have a 5.56% chance of totalling 3
print(probability(2, 6, 4))# == 0.0833
print(probability(2, 6, 7))# == 0.1667
probability(2, 3, 5) == 0.2222  # 2 three-sided dice have a 22.22% chance of totalling 5
print(probability(2, 3, 7))# == 0       # The maximum you can roll on 2 three-sided dice is 6
print(probability(3, 6, 7))# == 0.0694
print(probability(10, 10, 50))# == 0.0375
