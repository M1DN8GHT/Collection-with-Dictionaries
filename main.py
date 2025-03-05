# Define the initial video game collection
game_collection = {
    "The Legend of Zelda: Breath of the Wild": {
        "genre": "Action-adventure",
        "release_year": 2017,
        "platform": "Nintendo Switch"
    },
    "God of War": {
        "genre": "Action-adventure",
        "release_year": 2018,
        "platform": "PlayStation 4"
    },
    "The Witcher 3: Wild Hunt": {
        "genre": "RPG",
        "release_year": 2015,
        "platform": "Multiple"
    },
    "Red Dead Redemption 2": {
        "genre": "Action-adventure",
        "release_year": 2018,
        "platform": "Multiple"
    }
}

def add_game(collection, game_name, game_properties):
    collection[game_name] = game_properties

def update_game(collection, game_name, property_name, new_value):
    if game_name in collection:
        collection[game_name][property_name] = new_value

def remove_game(collection, game_name):
    if game_name in collection:
        del collection[game_name]

def display_collection(collection):
    for game_name, properties in collection.items():
        print(f"{game_name}:")
        for key, value in properties.items():
            print(f"  {key}: {value}")
        print()

def menu():
    while True:
        print("\nVideo Game Collection Menu")
        print("1. Add a new game")
        print("2. Update an existing game")
        print("3. Remove a game")
        print("4. Display all games")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            game_name = input("Enter the game name: ")
            genre = input("Enter the genre: ")
            release_year = int(input("Enter the release year: "))
            platform = input("Enter the platform: ")
            add_game(game_collection, game_name, {
                "genre": genre,
                "release_year": release_year,
                "platform": platform
            })
        elif choice == '2':
            game_name = input("Enter the game name to update: ")
            property_name = input("Enter the property to update (genre, release_year, platform): ")
            new_value = input("Enter the new value: ")
            if property_name == "release_year":
                new_value = int(new_value)
            update_game(game_collection, game_name, property_name, new_value)
        elif choice == '3':
            game_name = input("Enter the game name to remove: ")
            remove_game(game_collection, game_name)
        elif choice == '4':
            display_collection(game_collection)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()
