# nums = [4, 12, 4, -9, 0, 5]
# print(sorted(nums))
# print(nums)
#
# print("#2")
# print(nums.sort())
# print(nums)
import pprint

# words = ['apple', 'pear', 'orange']
# print(sorted(words))

# my_dict = {
#     'london': 2,
#     'paris': 0,
#     'tel_aviv': 13
# }
# p = {
#     'id': 234234,
#     'name': 'sdfsdf',
#     'address': 'sdfsd'
# }
# print(sorted(my_dict))

l1 = [
    {'tel_aviv': {'weather': 'sunny', 'temp': 13}},
    {'paris': {'weather': 'cloudy', 'temp': 1}},
    {'london': {'weather': 'rain', 'temp': 3}}
]

# def key_by_temp(elem):
#     return list(elem.values())[0]['temp']
#
# pprint.pprint(sorted(l1, key=key_by_temp, reverse=True))

words = ['apple', 'pear', 'orange', 'kiwi', 'mangustin']
print(sorted(words, key=len))
