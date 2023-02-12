import json

import requests

if __name__ == '__main__':
    # response = requests.get("https://api.kanye.rest/")
    # if response.status_code == 200:
    #     # print(json.loads(response.text)['quote'])
    #     print(response.json()['quote'])

    # response = requests.get("https://api.genderize.io/",
    #                         params={'name': 'shani'})
    # if response.status_code == 200:
    #     print(response.json())

    country = input("insert a country: ")
    response = requests.get(
        f"https://restcountries.com/v3.1/name/{country}")

# https://genderize.io?name=shani&country=israel
# https://genderize.io/shani

# https://www.amazon.com/BENGOO-G9000-Controller-Cancelling-Headphones/dp/B01H6GUCCQ/

# https://www.imdb.com/movies
# https://www.imdb.com/movies/234645/
# https://www.imdb.com/movies/234645/actors/
# https://www.imdb.com/movies/234645/actors/34757934

# https://www.imdb.com/actors
# https://www.imdb.com/actors/34568345