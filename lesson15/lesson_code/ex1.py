def foo():
    print("hi")

def my_func(func):
    func()


def create_quote():
    print("Creating a function that will print a quote...")

    # defining a new function inside a function
    def display_quote():
        print("\n*********************************************\n"
              "Quote by John Quincy Adams, 6th U.S. President:\n"
              "Try and fail, but don't fail to try\n"
              "*********************************************\n")

    return display_quote

if __name__ == '__main__':
    ret_val = create_quote()
    print(type(ret_val))
    ret_val()
    # display_quote()
