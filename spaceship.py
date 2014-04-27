checkio(data):
    width = len(data[0])
    height = len(data)
    good_land = "G", "S"
    result = []
    x = 0
    y = 0
    counting = False 
    
    while(True):
        x %= width
        y %= height
        land = data[y][x]
        if land in good_land and not counting:
            counting = True

        elif ...:
            pass

        #end while
        if x >= width and y >= height:
            break
            
            
           
            
        



li =['GGTGG','TGGGG','GSSGT','GGGGT','GWGGG','RGTRT','RTGWT','WTWGR']
checkio(li)
