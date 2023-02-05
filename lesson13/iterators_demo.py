drinks = ['coffee', 'tea', 'juice', 'coke']
# drinks = {'a': 1, 'b':2, 'c':3}

for d in drinks:
    print(d)

# for k, v in drinks.items():
#     print(k, v)

drinks_iterator = iter(drinks)
print(type(drinks_iterator))
val = next(drinks_iterator)
print(val)
# val = next(drinks_iterator)
# print(val)
print(next(drinks_iterator))
print(next(drinks_iterator))
print(next(drinks_iterator))
print(next(drinks_iterator))

# class MyClass:
#     # pass
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         pass
#
#
# m = MyClass()
# for i in m:
#     print(i)