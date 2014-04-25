def Checkio(cis, root):
    res=0
    j=len(cis)-1
    for i in range(j+1):
        c=ord(cis[i])
        #print("c: {} i:{} root:{} j: {}".format(c,i,root, j))
        if 47 < c < 58:
            res += (c - 48)*(root**(j-i))
        elif 64 < c < 91:
            if root < 11:
                return 0
            res += (c-64+9) * (root**(j-i)) 
              
    return res



#print(Checkio("1010",2))




if __name__=="__main__":
     assert Checkio("A",16)==10
     assert Checkio("0",16)==0 
     assert Checkio("1010",2)==10
     assert Checkio("A",10)==0
     assert Checkio("12221",10)==12221




    

