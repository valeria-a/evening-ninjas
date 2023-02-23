# run in colab
# https://colab.research.google.com/drive/1JkyWWdNm02HpW4qR5NDJYguT79kDvshV?usp=sharing

from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Lock

lock = Lock()
counter = 0

def count():
    global counter
    for _ in range(1_000_000):
        lock.acquire()
        counter = counter + 1
        lock.release()


if __name__ == '__main__':

    with ThreadPoolExecutor(max_workers=20) as executor:
        for i in range(100):
            executor.submit(count)
    print(counter)