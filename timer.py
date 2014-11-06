from threading import Thread
from time import sleep



class Timer():
    _thread = None

    def __init__(self):
        self._enabled = False

    @property
    def enabled(self):
        return self._enabled

    def on_tick(self):
        pass

    def start(self):
        self._thread = Thread(target=self._run())
        self._thread.start()

    def _run(self, secs = 10):
        sleep(secs)
        self.on_tick()



def on_tick():
    print("5 vteřin!")


t = Timer()
t.on_tick =  on_tick

t.start()

s =  input()
print(s)
        
        
    
