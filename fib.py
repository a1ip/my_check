def fib(number):
    fib_dict = {0:1, 1:1}
    for i in range(2, number+1):
        fib_dict[i] = fib_dict[i-2] + fib_dict[i-1]
    return fib_dict[number]


def fib2(number):
    fili = [1,1]
    [fili.append(fili[i-2] +
                 fili[i-1]) for
                 i in range(2, number+1)]
    return fili[-1]

def fib3(number):
    zero = first = 1
    for i in range(2, number + 1):
        zero, first = first, zero + first
    return first


if __name__ == "__main__":
    x = 5
    print(fib(x))
    print(fib2(x))
    print(fib3(x))
