def checkio(cros, words):
    code = list()
    alphabet = ""
    cipher = {0:" "}
    for line in cros:
        code.extend(([str(i) for i in line if i != 0]))
    for c in words:
        alphabet += c
    print(code)
    
    
    keys = {x: alphabet.count(x) for x in set(alphabet)}
    # alphabet_suggest = {x: code.count(x) for x in set(code)}

    
    alpha_coding=dict().fromkeys(set(keys.values()),tuple())
    num_coding = dict().fromkeys(alpha_coding.keys(),tuple())
    
    for key in set(alphabet):
        print(key, alphabet.count(key))
        alpha_coding[alphabet.count(key)] += key,

    for key in set(code):
        num_coding[code.count(key)] += key,

    print(alpha_coding)
    print(num_coding)
    



checkio(
    [
        [21, 6, 25, 25, 17],
        [14, 0, 6, 0, 2],
        [1, 11, 16, 1, 17],
        [11, 0, 16, 0, 5],
        [26, 3, 14, 20, 6]
    ],
    ['hello', 'habit', 'lemma', 'ozone', 'bimbo', 'trace'])





    
