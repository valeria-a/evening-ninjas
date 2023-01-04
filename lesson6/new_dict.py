cities = {
    "UK": "London",
    "Israel": "Jerusalem",
    "France": "Paris",
    # 0: 365
    # "UK": "Manchester"
}
# print(cities)
# print(cities["UK"])
# print(cities[0])

# months = {
#     1: "jan",
#     2: "feb",
#     3: "mar"
# }
#
# print(months[2])
# # print(months[50])
# print(months.get(50, "no value"))

# grades = {
#     "Daniel": [90, 99, 100],
#     "Barel": [99, 90]
# }
#
# # print(grades["Daniel"][-1])
# grades["Slava"] = [98, 97]
# print(grades)
# grades["Barel"].append(100)
# print(grades)

# my_set = set()
#
# my_dict = dict()
# my_dict = {}
#
# my_list = []
# my_list = list()
#
# my_tuple = ()
# my_tuple = tuple()

# for country in cities:
#     print(country, cities[country])

# for country in cities.keys():
#     print(country, cities[country])

# for city in cities.values():
#     print(city)


#
# for elem in cities.items():
#     # print(elem)

# for country, city in cities.items():
#     print(country, city)


grades = {
    "Daniel": [90, 99, 100],
    "Barel": [99, 90],
    "Slava": [100, 98]
}

grades1 = {
    "Or": [99, 100],
    "Nadav": [99, 98, 100],
    "Daniel": []
}

# for name, grades_list in grades.items():
#     if 100 in grades_list:
#         print(name)

# grades.pop("Barel")
# del grades["Barel"]
# print(grades)

# print(dict.fromkeys(["a", "b", "c"], 10))

grades.update(grades1)
print(grades)
print(grades1)
