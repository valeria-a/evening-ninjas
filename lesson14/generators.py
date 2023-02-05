def my_gen():
    num = 1
    print("Before first yield")
    yield num

    num = 2
    print("Before second yield")
    yield num

    num = 3
    print("Before third yield")
    yield num


if __name__ == '__main__':
    g = my_gen()
    print(g)
    for n in g:
        print("new iteration")
        print(n)
