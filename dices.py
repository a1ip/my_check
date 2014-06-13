from itertools import product

def probability(dices, sides, value):
    s = [i for i in range(1,sides+1) if value % i == 0]
    print(s)
    return (sum(1 for i in product(s,repeat=dices)
               if sum(i)==value) / (sides ** dices))





print(probability(2, 6, 3))# == 0.0556  # 2 six-sided dice have a 5.56% chance of totalling 3
print(1)
print(probability(2, 6, 4))# == 0.0833
print(1)
probability(2, 6, 7) == 0.1667
print(1)
probability(2, 3, 5) == 0.2222  # 2 three-sided dice have a 22.22% chance of totalling 5
print(1)
probability(2, 3, 7) == 0       # The maximum you can roll on 2 three-sided dice is 6
print(1)
probability(3, 6, 7) == 0.0694
print(1)
probability(10, 10, 50) == 0.0375
