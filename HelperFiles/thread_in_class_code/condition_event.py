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

    def __init__(self, integers, condition,event):
        """
        Constructor.

        @param integers list of integers
        @param condition condition synchronization object
        """
        threading.Thread.__init__(self)
        self.integers = integers
        self.condition = condition
        self.event = event

    def run(self):
        """
        Thread run method. Append random integers to the integers list
        at random time.
        """
        count = 5
        while True:
            integer = random.randint(0, 256)
            self.condition.acquire()
            print 'condition acquired by %s' % self.name
            self.integers.append(integer) 
            print '%d appended to list by %s' % (integer, self.name)
            print 'condition notified by %s' % self.name
            self.condition.notify()
            print 'condition released by %s' % self.name
            self.condition.release()
            time.sleep(1)
            count -= 1
            if count == 0:
               break
        self.condition.notifyAll()
        self.event.set()


class Consumer(threading.Thread):
    """
    Consumes random integers from a list
    """

    def __init__(self, integers, condition,event):
        """
        Constructor.

        @param integers list of integers
        @param condition condition synchronization object
        """
        threading.Thread.__init__(self)
        self.integers = integers
        self.condition = condition
        self.event = event

    def run(self):
        """
        Thread run method. Consumes integers from list
        """
        
        while True:
            self.condition.acquire()
            print 'condition acquired by %s' % self.name
            while True:
                if self.integers:
                    integer = self.integers.pop()
                    print '%d popped from list by %s' % (integer, self.name)
                    break
                print 'condition wait by %s' % self.name
                self.condition.wait()
                if self.event.isSet():
                    print("well well event")
                    self.event.clear()
                    return
            print 'condition released by %s' % self.name
            self.condition.release()

def main():
    integers = []
    f = open('condition_output.txt', 'w+')
    condition = threading.Condition()
    event = threading.Event()
    t1 = Producer(integers, condition,event)
    t2 = Consumer(integers, condition,event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
