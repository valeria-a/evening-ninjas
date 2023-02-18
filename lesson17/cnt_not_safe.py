# run in colab

from concurrent.futures import ThreadPoolExecutor

counter = 0

def count():
    global counter
    for _ in range(1_000_000):
        counter = counter + 1


if __name__ == '__main__':

    with ThreadPoolExecutor(max_workers=20) as executor:
        for i in range(100):
            executor.submit(count)
    print(counter)