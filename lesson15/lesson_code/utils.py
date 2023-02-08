import math
import time


def performance_log():
    pass

def greeting(orig_func):

    def wrapping_function(*args, **kwargs):
        print("Hi")
        ret_val = orig_func(*args, **kwargs)
        print("Bye")
        return ret_val

    return wrapping_function

@greeting
def factorial():
    num = int(input("Please insert a number: "))
    fact = math.factorial(num)
    print(f"The factorial of {num} is {fact}")

# factorial = greeting(factorial)

@performance_log
def capitalize():
    txt = input("Please insert a text to capitalize: ")
    print(f"Your capitalized text is: {txt.capitalize()}")

# capitalize = my_dec(capitalize)

def convert_from_farenheit():
    temp_F = float(input("Please insert a temperature in °F: "))
    temp_C = (temp_F - 32) * (5/9)
    print(f"{temp_F} in °F is {temp_C} °C")


@greeting
def convert_from_celcius():
    temp_C = float(input("Please insert a temperature in °C: "))
    temp_F = (temp_C * (9/5)) + 32
    print(f"{temp_C} in °C is {temp_F} °F")


@greeting
def convert_from_str(s: str):
    return int(s)

# convert_from_str = greeting(convert_from_str)

if __name__ == '__main__':
    # factorial()
    # convert_from_celcius()
    # greeting_decorator(convert_from_farenheit)()
    # capitalize()
    num = convert_from_str('4')
    print(num)