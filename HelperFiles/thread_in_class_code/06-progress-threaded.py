import threading
import random
import time

from blessings import Terminal
from progressbar import ProgressBar

term = Terminal()
"""
Create an object with a write method that writes to a
specific place on the screen, defined at instantiation.
"""
class Writer(object):
    """
    Input: location - tuple of ints (x, y), the position of the bar in the terminal
    """
    def __init__(self, location):
        self.location = location

    def write(self, string):
        with term.location(*self.location):
            print(string)
            
class Progress(object):
    def __init__(self,location):
        self.writer = Writer(location)
        self.p = ProgressBar(fd=self.writer)
    def start(self):
        self.p.start()
    def update(self,p):
        self.p.update(p)
    def finish(self):
        self.p.finish()

class MyThread(threading.Thread):

    def __init__(self, location,lock):
        # Call parent constructor (thread)
        threading.Thread.__init__(self)
        
        self.location = location
        self.pbar = Progress(location)
        self.lock = lock
        
        
    
    def run(self):
        """
        Thread run method. Check URLs one by one.
        """
        self.pbar.start()
        with self.lock:
            for i in range(100):
                self.pbar.update(i)
                time.sleep(random.random())
            
        self.pbar.finish()
        
        


if __name__=="__main__":
    lock = threading.Lock()
    with term.fullscreen():
            threads = []
            x = 0
            y = 10
            for i in range(10):
                threads.append(MyThread((x,y),lock))
                y += 1
        
            for t in threads:
                t.start()
    
            for t in threads:
                t.join()
