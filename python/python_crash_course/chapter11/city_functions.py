def get_city(city, country, population=-1):
    if population == -1:
        return f"{city}, {country}"
    else:
        return f"{city}, {country} - population {population}"
