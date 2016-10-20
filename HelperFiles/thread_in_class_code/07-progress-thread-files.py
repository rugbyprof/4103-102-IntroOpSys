import threading
import urllib3

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

class FetchUrls(threading.Thread):
    """
    Thread checking URLs.
    """

    def __init__(self, urls, output,location):
        """
        Constructor.

        @param urls list of urls to check
        @param output file to write urls output
        """
        threading.Thread.__init__(self)
        self.urls = urls
        self.output = output
        self.pbar = Progress(location)
    
    def run(self):
        """
        Thread run method. Check URLs one by one.
        """
        http = urllib3.PoolManager()
        while self.urls:
            url = self.urls.pop()
            try:
                r = http.request('GET',url,preload_content=False)

            except e:
                print 'URL %s failed: %s' % (url,e.reason)
                
            fileSize = int(r.headers['Content-Length'])
            
            self.pbar.start()
            i = 0
            for chunk in r.stream(32):
                i += 32
                self.output.write(chunk)
                p = int(float(i) / float(fileSize) * 100)

                self.pbar.update(p)
            self.pbar.finish()

# What happens if we don't close the file?  
# What happens if we don't join?  

def main():
    with term.fullscreen():
        y = 5
        num_threads = 25
        threads = []
        f = open('output_progress.txt', 'w+')
        for i in range(num_threads):
            threads.append(FetchUrls(['http://terrywgriffin.com/thread_data/'+chr(i+65)+'.txt'], f,(0,y)))
            y += 1
        for t in threads:
            t.start()
        

        for t in threads:
            t.join()

        f.close()

if __name__ == '__main__':
    main()
