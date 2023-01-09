friend2countries = {
    'lital': ['paris', 'london', 'lyon'],
    'dror': ['new_york', 'kyoto', 'tokyo']
}

city2country = {
    'paris': 'france',
    'london': 'uk',
    'new_york': 'us',
    'lyon': 'france',
    'kyoto': 'japan',
    'tokyo': 'japan'
}

expected_dict = {
    'lital': {
        'france': ['paris', 'lyon'],
        'uk': ['london']
    },
    'dror': {
        'us': ['new_york'],
        'japan': ['tokyo', 'kyoto']
    }
}

def organize_travel_dict(name2city, city2country):
    ret_dict = {}

    for name, cities in name2city.items():
        if name not in ret_dict:
            ret_dict[name] = {}

        for city in cities:
            country = city2country[city]
            if country not in ret_dict[name]:
                ret_dict[name][country] = []
            ret_dict[name][country].append(city)

