# result = 5 + 6
# print(result)
#
#
# num = 10
# print(result * num)
#
# user_input = input("Insert your input: ")
# print(user_input)
#
# print(type(num))
# num1 = result / num
# print(num1)
# print(type(num1))
# print(type(user_input))

# year = input("Insert your birth year: ")
# year_as_int = int(year)
# age = 2022 - year_as_int
# print("You are", age, "years old")
# my_text = f"You are {age} years old"
# my_text = "You are {age} years old"

# print(f"You are {2022 - int(input('Insert a year: '))} years old")

# word = "Sun"
# word1 = 'Sun'
# word2 = "She said: \"The weather is great\""
# word3 = 'She said: "The weather is great"'
# word4 = "Hello\nworld"
# word5 = "Hello\tworld"
# word6 = """My name is Valeria
# I'm 35 years old
# I live in Netanya
# """
# print(word6)
#

# + - /*
# // %
# total_minutes = int(input("Insert minutes: "))
# # hh:mm
# print(f"{total_minutes//60}:{total_minutes%60}")

# my_bool = True
# my_bool2 = False
#
# result1 = 4 < 5
# print(result1)

# <= >= < >

# ==

# salary = int(input("Insert salary: "))
# is_10000 = salary == 10_000
# print(is_10000)
#
# milion = 1_000_000

# salary = int(input("Insert salary: "))
# is_not_10000 = salary != 10_000
# print(is_not_10000)


# print(True and True)
# print(False or False)
# my_bool = True
# print(not my_bool)

# salary = int(input("Insert salary: "))
# if salary >= 1_000_000:
#     print("You are a millionaire")
# else:
#     print("Not a milionaire")
#
# print("bye")


# print("Welcome! We will help you to fix your issue with lamp")
# is_plugged = input("Is lamp plugged in? (y/n)")
# if is_plugged == 'y':
#     is_burned = input("Is lamp burned? (y/n)")
#     if is_burned == 'y':
#         print("Replace lamp")
#     else:
#         print("Repair lamp")
# else:
#     print("Plug in lamp")


# num = int(input("Insert num: "))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

# beer, wine
# 0.3 or less beer
# wine: 0.2 or less

# drink = input("Insert drink: ")
# amnt = float(input("Insert amount in liters"))
# if (drink == 'beer' and amnt <= 0.3) or \
#     (drink == 'wine' and amnt <= 0.2):
#     print("You can drive")
# else:
#     print("You cannot drive")

weather = input("Insert weather (sun/rain/cloudy)")
if weather == 'sun':
    print("Take sunglasses")
elif weather == "rain":
    print("Take umbrella")
elif weather == 'snow':
    print("Take coat")
else:
    print("Take nothing")

print("Bye")