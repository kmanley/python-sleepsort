import threading
import Queue
import time

def sleepsort(unsorted):  
    q = Queue.Queue()
    def threadfunc(x):
        time.sleep(x)
        q.put(x)
    threads = [threading.Thread(target=threadfunc, args=(item,)) for item in unsorted]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return [q.get() for i in range(q.qsize())]

if __name__ == "__main__":
    import random
    N = 10
    unsorted = [random.randrange(10) for i in range(N)]
    print "unsorted: %r" % unsorted
    print "sorted:   %r" % sleepsort(unsorted)
