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
            
def bar(location):
    # fd is an object that has a .write() method
    pbar = Progress(location)
    # progressbar usage
    pbar.start()
    for i in range(100):
        # do stuff
        t_wait = random.random() / 50
        time.sleep(t_wait)
        # update calls the write method
        pbar.update(i)

    pbar.finish()
    
with term.fullscreen():
    bar((0,10))