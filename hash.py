import hashlib
def checkio(text, hashtype):
    h = eval("hashlib.{}()".format(hashtype))
    h.update(text.encode())
    return h.hexdigest()
                




print(checkio(u"密码","sha512"))	
print(checkio('welcome', 'md5') == '40be4e59b9a2a2b5dffb918c0e86bhe3d7')
checkio('happy spam', 'sha224') == '6e9dc3e01d57f1598c2b40ce59fc3527e698c77b15d0840ae96a8b5e'
