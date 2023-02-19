import time
from threading import Thread

import requests

def get_quote(num):
    # time.sleep(5)
    print(f"Worker started - Getting quote {num}")
    response = requests.get("https://api.kanye.rest")
    if response.status_code < 400:
        print(f"worker {num} finished working")
        return {'id': num, 'quote': response.json()['quote']}
    else:
        raise Exception(f"Received response code {response.status_code} for quote {num}")


if __name__ == '__main__':
    thread1 = Thread(target=get_quote, args=(1, ))
    thread1.start()

    thread2 = Thread(target=get_quote, args=(2, ))
    thread2.start() # non-blocking

    print("before join1")
    thread1.join() # blocking
    print("after join1, before join2")
    thread2.join()
    print("after join2")


