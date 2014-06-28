from itertools import product, combinations

def probability1(dices,
                sides,
                number):
    return sum(1 for i in
               product(range(1,sides + 1), repeat = dices)
               if sum(i) == number) / pow(sides, dices) 

from itertools import combinations_with_replacement as comb
def probability(dices,
                sides,
                number):
    count = 0
    for i in comb(range(1, sides+1), dices):
        if sum(i) == number:
            first = i[0]
            if all(r==first for r in i):
                count += 1
            else:
                count += dices
    print(count)
    return count / pow(sides, dices) 



print(probability(2, 6, 3))
print(probability(2, 3, 7))
print(probability(2, 6, 7))
print(probability(10, 10, 50))
print(probability(3, 6, 7))# == 0.0694

##probability(2, 6, 3) == 0.0556  # 2 six-sided dice have a 5.56% chance of totalling 3
##probability(2, 6, 4) == 0.0833
##probability(2, 6, 7) == 0.1667
##probability(2, 3, 5) == 0.2222  # 2 three-sided dice have a 22.22% chance of totalling 5
##probability(2, 3, 7) == 0       # The maximum you can roll on 2 three-sided dice is 6
##probability(3, 6, 7) == 0.0694
##probability(10, 10, 50) == 0.0375
