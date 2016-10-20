from tqdm import tqdm
import time
import threading
import os

class MyThread(threading.Thread):
    """
    Thread checking URLs.
    """

    def __init__(self, row):
        """
        Constructor.

        @param urls list of urls to check
        @param output file to write urls output
        """
        threading.Thread.__init__(self)
        self.row = row
        self.cls()
        
    def progress(self):
        escape = "\033["+str(self.row)+";"+str(self.row)+"3H"
        print(escape)

        with tqdm(total=100) as pbar:
            for i in range(100):
                pbar.update(1)
                time.sleep(.02)
                

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        return ''

    
    def run(self):
        """
        Thread run method. Check URLs one by one.
        """
        
        self.progress()


if __name__=="__main__":
    threads = []
    row = 10
    for i in range(10):
        threads.append(MyThread(row))
        row += 2
        
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()