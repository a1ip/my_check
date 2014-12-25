from time import sleep
from threading import Thread
def vypis():
    for c in "Text k vypsaní.":
        print(c)
        sleep(1)


Thread(target=vypis).start()

print("Hlavní vlákno.")
sleep(2)
print("Tady můžeš pokračovat dál...")
sleep(1)
print("A tak dále...")
      
