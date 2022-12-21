# i=0
# while i < 10:
#     print("********")
#     i += 1
#
grades = [99, 98, 97, 80, 100, 75, 93]


# i = 0
# while i < len(grades):
#     print(grades[i])
#     i += 1



# for iterating list
# for xxx in grades:
#     print(xxx)

# for i, grade in enumerate(grades):
#     print(f"Grade number {i+1} is: {grade}")

# i = 0
# while i < len(grades):
#     print(f"Grade number {i+1} is: {grades[i]}")

# for c in "Hello":
#     print(c)

# for i, c in enumerate("Hello"):
#     print(i, c)

# for i in range(10):
#     print(f"{i}^2 = {i**2}")

# r = range(10)
# r = range(100, 1_000_000)
# print(type(r))
# print(1000 in r)
# r = range(10, 20, 2)
# for i in range(0, 101, 2):
#     print(i)
#
# r = range(0, 101, 2)
# print(5 in r)
#
# for i in range(100, -1, -2):
#     print(i)

# import string
# string.ascii_lowercase


# grades = [99, 98, 97, 80, 100, 75, 93]
# names = ['Herut', 'Lior', 'Chen', 'Gal']
# grades = []
# for name in names:
#     grade = int(input(f"Insert a grade for {name}"))
#     grades.append(grade)
# for i, name in enumerate(names):
#     print(f"Record number {i}: The grade of {name} is {grades[i]}")


# word = "Thursday"
# for char in word:
#     print(char)


# r = range(1_000_000)
# print(50_098 in r)
# print(r[5:15])
# for num in range(10):
#     print(num)

# for num in range(-5, 20, 3):
#     print(num)

# print(range(-5, 20, 3))

# my_range = range(-5, 0)
# print(my_range)

# cities = ['New York', 'Kyiv', 'Paris', 'London', 'Tel Aviv']
# countries = ['USA', 'Ukraine', 'France', 'UK', 'Israel']
#
# for i in range(len(cities)-1, -1, -1):
#     print(f"{countries[i]} - {cities[i]}")


# find max
nums = [54, -1, 45, 987, 5, 2, 65, 7, 12]
# max_num = nums[0]
#
# for num in nums:
#     if num > max_num:
#         max_num = num
# print(max_num)
#
[1000, 54, -1, 45, 987, 5, 2, 65, 7, 12]
# [54, -1, 45, 987, 5, 100, 2, 165, 7, 12]

# nums = [-1, 54, 45, 987, 5, 2, 65, 7, 12]
# nums = [54, -1]
# [54, -1, 56] #Max = 56 secons = -1

# max = 54 second_max = -1
# num = 56
# max = 56
# [54, 5, 56]

#  * second_max  *  max  *

# max_num = max(nums[0:2])
# second_max = min(nums[0:2])
# max_num = nums[0]
# second_max = nums[1]
# for num in nums:
#     # if num < second_max:
#     #     continue
#     if second_max < num <max_num:
#         second_max = num
#     if num > max_num:
#         second_max = max_num
#         max_num = num


# while True:
#     num = input("Insert grades number: ")
#     if num.isdigit() and int(num) > 0:
#         num = int(num)
#         break
#
# names = []
# grades = []
# for i in range(num):
#     name = input("Insert name: ")
#     names.append(name)
#     while True:
#         grade = input(f"Insert {name}'s grade: ")
#         if grade.isdigit() and 0 <= int(grade) <= 100:
#             grade = int(grade)
#             grades.append(grade)
#             break
#
# print(f"Names: {names}, grades: {grades}")
# print(f"The avg is: {sum(grades)/num}")


# num = 19
#
# start_range = int(input("Insert start range: "))
# end_range = int(input("Insert end range: "))
# primes = []

# for num in range(start_range, end_range+1):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             # not prime
#             is_prime = False
#             break
#
#     if is_prime:
#         primes.append(num)
#
# print(primes)


# rows = int(input("Num: "))
# for i in range(1, rows+1):
#     # print single row
#     for j in range(1, i+1):
#         print(j, end=" ")
#     # print('')
#     print('\n', end='')







