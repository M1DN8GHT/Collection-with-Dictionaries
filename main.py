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

print(inventory["sword"]["value"]) 
inventory["sword"]["attack"] = 20
print(inventory["sword"]["attack"])

sword = {
    "name": "Sting",
    "attack": 7,
    "value": 5000
}
print(inventory["sword"])