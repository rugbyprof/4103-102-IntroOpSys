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

class Producer(threading.Thread):
    """
    Produces random integers to a list
    """

    def __init__(self, buffer, location, condition):
        """
        @param integers list of integers
        @param condition condition synchronization object
        """
        threading.Thread.__init__(self)
        self.buffer = buffer
        self.condition = condition
        self.pbar = Progress(location)

    def run(self):
        """
        Thread run method. Append random integers to the integers list
        at random time.
        """
        self.pbar.start()
        for i in range(100):
            with self.condition:
                for j in range(random.randint(3,5)):
                    resource = random.randint(0, 256)

                    self.buffer.append(resource) 
                    self.pbar.update(len(self.buffer))
                    if len(self.buffer) > 80:
                        self.pbar.update(int(len(self.buffer)/2))
                self.condition.notifyAll()
                time.sleep(1)
        self.pbar.finish()


class Consumer(threading.Thread):
    """
    Consumes random integers from a list
    """

    def __init__(self, buffer, location, condition):
        """
        Constructor.

        @param integers list of integers
        @param condition condition synchronization object
        """
        threading.Thread.__init__(self)
        self.buffer = buffer
        self.condition = condition
        self.pbar = Progress(location)
        
    def run(self):
        """
        Thread run method. Consumes integers from list
        """
        self.pbar.start()
        i = 1
        while len(self.buffer) > 0:
            with self.condition:
                for j in range(random.randint(2,5)):
                    if self.buffer:
                        self.pbar.update(i)
                        i += 1
                        resource = self.buffer.pop()


                self.condition.wait()

        self.pbar.finish()

def main():
    with term.fullscreen():
        buffer = []
        f = open('condition_output.txt', 'w+')
        condition = threading.Condition()
        threads = []
        y = 5
        threads.append(Producer(buffer, (0,y),condition))
    
        for i in range(20):
            threads.append(Consumer(buffer,(0,y),condition))
            y += 1

        for t in threads:
            t.start()
            
        for t in threads:
            t.join()

if __name__ == '__main__':
    main()


