import weakref
import gc

class Reference():
    _count = 0

    def __init__(self):
        print("Začátek objektu.")
        Reference._count += 1
        self.number = Reference._count

    def __del__(self):
        print("Konec objektu %s" % self.number)
        if Reference: Reference._count -= 1

    def __repr__(self):
        return "Ref: {}".format(self.number)


    @staticmethod
    def get_count():
        return Reference._count


if __name__ == "__main__":
    #gc.disable() # kvuli pythonu < 3.4
    r1 = Reference()
    r2 = Reference()
    r3 = Reference()
    r1.next = r2
    r2.next = r3
    r3.next = r1
    w1 = weakref.ref(r1)
    del(r1)
    del(r2)
    del(r3)
    print("prave jsem odstranil reference")
    #r4 = Reference()
    #r5 = Reference()
    print(w1)
    print(w1().next)
