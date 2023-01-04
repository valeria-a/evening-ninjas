def fact_number(num: int, calc_sqr=False) -> int | tuple[int, int]:
    print("val of calc_sqr", calc_sqr)
    ret_val = 1
    for i in range(1, num+1):
        ret_val *= i

    if calc_sqr:
        return ret_val, num ** 2

    return ret_val


# print(fact_number(5))
# ret_val = fact_number(5, calc_sqr=True)
# print(ret_val)
#
# fact_number(5, True)
# fact_number(num=5, calc_sqr=True)
# fact_number(calc_sqr=True, num=5)
# fact_number(calc_sqr=True, 5) # incorrect

# def foo(a, b, num1=0, num2=1):
#     print(a, b, num1, num2)
#
# foo("fff", "fgfg", num2=4, num1=8)
# # foo("fff", "fgfg", 4, num1=8)
# foo("ttt", "yyy")


# def bar(num1, *args):
#     print("num1:", num1)
#     print("args", args)
#
# bar(1, 2, 3, "a", "b", "y")
# bar("hello")

def bar(num1, *args):
    print("num1:", num1)
    print("args", args)
    print("args len:", len(args))

my_num = 6
my_tuple = (4,5,6,78,0)
bar(my_num, my_tuple)
bar(my_num, *my_tuple)
