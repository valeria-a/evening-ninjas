# print("the beginning of utils")
# from lesson7.utils.text_utils import get_last_char

print("inside utils", __name__)

MONTHS_IN_YEAR = 12

def get_lsd(num: int) -> int:
    return num % 10

def get_msd(num: int) -> int:
    return int(str(num)[0])

def floor():
    # get_last_char("hello")
    print("floor")


if __name__ == '__main__':
    print("hello world")
    floor()