def min(*args, key = None):
    return sorted(args,key=key)[0]

def max(*args, key = None):
    return sorted(args,key=key)[-1]






assert max(3, 2) == 3
assert min(3, 2) == 2
print( max([1, 2, 0, 3, 4]))# == 4
min("hello") == "e"
max(2.2, 5.6, 5.9, key=int) == 5.6
min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
