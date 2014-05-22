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


if __name__ == "__main__":
    print(fib(70))
    print(fib2(70))
