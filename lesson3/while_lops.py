# g1 = int(input("insert grade 1: "))
# g2 = int(input("insert grade 2: "))
# g3 = int(input("insert grade 3: "))
# a = (g1 + g2 + g3) / 3
# print(a)

# count = 1
# grades_sum = 0
# while count <= 10:
#     grade = int(input("Insert grade: "))
#     # grades_sum = grades_sum + grade
#     grades_sum += grade
#     count += 1
# print(grades_sum/(count-1))
# print("bye")


# # insert 3 grades and print avg
# count = 0
# grades = []
# grades_sum = 0
# while count < 3:
#     grade = int(input("Insert grade: "))
#     grades.append(grade)
#     grades_sum = grades_sum + grade
#     count = count + 1
# print(f"All the grades: {grades}")
# print(f"The avg is: {grades_sum / len(grades)}")



# drink_type = input("Insert drink:").lower().strip()  #beer / wine
#
# while drink_type not in ["beer", "wine"]:
#     drink_type = input("Incorrect input. Insert drink: ").lower().strip()
#
# print(f"You inserted {drink_type}")

#########

# drink_type = None  #beer / wine
# while drink_type not in ["beer", "wine"]:
#     msg = "Incorrect input. Try again: "
#     if drink_type is None:
#         msg = "Insert drink: "
#     drink_type = input(msg).lower().strip()
#
# print(f"You inserted {drink_type}")

# while True:
#     print("hey")


# while True:
#     drink_type = input("Insert drink: ").lower().strip()
#     if drink_type in ["beer", "wine"]:
#         break
# print(f"You inserted {drink_type}")

# incorrect_input = True
# while incorrect_input:
#     drink_type = input("Insert drink: ").lower().strip()
#     if drink_type in ["beer", "wine"]:
#         incorrect_input = False
# print(f"You inserted {drink_type}")

# while False:
#     pass

# ---------------------------------
# end_of_input = False
# temp_max = None
# while not end_of_input:
#     i = input("Insert num or $ to finish: ")
#     if i == '$':
#         end_of_input = True
#     else:
#         num = int(i)
#         if temp_max is None:
#             temp_max = num
#         if num > temp_max:
#             temp_max = num
# print("MAx num", temp_max)
# ------------------

# while loop to create a list of something

# while loop to create a list of lists

# two lists with the same index


# while loops
# count = 0
# grades = []
# while count < 3:
#     grade = int(input("grade: "))
#     grades.append(grade)
#     count += 1
# print(grades)

# num = input("Insert a num: ")
# while not num.isdigit():
#     num = input("Please try again: ")
# print("Great!")

# incorrect_input = True
# first_iteration = True
# message = "Insert a num: "
#
# while incorrect_input:
#
#     if not first_iteration:
#         message = "Please retry: "
#
#     num = input(message)
#     if num.isdigit():
#         incorrect_input = False
#     first_iteration
#
# print("Great")

# option 2

# incorrect_input = True
# message = "Insert a num: "
#
# while incorrect_input:
#
#     num = input(message)
#     if num.isdigit():
#         incorrect_input = False
#
#     message = "Please retry: "
#
# print("Great")

# while True:
#     num = input("Insert a num: ")
#     if num.isdigit():
#         break
#     print("After if")
#
# print("Great")
# print("Bye-bye")

# while True:
#     num = input("Insert a num or $ to finish: ")
#     if num == '$':
#         break
#     num = int(num)
#     if num % 10 == 0:
#         continue
#     print(num)
