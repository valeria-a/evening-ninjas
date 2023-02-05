l1 = ['drink', 'sit', 'stand', 'sleep']
# l2 = []
# for elem in l1:
#     l2.append(elem.upper())


ret_val = list(map(str.upper, l1))
print(ret_val)
# for e in ret_val:
#     print(e)

print(list(map(len, l1)))


nums1 = [1, 2, 3, 4, 5]
nums2 = [10, 20, 30, 40, 50]

# [11, -18, 33, -36, 55]

def my_mapping_func(n1, n2):
    if n1 % 2 == 1:
        return n1 + n2
    else:
        return n1 - n2



# print(list(map(my_mapping_func, nums1, nums2)))

# print(list(map(sum, nums1, nums2)))
# print(list(map(my_mapping_func, nums1)))

def my_sum(*args, **kwargs):
    print(kwargs)
    return sum(args)

print(my_sum(3, 4, 5, 6, 7, a=1, b='h', c=4))

print(list(map(my_sum, nums1, nums2, [100, 200, 300])))