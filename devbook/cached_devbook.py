from time import time
from random import randint



def cache(func):  	# func je funkce, kterou chceme kešovat
    memo = {}    	# slovník, ve kterém klíč(key)
                        # je argument funkce faktoriál; 
                        # a hodnota (value) je vypočtený faktoriál 
    def use_cache(*args): #tzv. closure, tj. funkce ve funkci
        if args not in memo: 
            memo[args] = func(*args)
        return memo[args]
    return use_cache


# Zápis č.1. Standardní modul
from math import factorial as factorial_1

# Zápis č.2.  Funkcionální zápis
from functools import reduce
from operator import mul
factorial_2 = lambda n: reduce(mul, range(n, 0, -1))

# Zápis č.3. Rekurze
def factorial_3(n): 
    return 1 if n == 1 else n * factorial_3(n-1)


# Zápis č.4. Iterace
def factorial_4(n):
	f = 1
	for i in range(1, n+1):
		f *= i
	return f

# Odkomentujte řádek, který chcete testovat
# factorial = factorial_1; print("Standardní modul.")
factorial = factorial_2; print("Funkcionální programování.")
# factorial = factorial_3; print("Rekurze.")
# factorial = factorial_4;   print("Iterace.")


# stručná kontrola správnosti kódu
# pro případ, že by někdo chtěl experimentovat
# se zápisy jednotlivých funkcí.
for i in range(10):
    check = randint(1, 900)
    # kontrola vůči standardnímu pythonovskému faktoriálu
    assert factorial(check) == factorial_1(check), check




scope = (1000, 1010) # funkční obor 
repeat = 20   # počet volání funkce

# Vypočítáme vhodnost
print("Vhodnost: {}".format(round(repeat/(scope[1]-scope[0]), 1)))

# Náhodně generovaná množina celých čísel.
values = [randint(*scope) for i in range(repeat) ]
start = time()
for value in values:
    factorial(value)
delay_no_dec = time() - start
print("Doba měřená s nekešovanou funkcí je: {} s.".
                          format(
                            round(delay_no_dec, 5)))

start = time()
factorial = cache(factorial)
for value in values:
    factorial(value)
delay_with_dec = time() - start
print("Doba měřená s kešovanou funkcí je: {} s.".
                          format(
                              round(delay_with_dec, 5)))

print("Kešovaná funkce je: {}krát rychlejší.".
                      format(round(
                          delay_no_dec / delay_with_dec, 1) ))

