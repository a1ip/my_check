start = set()
end = set()
sep = "-"

def find_moves(fro):
    pass

def checkio(data, count = 1):
    data = data.split(sep)
    start.add(data[0])
    end.add(data[1])
    if start & end:
        return count
    else:
        

    




if __name__ == "__main__":
    checkio("b1-d5") == 2, "First"
    checkio("a6-b8") == 1, "Second"
    checkio("h1-g2") == 4, "Third"
    checkio("h8-d7") == 3, "Fourth"
    checkio("a1-h8") == 6, "Fifth"
