KEYS = dict()
KEYS.update({str(x): x+1 for x in range(1,10)})
KEYS.update({chr(x): x-54 for x in range(65,91)})

def checkio(num):
    radix = KEYS[sorted(num)[-1]]
    for i in range(radix, 37):
        if int(num, i) % (i-1) == 0:
            return i
    else:
        return 0
