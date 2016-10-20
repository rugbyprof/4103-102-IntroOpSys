## 01-thread.py

This is a simple threading example in which 4 threads open 4 files and try to write to the 
same shared resource (a file). It gets nice and jacked up as they all write their intermixed
32 byte chunks all over each other.

## 02-thread-lock.py

This extends the previous example by adding a "nice" lock to the shared resource (the file). I say
nice because no thread tries to unlock another threads ... lock (because they can). My example my
be a little over the top, but it explains how ownership works between locks and threads.

## 03-thread-lock.py

The shows how threads can unlock a locked lock :) Say that real fast (sounds like klingon). We end
up with output like the first example.

## 04-thread-rlock.py

This would attempt to unlock a locked lock, but rlock doesn't even have a 'locked()' method to
check. There is a way to check: `if self.lock._RLock__owner is threading.current_thread()` this 
simply tells you if you own it. The way I have the code written, it will pass this if ONE time
then unlock and lock in and endless loop after the first context switch.

## 05-thread-progress.py

Shows a progress bar example reading 10 files from a server and showing the download progress of each file.

## semaphore.py (based on thread_progress.py)

Downloads as many files concurrently as the "semaphore" allows. 
