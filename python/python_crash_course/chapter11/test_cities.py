from city_functions import get_city

def test_city_country():
    countries = ['China', 'Japan', 'America']
    cities = ['Chengdu', 'Tokyo', 'New York']
    populations = [1230000, 232000, 2300001]

    for (city, country) in zip(cities, countries):
        assert get_city(city, country) == f"{city}, {country}"

    for (city, country, population) in zip(cities, countries, populations):
        assert get_city(city, country, population) == f"{city}, {country} - population {population}"

