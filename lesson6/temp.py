# import pprint
#
# def insert_persons(n: int) -> dict:
#     ret_dict = {}
#     for i in range(1,n+1):
#         one_p_dict = {"id_num": "0", "first_name": "", "last_name": "", "birth_year": "0", "phone_num": ""}
#         print(f"Enter information for person number {i}:")
#         for key_name in one_p_dict.keys():
#             temp_value = input(f"Enter {key_name}: ")
#             one_p_dict[key_name] = temp_value
#         ret_dict[one_p_dict["id_num"]] = one_p_dict
#     return ret_dict
#
# # ret_dict: {"111" : one_p_dict, "222": one_p_dict, "333":  one_p_dict}
#
# persons_num = int(input("Enter a number of persons: "))
# pprint.pprint(insert_persons(persons_num))

import pprint


def insert_persons(n: int) -> dict:
    persons_dict = {}
    for i in range(n):

        person = {}
        fields_name = {'id': ['ID', int],
                       'name': ['name', str],
                       'birth_year': ['birth year', int],
                       'address': ['address', str]}
        for field, field_data in fields_name.items():
            value = input(f'Please enter {field_data[0]}: ')
            value_type = field_data[1]
            person[field] = value_type(value)

        persons_dict[person['id']] = person

    return persons_dict


pprint.pprint(insert_persons(2))