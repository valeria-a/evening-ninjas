import multiprocessing
from concurrent.futures import ProcessPoolExecutor, as_completed

import time

COUNT = 300_000_000


def countdown(n_from, n_to):
    while n_from > n_to:
        n_from -= 1


if __name__ == '__main__':
    start = time.time()

    with ProcessPoolExecutor() as executor:
        future1 = executor.submit(countdown, COUNT//4, 0)
        future2 = executor.submit(countdown, COUNT//4, 0)
        future3 = executor.submit(countdown, COUNT//4, 0)
        future4 = executor.submit(countdown, COUNT//4, 0)
        start = time.time()


    end = time.time()

    print('Time taken in seconds -', end - start)