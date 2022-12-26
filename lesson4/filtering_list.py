fruits = ["banana", "apple", "pear", "ananas", "cherry"]

# filtered_list = []
# for f in fruits:
#     if 'a' not in f:
#         filtered_list.append(f)
#
# print(filtered_list)
#
# for f in fruits:
#     if "a" in f:
#         fruits.remove(f)
#

# fruits = ["banana", "apple", "pear", "ananas", "cherry"]
# 4  ["banana", "apple", "pear", "ananas", "cherry"]
# 3 ["banana", "apple", "pear",  "cherry"]
# 2 ["banana", "apple", "cherry"]
# 1
for i in range(len(fruits)-1, -1, -1):
    if "a" in fruits[i]:
        fruits.pop(i)

# for i in range(len(fruits)):
#     if "a" in fruits[i]:
#         fruits.pop(i)

# print(fruits)