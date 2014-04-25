def checkio(data):
    data = data.split(",")
    ports = dict()
    for i in range(1,9):
        ports[i] = [sorted(str(num).split(str(i)))[1] for \
                    num in data if str(i) in str(num)]
        print(ports[i])

    

checkio("12,15,16,23,24,28,83,85,86,87,71,74,56") #== "12382478561"
