def fibonacci_endless(limit):
    a, b = 0, 1
    yield a

    while a < limit:
        a, b = b, a + b
        yield a


if __name__ == '__main__':
    for elem in fibonacci_endless(100):
        if elem % 2 == 0:
            print(elem)

