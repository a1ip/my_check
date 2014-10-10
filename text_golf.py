def golf(d):
    s=slice(1,-1)
    for k in d[]:
        for i,j in enumerate(k[s]):
            if j in " " and all(filter(not str.isdigit



golf(["How are you doing?",
      "I'm fine. OK.",
      "Lorem Ipsum?",
      "Of course!!!",
      "1234567890",
      "0        0",
      "1234567890",
      "Fine! good buy!"]) == 3
