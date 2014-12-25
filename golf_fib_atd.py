
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def tribonacci():
    a, b, c = 0, 1, 1
    while True:
        yield a
        a, b, c = c, a + b, b + c

f=fibonacci()

res = 0
for i in range(5):
    res=next(f)




