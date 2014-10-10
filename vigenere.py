from itertools import cycle 
def decode_vigenere(decr:  "Decrypted old message.",
                    encr:  "Encrypted old message.",
                    new:   "New code to decrypt."):
    encr = cycle(encr)
    decr = cycle(decr)
    decrypted = bytearray()
    for val in new:
        c = ord(val) + ord(next(decr)) - ord(next(encr))
        if c < 65:
            c += 26
        elif c > 90:
            c -= 26
        decrypted.append(c)
    return decrypted.decode()






print(decode_vigenere('HELLO', 'OIWWC', 'ICP'))# == "BYE"

         ANDNOWFORSOMETHINGCOMPLETELYDIFFERENT
result: "IMALUMBERJACKANDIMOKISLEEPALLNIGHTANDRRCYJCUGRHXKLPHKNYWOFLDURNYPOCWYXBLRRPRFKUZTAZYTHMUYLMZANMYJAYCJTXZQNIYDWSLXCVQGFTBIXMSHICXJADVIBY"
Right result: "IMALUMBERJACKANDIMOKISLEEPALLNIGHTANDIWORKALLDAYICUTDOWNTREESISKIPANDJUMPILIKETOPRESSWILDFLOWERSIPUTONWOMENSCLOTHINGANDHANGAROUNDINBARS"
decode_vigenere(u"ANDNOWFORSOMETHINGCOMPLETELYDIFFERENT",
                u"PLWUCJUMKZCZTRAPBTRMFWZRICEFRVUDXYSAI",
                u"XKTSIZQCKQOPZYGKWZDIBZZRTNTSZAXEAAOASGPVFXPJEKOLXANARBLLMYSRHGLRWCPLWQIZEGEPYRIMIYSFHUBSRSAMPLFFXNNACALMFLBFRJHAVVCETURUPLZHFBJLWPBOPPL")



