def golf(t):
    c=0
    for i in range(1, len(t)-1):
        for j in range(1,len(t[0])-1):
            if t==" " and " " not in (t[i+1][j],t[i-1,j], t[i][j+1],t[i][j-1]):c+=1
    print(c)
    return c
            




golf(["How are you doing?",
      "I'm fine. OK.",
      "Lorem Ipsum?",
      "Of course!!!",
      "1234567890",
      "0        0",
      "1234567890",
      "Fine! good buy!"]) == 3
