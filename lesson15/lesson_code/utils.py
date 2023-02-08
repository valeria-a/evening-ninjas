import math
import time


def greeting(orig_func):

    def wrapping_function(*args, **kwargs):
        print("Hi")
        ret_val = orig_func(*args, **kwargs)
        print("Bye")
        return ret_val

    return wrapping_function


def performance_log(ms=False):
    def f1(orig_func):
        def f2(*args, **kwargs):
            start = time.time()
            ret_val = orig_func(*args, **kwargs)
            end = time.time()
            res = end - start
            if ms:
                res *= 1000
            print(f"Function {orig_func.__name__} took {res} seconds")
            return ret_val

        return f2

    return f1

# def performance_log(orig_func):
#
#     def wrapping_function(*args, **kwargs):
#         start = time.time()
#         ret_val = orig_func(*args, **kwargs)
#         end = time.time()
#         print(f"Function {orig_func.__name__} took {end-start} seconds")
#         return ret_val
#
#     return wrapping_function

@greeting
def factorial():
    num = int(input("Please insert a number: "))
    fact = math.factorial(num)
    print(f"The factorial of {num} is {fact}")

# factorial = greeting(factorial)


def capitalize():
    txt = input("Please insert a text to capitalize: ")
    print(f"Your capitalized text is: {txt.capitalize()}")

# capitalize = my_dec(capitalize)

@performance_log(ms=True)
def convert_from_farenheit():
    temp_F = float(input("Please insert a temperature in °F: "))
    temp_C = (temp_F - 32) * (5/9)
    print(f"{temp_F} in °F is {temp_C} °C")

# convert_from_farenheit = performance_log(ms=True)(convert_from_farenheit)




@greeting
def convert_from_celcius():
    temp_C = float(input("Please insert a temperature in °C: "))
    temp_F = (temp_C * (9/5)) + 32
    print(f"{temp_C} in °C is {temp_F} °F")


@performance_log(ms=True)
def convert_from_str(s: str):
    return int(s)

# convert_from_str = greeting(convert_from_str)

if __name__ == '__main__':
    # factorial()
    # convert_from_celcius()
    # greeting_decorator(convert_from_farenheit)()
    # capitalize()
    # num = convert_from_str('4')
    # print(num)
    # convert_from_farenheit()
    print(convert_from_str('554757567567'))