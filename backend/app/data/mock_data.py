BUSINESS_TYPES = [
    {"id": "coffee_shop", "name": "Coffee Shop"},
    {"id": "bakery", "name": "Bakery"},
    {"id": "gym", "name": "Gym"},
    {"id": "salon", "name": "Salon"},
    {"id": "bookstore", "name": "Bookstore"},
]

NEIGHBORHOODS = [
    {"id": "allston", "name": "Allston"},
    {"id": "back_bay", "name": "Back Bay"},
    {"id": "beacon_hill", "name": "Beacon Hill"},
    {"id": "dorchester", "name": "Dorchester"},
    {"id": "fenway", "name": "Fenway"},
    {"id": "jamaica_plain", "name": "Jamaica Plain"},
    {"id": "mission_hill", "name": "Mission Hill"},
    {"id": "north_end", "name": "North End"},
    {"id": "roxbury", "name": "Roxbury"},
    {"id": "seaport", "name": "Seaport"},
    {"id": "south_boston", "name": "South Boston"},
    {"id": "south_end", "name": "South End"},
]

NEIGHBORHOOD_SCORES = [
    {
        "id": "allston",
        "name": "Allston",
        "scores": {
            "demand": 86,
            "competition": 58,
            "affordability": 72,
            "transit": 84,
            "growth": 78,
        },
    },
    {
        "id": "back_bay",
        "name": "Back Bay",
        "scores": {
            "demand": 92,
            "competition": 42,
            "affordability": 35,
            "transit": 93,
            "growth": 70,
        },
    },
    {
        "id": "beacon_hill",
        "name": "Beacon Hill",
        "scores": {
            "demand": 76,
            "competition": 55,
            "affordability": 38,
            "transit": 88,
            "growth": 60,
        },
    },
    {
        "id": "dorchester",
        "name": "Dorchester",
        "scores": {
            "demand": 74,
            "competition": 76,
            "affordability": 82,
            "transit": 70,
            "growth": 84,
        },
    },
    {
        "id": "fenway",
        "name": "Fenway",
        "scores": {
            "demand": 88,
            "competition": 50,
            "affordability": 48,
            "transit": 90,
            "growth": 75,
        },
    },
    {
        "id": "jamaica_plain",
        "name": "Jamaica Plain",
        "scores": {
            "demand": 80,
            "competition": 68,
            "affordability": 70,
            "transit": 72,
            "growth": 73,
        },
    },
    {
        "id": "mission_hill",
        "name": "Mission Hill",
        "scores": {
            "demand": 82,
            "competition": 64,
            "affordability": 67,
            "transit": 82,
            "growth": 79,
        },
    },
    {
        "id": "north_end",
        "name": "North End",
        "scores": {
            "demand": 84,
            "competition": 45,
            "affordability": 40,
            "transit": 78,
            "growth": 62,
        },
    },
    {
        "id": "roxbury",
        "name": "Roxbury",
        "scores": {
            "demand": 72,
            "competition": 80,
            "affordability": 86,
            "transit": 68,
            "growth": 88,
        },
    },
    {
        "id": "seaport",
        "name": "Seaport",
        "scores": {
            "demand": 90,
            "competition": 48,
            "affordability": 30,
            "transit": 76,
            "growth": 92,
        },
    },
    {
        "id": "south_boston",
        "name": "South Boston",
        "scores": {
            "demand": 83,
            "competition": 60,
            "affordability": 52,
            "transit": 74,
            "growth": 82,
        },
    },
    {
        "id": "south_end",
        "name": "South End",
        "scores": {
            "demand": 87,
            "competition": 46,
            "affordability": 42,
            "transit": 86,
            "growth": 72,
        },
    },
]

BUSINESS_TYPE_WEIGHTS = {
    "coffee_shop": {
        "demand": 0.30,
        "competition": 0.20,
        "affordability": 0.15,
        "transit": 0.25,
        "growth": 0.10,
    },
    "bakery": {
        "demand": 0.25,
        "competition": 0.20,
        "affordability": 0.20,
        "transit": 0.20,
        "growth": 0.15,
    },
    "gym": {
        "demand": 0.25,
        "competition": 0.15,
        "affordability": 0.20,
        "transit": 0.15,
        "growth": 0.25,
    },
    "salon": {
        "demand": 0.25,
        "competition": 0.25,
        "affordability": 0.20,
        "transit": 0.15,
        "growth": 0.15,
    },
    "bookstore": {
        "demand": 0.20,
        "competition": 0.25,
        "affordability": 0.25,
        "transit": 0.15,
        "growth": 0.15,
    },
}