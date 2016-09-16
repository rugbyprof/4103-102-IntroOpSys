## Threading Assignment

You won't really have to write any code, but you will have to install some libraries and such on your droplet. So start early and hit me up with issues you run into. 

Install the following:

- `pip install urllib3` (maybe urllib2)
- `pip install imgurpython`
- `pip install pyopenssl ndg-httpsclient pyasn1` (this fixes some errors doing the https call)
- If the obove pip command chokes, try installing this first: `apt-get install libffi-dev libssl-dev`

Create a file called `getimgur.py` in a new directory called `/opt/4130repo/assignments/homework-02`. Just paste the code from below into the file and make it all run! I'll post more about what I want you to turn in. And READ the threading overview!

```python
from imgurpython import ImgurClient
import os
from queue import Queue
from threading import Thread
from time import time
import urllib3


"""
@Class: Imgur
@Usage: 
      imgur = ImgUr(download_directory_name)
"""
class ImgUr(object):
    """
    @Params: {string} - Download Directory
    @Returns: None
    """
    def __init__(self,dd=None):
        client_id = '50049400837.73078400742'
        client_secret = '5a730c87aeea8c2daad196ef3ff2c6da'
        
        if not dd:
            self.download_dir = 'downloads'
        else:
            self.download_dir = dd
            
        self.setup_download_dir(self.download_dir)

        self.data = []
        self.client = ImgurClient(client_id, client_secret)
        
        self.http = urllib3.PoolManager()
        
    """
    @Params: {int} - Minimum number of images to download
    @Description:
        This method uses the ImgurClient to download pages of images from imgur and
        places them into a list.
    @Returns: {list} - List of urls to images 
    """
    def get_links(self,min=10):
        page=0
        while len(self.data) <= min:
            items = self.client.gallery(page=page, window='day', show_viral=True)
            for item in items:
                name, ext = os.path.splitext(item.link)
                if ext=='.jpg' or ext=='.png':
                    self.data.append(item.link)
            page += 1
        return self.data
        
    """
    @Params: {string} - Url of image to download
    @Description:
        This method receives a url and downloads it using the urllib3 library. Saves it to 
        a directory determined by the class constructor.
    @Returns: None
    """             
    def download_link(self,link):
        path = self.download_dir+"/"+os.path.basename(link)
        r = self.http.request('GET', link, preload_content=False)

        with open(path, 'wb') as out:
            while True:
                data = r.read()
                if not data:
                    break
                out.write(data)
        r.release_conn()
        
    """
    @Params: {string} - Download directory name
    @Description:
        This will check to see if the param is a directory and if not
        it will create it.
    @Returns: None
    """
    def setup_download_dir(self,d):
        self.download_dir = d
        if not os.path.isdir(self.download_dir):
            os.makedirs(self.download_dir)

"""
@Class: DownloadWorker
@Extends: {Thread}
@Description:
    This class manages a "queue" of thread workers and uses the imgur client to
    download images concurrently.
@Returns: None
"""
class DownloadWorker(Thread):
   def __init__(self, queue,imgur):
       Thread.__init__(self)
       self.queue = queue
       self.imgur = imgur

   def run(self):
       while self.queue.qsize():
           # Get the work from the queue and expand the tuple
           link = self.queue.get()
           self.imgur.download_link(link)
           self.queue.task_done()


"""
@Function: singleProcess
@Description:
    This function uses the single threaded implementation to download "x" images from imgur
@Params:
    x {int}: Number of images to download
@Usage:   singleprocess()   # just call it!
@Returns: None
"""
def singleProcess(x=50):
   print('Running single thread...')
   ts = time()
   imgur = ImgUr('single')
   
   links = imgur.get_links(x)
   for link in links:
       imgur.download_link(link)
   print('Took {}s'.format(time() - ts))

"""
@Function: threaded
@Description:
    This function uses a threaded implementation to download "x" images from imgur
@Params:
    x {int}: Number of images to download
@Usage:   threaded()   # just call it!
@Returns: None
"""
def threaded(x):
   print('Running multi threaded...')
   ts = time()
   imgur = ImgUr('threaded')

   links = imgur.get_links(x)
   
   # Create a queue to communicate with the worker threads
   queue = Queue()
   # Create 8 worker threads
   for x in range(4):
       worker = DownloadWorker(queue,imgur)
       # Setting daemon to True will let the main thread exit even though the workers are blocking
       worker.daemon = True
       worker.start()
   # Put the tasks into the queue as a tuple
   for link in links:
       queue.put((link))
   # Causes the main thread to wait for the queue to finish processing all the tasks
   queue.join()
   print('Took {}'.format(time() - ts))
   
if __name__ == '__main__':
    singleProcess(50)
    threaded(50)
   ```
   
