import threading
import random
import time

from blessings import Terminal
from progressbar import ProgressBar

term = Terminal()

class Writer(object):
    """Create an object with a write method that writes to a
    specific place on the screen, defined at instantiation.

    This is the glue between blessings and progressbar.
    """
    def __init__(self, location):
        """
        Input: location - tuple of ints (x, y), the position
                          of the bar in the terminal
        """
        self.location = location

    def write(self, string):
        with term.location(*self.location):
            print(string)

class Producer(threading.Thread):
    """
    Produces random integers to a list
    """

    def __init__(self, integers, event):
        """
        Constructor.

        @param integers list of integers
        @param event event synchronization object
        """
        threading.Thread.__init__(self)
        self.integers = integers
        self.event = event

    def run(self):
        """
        Thread run method. Append random integers to the integers list
        at random time.
        """
        while True:
            integer = random.randint(0, 256)
            self.integers.append(integer) 
            print '%d appended to list by %s' % (integer, self.name)
            print 'event set by %s' % self.name
            self.event.set()
            self.event.clear()
            print 'event cleared by %s' % self.name
            time.sleep(1)

class Consumer(threading.Thread):
    """
    Consumes random integers from a list
    """

    def __init__(self, integers, event):
        """
        Constructor.

        @param integers list of integers
        @param event event synchronization object
        """
        threading.Thread.__init__(self)
        self.integers = integers
        self.event = event

    def run(self):
        """
        Thread run method. Consumes integers from list
        """
        while True:
            self.event.wait()
            try:
                integer = self.integers.pop()
                print '%d popped from list by %s' % (integer, self.name)
            except IndexError:
                # catch pop on empty list
                time.sleep(1)

def main():
    integers = []
    f = open('condition_output.txt', 'w+')
    event = threading.Event()
    t1 = Producer(integers, event)
    t2 = Consumer(integers, event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
