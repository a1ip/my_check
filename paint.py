def checkio(paints, items):
    rounds, triple = divmod(items, paints)
    action = []
    for i in range(min(paints, items)):
        action.append(i)
    print(action * 2)



checkio(2, 3)  # "01,12,02"
checkio(6, 3)  # "012,012"
checkio(3, 6)  # "012,012,345,345"
checkio(1, 4)  # "0,0,1,1,2,2,3,3"
checkio(2, 5)  # "01,01,23,42,34"
