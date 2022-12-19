# grades = [90, 98, 99, 96]

# grades = [[90, 87, 70], [100, 70], [90], []]
# print(grades[2])
# print("grades[0]: ", grades[0])
# print("grades[0][0]: ", grades[0][0])
# print("grades[0][0][0]: ", grades[0][0][0])

my_list = [
    ["banana", "apple"],
    [[3.5, 7, 20], [5.6, 9, 10]],
    [
        [
            ["a", "b"],
            ["dd", "ee"],
            ["yy", "yy"]
        ]
        ,
        [["rr", "r"], ["ttt"], ["y", "o"]]
    ]
]

l1 = [my_list[0][0]]
ab = my_list[2][0][0]
print(ab)
print(l1)
new_list = l1 + [ab]
print(new_list)
# print(my_list[2][0][::2])
# print(my_list[2][0][1][1:])
# [["a", "b"], ["yy", "yy"]]
