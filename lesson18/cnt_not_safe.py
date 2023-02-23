# run in colab
import math
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
from threading import Lock


q = Queue()
counter = 0
lock =Lock()

def count():
    global counter
    for _ in range(1_000_000):
        # lock.acquire() #th1
        # counter = counter + 1
        # lock.release()
        with lock:
            counter = counter + 1


# counter = 12
# th1 12 + 1 (13)
# th2 12 + 1 = 13 => counter
# th1 13 => counter

# l = [1,2,3,45]
# th1 -> read print(l)
# th2 -> l.append("er") | add elem, count+=1



if __name__ == '__main__':

    with ThreadPoolExecutor(max_workers=20) as executor:
        for i in range(100):
            executor.submit(count)
    print(counter)


