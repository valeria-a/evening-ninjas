absolute_path = "/Users/valeria/src/evening-ninjas/lesson12/files/data/alice_in_wonderland.txt"
relative_path = "files/data/alice_in_wonderland.txt"

# class MyTest:
#
#     def __enter__(self):
#         pass
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass

# file_descriptor = open(relative_path, mode='r', encoding='utf-8')
# print(type(file_descriptor))
# content = file_descriptor.read()
# file_descriptor.close()

# with open(relative_path, mode='r', encoding='utf-8') as file_descriptor:
#     content = file_descriptor.read()
#     print("is closed", file_descriptor.closed)
#     print("finished block")
# print("is closed", file_descriptor.closed)
# file_descriptor.read()

# print(content)
# print(type(content))


# with open(relative_path, mode='r', encoding='utf-8') as file_descriptor:
#     content = file_descriptor.read(100)
#     print(content)
#     print("reading next 100 chars....")
#     content = file_descriptor.read(100)
#     print(content)
#     print("setting to 1000")
#     file_descriptor.seek(1000)
#     print(file_descriptor.read(100))
#     print("setting to 0")
#     file_descriptor.seek(0)
#     print(file_descriptor.read(100))
#     file_descriptor.read()
#     print("after the end")
#     print(file_descriptor.read())
#     print(file_descriptor.read())


# with open(relative_path) as f:
#     line = f.readline()
#     while line:
#         print(line, end="")
#         line = f.readline()

# with open(relative_path) as f:
#     print(f.read())

with open(relative_path) as f:
    for line in f:
        print(line, end="")





