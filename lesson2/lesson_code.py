# b1 = True
# b2 = False

# print(b1 and b2)
# print(3 and 5)

# print(bool(3))
# print(bool(0))

# drink_type = "water"
# # incorrect
# if drink_type == "beer" or "wine":
#     print("inside if")
#
# if drink_type == "beer" or drink_type == "wine":
#     print("inside if")

######
# string methods
######

# operators + - <=
# built-in functions: print(), input(), round(), int()
# methods: text.upper()

text = "The sun is shining and the life is beautiful!"
# print(text[2])
# print(text[3])
# print(text[-1])
# print(text[-5])
# print(len(text))
# word = "hello"
# print(len(word))
# print(word[len(word)-1])
# # print(word[5])
# print(word[-10])
text = "The sun is shining and the life is beautiful!"
# print(text[4:10])
# print(text[-20:-10])
# print(text[20:])
# print(text[:20])
# print(text[4:20:2])
# print(text[20:4])
# print(text[20:4:-1])
# print(text[::-1])

# "/usr/valeria/documents/my_file.txt"

# print("sun" in text)
# print("Sun" in text)
# print("!" in text)


# print("Hello" + " " + "World")
#
# res = "Hello" + " " + "World"
# print(res)

print("Hello" * 10)

# print("Hello" * "World")
# print("Hello" * 2.3)

# print("HHHHH" / 3)
# string slicing

# string methods
str1 = "baNaNa"
# str1upper = str1.upper()
# print(str1upper)
# print(str1)

# print(str1.lower())
# print(str1.upper())
# print(str1.title())
# print("hello world".title())

# str1 = "baNaNa"
# str1 = str1.upper()

str1 = "baNaNa"
# ret_val = str1.find("N")
# print(ret_val)
# str1.find("N", ret_val+1)
# print(str1.find("NaN"))
# print(str1.find("!"))
# print(str1.count("a"))
# str1.strip()

# num = int(input("Insert a num: "))
# print(num ** 2)

num = input("Insert a num:")
num = num.strip()
if num.isdigit():
    num = int(num)
    print(num ** 2)
else:
    print("Invalid input")




#operator in
# grades = [90, 95, 97, 85]
# print(50 in grades)
# print(97 in grades)

# print(text)
# print("THE" in text)
# print("the" in text.lower())
#
# drink_type = input("Insert drink").lower()
# if drink_type.lower() == 'beer':

# more string methods
# print(text)
ret_val = text.find("sun")
ret_val = text.find("the")
ret_val = text.find("i")
ret_val = text.find(" ")
ret_val = text.find(" ", 10)
# look for a space starting from the word "shining"
shining_idx = text.find("shining")
ret_val = text.find(" ", shining_idx)

ret_val = text.find("blabla")
ret_val = text.index(" ")
ret_val = text.index("shining")
# ret_val = text.index("blabla")
ret_val = text.count(" ")
ret_val = "    the sun        ".strip()
ret_val = "    The Sun        ".strip().lower().index("s")
# ret_val = "    The Sun        ".strip().lower().index("s").lower() #wrong
# ret_val = text.endswith("!")

# words_list = text.split(" ")
# ret_val = "_".join(words_list)
# ret_val = "_$blabla$_".join(words_list)
# ret_val = "_".join(["aaaa", "bbbb"])
# print(words_list)

# ret_val = text.replace(" ", "_")
#
# hours = 9
# minutes = 20
# seconds = 8
# ret_val = ":".join([str(hours), str(minutes), str(seconds)])
# print(ret_val)

######
# exercises - A9 (ex 1 - 4)

########
# motivation for lists


# ret_val = text.split(" ")
# print(ret_val)
# print(type(ret_val))
# print(ret_val[::-1])


# lists
my_list = []
my_list = ["Hello", 'World']
grades = [90, 95, 97, 85]
# print(grades[2])
various_list = ["Hello", [], True, 5.733, 78,
                ["aaa", 'bbb', [1,2,3,4]]]
# various_list[2] #bool
# various_list[3] #float
# print(various_list[-1])
# temp = various_list[-1]
# print(temp)
# temp[0] #aaa
# various_list[-1][-1][2]
# various_list[1][1]  #error
# grades[7]
# print([3, 4, 5])
# print([3, 4, 5][0]) # prints 3
# print([3, 4, 5], [0]) # prints 2 lists
# t = [3, 4, 5]
# print(t[0])

# nested lists

# l1 = [[2, 3, 4], [20, 30, [40]]]
# print(l1[-1][-1] > 30) # WRONG!
# print(int(l1[-1][-1]) > 30) # WRONG!
# print(l1[-1][-1][0] > 30)


#####
## A5

# more built-in functions
# print(len(grades))
# print(len(text))
# print(text)
# print(text[3] == ' ')
# print(len(""))
# print(len([]))
# print(type(len([])))
# print(type(len))
# print(len(5))
# seats = input("Insert seats: ")
# split_seats = seats.split(" ")
# print(split_seats)
# print("split_seats[0]=", split_seats[0])
# if len(split_seats) == 2


########
########
## ex A9 - 5



# list methods
# l1 = []
# g1 = int(input("insert g1 "))
# g2 = int(input("insert g2 "))
# r1 = l1.append(g1)
# print(f"new l1: {l1}")
# print(f"return value of append: {r1}")
# print(l1.append(g1))
# l1.append(g2)
# print(l1)
# new_text = text.lower()
# l1.append("gfd")
# print(l1)
# l1.append(g1)
# print(l1)
# l1.append(g2)
# print(l1)
# l1.pop(0)
# l1.remove(90)
# print(l1)
# l2 = [10, 20, 30, 50]
# print(l2)
# l2.insert(3, 40)
# print(l2)
#
# l3 = [90, 50, 67, 50]
# print(l3.count(50))
