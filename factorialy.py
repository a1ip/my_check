from math import factorial
from random import randint

def my_fact1(x):
    return 1 if x == 1 else x * my_fact1(x-1)


functions = [name for name in locals() if name.startswith("my_func")]

for f in functions:
    for __ in range(10):
        number = randint(1,1000)
        assert (locals()[f](number) ==
                factorial(number), number)
                    


    
