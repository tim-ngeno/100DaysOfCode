travel_log = [
    {
        "country": "France",
        "visits": 23,
        "cities": ["Paris", "Lille", "D'jon"],
    },
    {
        "Country": "Germany",
        "visits": 12,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    },
]

# print(travel_log[1])


def new_country(country, visits, cities):
    """adds a new country to a list of dictionaries"""
    new_log = {
        "country": country,
        "visits": visits,
        "cities": cities,
    }

    travel_log.append(new_log)


new_country("Russia", 3, ["Moscow", "Saint Petersburg"])
print(travel_log)
