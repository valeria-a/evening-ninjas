def calc_square(num: int) -> int:
    return num ** 2


def convert_and_run(f: callable, number_as_str: str):
    new_num = int(number_as_str)
    return f(new_num)


if __name__ == '__main__':
    print(calc_square(7))
    print(calc_square)

    my_func = calc_square
    print(my_func)
    print(my_func(7))

    ret_val = convert_and_run(calc_square, '23')
    print(ret_val)
