# nums = [3, 6, 2, 1, 3, 7, 7]
#
# if nums[0] > nums[1]:
#     largest, second_largest = nums[0], nums[1]
# else:
#     second_largest, largest = nums[0], nums[1]
#
#
# # all the elements in the list are the same
# if len(nums) == 0 or nums.count(nums[0]) == len(nums):
#     print('None')
#
# for n in nums[2:]:
#     if n > second_largest:
#         pass
#     elif second_largest <= n <= largest:
#         second_largest = n
#     # n  second_largest  largest - nothing to do
#     # second_largest  n  largest => second_largest = n
#     # second_largest  largest  n =>  second_largest = largest, largest = n