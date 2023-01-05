import pprint

person = {
    "id": 123456789,
    "name": "Valeria",
    "birth_year": 1987,
    "address": "Netanya"
}

person2 = {
    "id": 987654321,
    "name": "Daniel",
    "birth_year": 1992,
    "address": "Rishon"
}

persons_list = [person, person2]
persons_dict = {}
#
# for p in persons_list:
#     print(p["name"], p["birth_year"])

for p in persons_list:
    persons_dict[p["id"]] = p

pprint.pprint(persons_dict)
my_id = 9876543211
# print(persons_dict[my_id]["address"])
print(persons_dict
      .get(my_id, {})
      .get("address"))
