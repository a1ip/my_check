def count_gold(data):
    result = list(data[-1]) 
    for i in range(len(data)-2, -1, -1):
        for v, value in enumerate(data[i]):
            result[v] = value + max(result[v], result[v+1])
    return result[0] 
    
        



if __name__ == "__main__":
    print(count_gold((
    (1,),
    (2, 3),
    (3, 3, 1),
    (3, 1, 5, 4),
    (3, 1, 3, 1, 3),
    (2, 2, 2, 2, 2, 2),
    (5, 6, 4, 5, 6, 4, 3)
)) == 23)


    print(count_gold((
    (1,),
    (2, 1),
    (1, 2, 1),
    (1, 2, 1, 1),
    (1, 2, 1, 1, 1),
    (1, 2, 1, 1, 1, 1),
    (1, 2, 1, 1, 1, 1, 9)
)) == 15)

    print(count_gold((
    (9,),
    (2, 2),
    (3, 3, 3),
    (4, 4, 4, 4)
)) == 18)
