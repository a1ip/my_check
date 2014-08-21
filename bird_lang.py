VOWELS = "aeiouy"
def translate(speech):
    translation = []
    skip = 0
    for letter in speech:
        if skip:
            skip -= 1  
            continue
        elif letter not in VOWELS and letter.isalpha():
            skip += 1
        elif letter in VOWELS:
            skip += 2
        translation.append(letter)
    return "".join(translation)




print(translate("hieeelalaooo"))# == "hello"
print(translate("hoooowe yyyooouuu duoooiiine"))# == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"
