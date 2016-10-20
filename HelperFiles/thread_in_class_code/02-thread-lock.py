import threading
import urllib3

class FetchUrls(threading.Thread):
    """
    Thread checking URLs.
    """

    def __init__(self, urls, output,lock):
        """
        Constructor.

        @param urls list of urls to check
        @param output file to write urls output
        """
        threading.Thread.__init__(self)
        self.urls = urls
        self.output = output
        
        self.lock = lock
    
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
            
            self.lock.acquire()
            string = 'Acquired by %s\n' % self.name
            self.output.write(string)
            for chunk in r.stream(32):
                self.output.write(chunk)
            
            print 'write done by %s' % self.name
            print 'URL %s fetched by %s' % (url, self.name)
            string = 'Released by %s\n' % self.name
            self.output.write(string)
            self.lock.release()


def main():
    urls1 = ['http://terrywgriffin.com/thread_data/A.txt']
    urls2 = ['http://terrywgriffin.com/thread_data/B.txt']
    urls3 = ['http://terrywgriffin.com/thread_data/C.txt']
    urls4 = ['http://terrywgriffin.com/thread_data/D.txt']
    f = open('02-output.txt', 'w+')
    
    lock = threading.Lock()
    
    threads = []

    for i in range(20):
        threads.append(FetchUrls(urls1, f, lock))

    for t in threads:
        t.start()

#    for t in threads:
#        t.join()

    f.close()

if __name__ == '__main__':
    main()
