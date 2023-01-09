# my_list = [3, 4, 2, 3, 5]
# sorted_list = sorted(my_list)
# print(my_list is sorted_list)

# ret_val = my_list.sort()
# print(ret_val)

weather = {
    'Tel Aviv': {
        'temp': 13,
        'humidity': 60,
        'is_raining': False
    },
    'London': {
        'temp': 3,
        'humidity': 70,
        'is_raining': True
    },
    'Madrid': {
        'temp': 10,
        'humidity': 60,
        'is_raining': False
    }
}

# for k, v in weather.items():
#     # if k.startswith('L'):
#     #     weather.pop(k)
#     #     weather['aaa'] = 8
#     if v['humidity'] > 90:
#         v['is_raining'] = True

# print("Hi")
# v = input()
# print("bye")

# O(1)

# def foo(nums: list[int]) -> int:
#     if nums:
#         return nums[0]
#     else:
#         return None

def foo(nums: list[int]):
    print(nums)

# O(n)

def foo1(nums: list[int]):
    for n1 in nums:
        for n2 in nums:
            print(n1 * n2)

# O(n^2)
#
# foo([1,2,3,4])
# foo([i for i in range(10_000_000)])

a = [3, 4,5 , 6,8]
5 in a

d1 = {
    'z': 45,
    'r': 67,
    'y': 78
}
# _ _ _ _ _ _ _ .... _678_

48752080

# 'y' in d1 -> 678
