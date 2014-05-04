def checkio(right):

    Li = [(i,y) for i in sorted(right) for
          y in sorted(right, reverse=True)]
    print(Li)

checkio([1,2,3,4,5,6])
        
        
