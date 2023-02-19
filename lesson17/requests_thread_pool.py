import math
import time
from concurrent.futures import ThreadPoolExecutor, Future, as_completed
from threading import Event

import requests

def perform_a_lot_of_calc(num, event: Event):
    for i in range(1_000_000_000):
        if event.is_set():
            break
        num += 1
    return num

# r = True
# perform_a_lot_of_calc(5, r)
def get_quote(num):
    # if num == 99:
    #     raise Exception(" error 99")
    # print(f"Worker started - Getting quote {num}")
    response = requests.get("https://api.kanye.rest")
    if response.status_code < 400:
        # print(f"worker {num} finished working")
        return {'id': num, 'quote': response.json()['quote']}
    else:
        raise Exception(f"Received response code {response.status_code} for quote {num}")

def callback_fn(future):
    try:
        print(future.result())
    except Exception as e:
        print("error in future", e)

if __name__ == '__main__':
    s = time.time()
    with ThreadPoolExecutor(10) as executor:

        # futures = []
        for i in range(100):
            future = executor.submit(get_quote, i)  # non-blocking
            future.add_done_callback(callback_fn)
            # futures.append(future)

            # print(future.result())

        print("All tasks submitted")

        cancel_wrap = [False]
        event = Event()
        long_future = executor.submit(perform_a_lot_of_calc, 10, event)
        # signal cancel
        event.set()
        # cancel_wrap[0] = True


        # future.cancel()


        # time.sleep(0.3)

        # try:
        #     result = futures[-1].result(timeout=0.4)  # blocking
        # except TimeoutError as e:
        #     print("timeout")

        # print(futures[-1].result()) #blocking
        #
        # print("first future done:", futures[0].done()) # non-blocking
        # print("last future done:", futures[-1].done()) # non-blocking



        # for future in as_completed(futures):  # blocking
        #     result = future.result()
        #     print(result)

    # results = []
    # for f in futures:
    #     results.append(f.result())
    # print(results)

    print("All tasks completed")
    e = time.time()
    print(e-s)

