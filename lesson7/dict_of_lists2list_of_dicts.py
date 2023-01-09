def dict_of_lists2list_of_dicts(input_dict):
    list_of_dicts = []
    # d1 = {}

    for j in range(len(list(input_dict.values())[0])):
        d1 = {}
        for key, value in input_dict.items():
            d1[key] = input_dict[key][j]
            list_of_dicts.append(d1)

    return list_of_dicts

rainfall_mm = {'Tokyo': [15, 37, 62, 4], 'Osaka': [0, 3, 60, 45]}

# expected:
# [
#     {'Tokyo': 15, 'Osaka': 0},
#     {'Tokyo': 37, 'Osaka': 3},
#     {'Tokyo': 62, 'Osaka': 60},
#     {'Tokyo': 4, 'Osaka': 45},
# ]

print(dict_of_lists2list_of_dicts(rainfall_mm))