cities = ['Tel Aviv', 'London', 'New York', 'Paris']
countries = ['Israel', 'UK', 'US', 'France']

# {'Tel Aviv' : 'Israel', ....}

ret_dict = {}
# for i in range(len(cities)):
#     ret_dict[cities[i]] = countries[i]

for city, country in zip(cities, countries):
    ret_dict[city] = country
    
print(ret_dict)
