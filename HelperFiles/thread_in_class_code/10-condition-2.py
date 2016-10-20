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

    def __init__(self, location,condition):
        # Call parent constructor (thread)
        threading.Thread.__init__(self)
        
        self.location = location
        self.pbar = Progress(location)
        self.condition = condition
    
        
    def run(self):
        """
        Thread run method. Check URLs one by one.
        """
        self.pbar.start()
        with self.condition:
        
            if not self.name == 'Thread-1':
                self.condition.wait()
                
            for i in range(100):
                self.pbar.update(i)
                time.sleep(random.random()/4)
                if self.name == 'Thread-1' and i % 20 == 0:
                    self.condition.notifyAll()
                    break

            self.pbar.finish()
        
if __name__=="__main__":
    with term.fullscreen():
            condition = threading.Condition()
            
            threads = []
            x = 0
            y = 10

            mainThread = MyThread((x,y),condition)
            y+=1

            for i in range(10):
                threads.append(MyThread((x,y),condition))
                y += 1
        
            mainThread.start()
            mainThread.join()
            
            for t in threads:
                t.start()

    
            for t in threads:
                t.join()
                

            
                
                
                
