import threading
import urllib3

class FetchUrls(threading.Thread):
    """
    Thread checking URLs.
    """

    def __init__(self, urls, output):
        """
        Constructor.

        @param urls list of urls to check
        @param output file to write urls output
        """
        threading.Thread.__init__(self)
        self.urls = urls
        self.output = output
    
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
                
            string = 'Thread %s writing\n' % self.name
            self.output.write(string)
            for chunk in r.stream(32):
                self.output.write(chunk)
            
            print 'write done by %s' % self.name
            print 'URL %s fetched by %s' % (url, self.name)

def main():
    urls1 = ['http://terrywgriffin.com/thread_data/A.txt']
    urls2 = ['http://terrywgriffin.com/thread_data/B.txt']
    urls3 = ['http://terrywgriffin.com/thread_data/C.txt']
    urls4 = ['http://terrywgriffin.com/thread_data/D.txt']
    f = open('01-output.txt', 'w+')
    t1 = FetchUrls(urls1, f)
    t2 = FetchUrls(urls2, f)
    t3 = FetchUrls(urls3, f)
    t4 = FetchUrls(urls4, f)
    t2.start()
    t3.start()
    t4.start()
    t1.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    f.close()

if __name__ == '__main__':
    main()
