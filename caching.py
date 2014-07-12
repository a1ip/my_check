from functools import reduce
from operator import mul
from random import randint
from time import time
from math import hypot


def cache(func):
    hist={}
    def hidden(*args):
        if args not in hist: hist[args] = func(*args)
        return hist[args]
    return hidden
    



def factorial(n):
    return reduce(mul, range(1,n+1))

def time_me(func, interval, scope):
    start = time()
    for i in range(1, scope):
        func(randint(1, interval))
    return ("čas funkce  {}".
            format(round(time()-start, 3)))

def time_me_hypot(func, interval, scope):
    start = time()
    for i in range(1, scope):
        func(randint(1, interval), 1)
    return ("čas funkce  {}".
            format(round(time()-start, 3)))



        




if __name__ == "__main__":
      assert factorial(3) == 6, "první"
      assert factorial(4) == 24, "druhy"

      print("Funkce factorial")  
      interval = 1000
      scope = 10**2
      print("Bez cache je...")  
      print(time_me(factorial, interval, scope))

      factorial = cache(factorial)
      print("S cache je...")
      print(time_me(factorial, interval, scope))
      
#***********************************************
       
      print("\n" +
            "Funkce hypot")  
      interval = 100
      scope = 10**6
      print("Bez cache je...")  
      print(time_me_hypot(hypot, interval, scope))

      hypot = cache(hypot)
      print("S cache je...")
      print(time_me_hypot(hypot, interval, scope))


     




