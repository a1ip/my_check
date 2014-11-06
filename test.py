
def nic(obj):
    obj(test)
    class Nic():
        pass
    return Nic

@nic
class Test():
    def __init__(self, test):
        pass
        

t = Test()
print(t)
