import time
from threading import Thread

def myfunc(i):
    print("sleeping 5 sec from thread %d \n" % i)
    time.sleep(5)
    print("finished sleeping from thread %d \n" % i)

threads = list()
for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()
    threads.append(t)

while(any(t.is_alive() for t in threads)):
      pass

print("Konec")
