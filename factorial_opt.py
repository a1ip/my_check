from timeit import timeit as t
from math import factorial
def fact(n):
    f = 1
    for i in range(1,n,2):
        f *= i**2 + i
    return f if not n%2 else f*n

def fact2(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

number = 10000
assert fact(number) == fact2(number)== factorial(number)

print("Moje:{}".format(t("fact(10000)","from __main__ import fact", number=100)))
print("Moj2e:{}".format(t("fact2(10000)","from __main__ import fact2", number=100)))

print("Stand:{}".format(t("factorial(10000)","from math import factorial", number=100)))



    
