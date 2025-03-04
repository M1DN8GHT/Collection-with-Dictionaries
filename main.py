sword = {
    "name": "Excalibur",
    "attack": 10,
    "value": 1000
}

armor = {
    "name": "Chainmail",
    "defense": 5,
    "value": 500
}

shield = {
    "name": "Aegis",
    "defense": 10,
    "value": 750
}

healing_potion = {
    "name": "Small Healing Potion",
    "heal": 10,
    "value": 25
}

inventory = {
    "sword": sword,
    "armor": armor,
    "shield": shield,
    "healing_potion": healing_potion
}
inventory["sword"]["attack"] = 20

inventory["sword"] = {
    "name": "Sting",
    "value": 500,
    "attack": 7,
    "value": 5000
}

market = {
    "apples": 5,
    "oranges": 1
}

market["oranges"] -= 1

del market["oranges"]

market["bananas"] = 10

# This prints each item from the dictionary and its value
for item in market:
    print(f"We have {market[item]} of {item} in stock")

# To get a list of all the keys in a dictionary
list_of_keys = list(market.keys())
print(list_of_keys)
