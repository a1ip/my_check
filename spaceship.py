checkio(data):
    width = len(data[0])
    height = len(data)
    good_land = "G", "S"
    result = []
    x = 0
    y = 0
    counting = False 
    
    while(True):
        #[x % width] returns endless 0 to width - 1
        land = data[y][x % width]  
        if land in good_land and not counting:
            counting = True

        elif ...:
            pass

        #end while
        if x%width == width-1 and y == height-1: break
            
            
           
            
        



li =['GGTGG','TGGGG','GSSGT','GGGGT','GWGGG','RGTRT','RTGWT','WTWGR']
checkio(li)
