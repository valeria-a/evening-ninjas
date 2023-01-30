import datetime
import json
import os
from json import JSONEncoder

my_dict = {
    'tel_aviv':
        {
            'sun': {'weather': 'cloudy', 'temp': 15,
                    "date": datetime.date(2020, 12, 13)},
            'mon': {'weather': 'sunny', 'temp': 25}
        },
    'netanya':
        {
            'sun': {'weather': 'rainy', 'temp': 13},
            'mon': {'weather': 'cloudy', 'temp': 20}
        },
}
# print(my_dict['netanya']['mon'])
#
with open("weather.json", "w") as f:
    json.dump(my_dict, f)

# class MyEncoder(JSONEncoder):


# path = "files/data/example_2.json"
# path = "files/data/my_persons.json"
#
# with open(path, 'r') as f:
#     # content = f.read()
#     content = json.load(f)
#
# # print(content['quiz']['sport']['q1']['question'])
# print(content[1])

# os.remove()