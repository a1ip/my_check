def checkio(data):
    results = [0,1]
    on_island = False
    islands = 1
    prev_line = [0 for i in data[0]]
    prev_cell = 0
    for line in data:
        for i in range(len(line)):
            if line[i]:
                line[i] = prev_cell or prev_line[i]
                results[islands] += 1 if line[i] else islands+=1
                prev_cell = line[i]
           
        prev_line = line
                
                

    return results[2:]
