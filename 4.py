#  Dictionaries in Python
# https://realpython.com/python-dicts/

# Challenge

# Dot doesn't travel to Europe often, so they decide to take the most expensive option for each course as well as drink. Create a new dictionary called meals that will contain the names of the courses as the keys (starters, mains...), and the name of the food or drink item as the values.

# After assembling the dictionary appropriately, when Dot gives a 10% tip on this meal, how much will the tip come out to?

starters = {
    "Potato Pancakes": 7.99,
    "Salami Platter": 10.29,
    "Brezel": 6.99,
    "Maultaschen": 9.99,
    "Fried Potatoes": 4.99
}

mains = {
    "Braised Beef Short Ribs": 18.99,
    "Paprika Beef Goulash": 15.5,
    "Jager Schnitzel": 16.99,
    "House-mase Bratwurst": 11.99,
    "Kasespatzle": 14.99,
    "German Ravioli": 12.79,
    "Curry Wurst": 10.99
}

desserts = {
    "Chilled Chocolate Fondant": 7.9,
    "Pepermint Crisp Tart": 5.9,
    "Ginger Cobbler": 6.9,
    
}

beers = {
    "Stigel Radler": 6.9,
    "Munich Lager": 7.9,
    "Kong Ludwig Weissbier": 8.9,
    "Warsteiner Punkel": 7.5,
}


# if you want to see the keys of the dictionary in the list: keys = list(starters.keys())
# if you want to see the keys of the dictionary in the list: values = list(starters.values())
keys = list(beers.keys())
values = list(beers.values())
print(keys)
print(values)
print(starters["Salami Platter"])


meals = {
    "starters": "Salami Platter",
    "mains": "Braised Beef Short Ribs",
    "desserts": "Chilled Chocolate Fondant",
    "beers": "Kong Ludwig Weissbier"
}

total = starters["Salami Platter"] + mains["Braised Beef Short Ribs"] + desserts["Chilled Chocolate Fondant"] + beers["Kong Ludwig Weissbier"]
print(total)
tips = total * 0.1
print(tips)


# SOLUTION

starter_keys = list(starters.keys())
starter_keys

mains_keys = list(mains.keys())
mains_keys

desserts_keys = list(desserts.keys())
desserts_keys

beers_keys = list(beers.keys())
beers_keys

meals = {
}

meals["starters"] = starter_keys[1]
meals["mains"] = mains_keys[0]
meals["desserts"] = desserts_keys[0]
meals["beers"] = beers_keys[2]

meals

(starters[meals['starters']] +
 mains[meals['mains']] +
 desserts[meals['desserts']] +
 beers[meals['beers']]) * 0.1
