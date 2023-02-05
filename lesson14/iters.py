# print(16 in range(10, 1000, 3))

class MyRange:

    def __init__(self, end):
        self._end = end
        self._iter_counter = 1

    def __iter__(self):
        self._iter_counter = 1
        return self

    def __next__(self):
        curr_val = self._iter_counter
        if curr_val > self._end:
            raise StopIteration()
        self._iter_counter += 1
        return curr_val


if __name__ == '__main__':

    my_range = MyRange(10)
    for i in my_range:
        print(i)
    for i in my_range:
        print(i)

