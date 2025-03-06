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
    },
    "Cyberpunk 2077": {
        "genre": "RPG",
        "release_year": 2020,
        "platform": "Multiple"
    },
    "Minecraft": {
        "genre": "Sandbox",
        "release_year": 2011,
        "platform": "Multiple"
    },
    "Fortnite": {
        "genre": "Battle Royale",
        "release_year": 2017,
        "platform": "Multiple"
    },
    "Overwatch": {
        "genre": "First-person shooter",
        "release_year": 2016,
        "platform": "Multiple"
    },
    "Apex Legends": {
        "genre": "Battle Royale",
        "release_year": 2019,
        "platform": "Multiple"
    },
    "Hades": {
        "genre": "Roguelike",
        "release_year": 2020,
        "platform": "Multiple"
    }
}

# Function to add a new game to the collection
def add_game(collection, game_name, game_properties):
    collection[game_name] = game_properties

# Function to update an existing game in the collection
def update_game(collection, game_name, property_name, new_value):
    if game_name in collection:
        collection[game_name][property_name] = new_value

# Function to remove a game from the collection
def remove_game(collection, game_name):
    if game_name in collection:
        del collection[game_name]

# Function to display all games in the collection
def display_collection(collection):
    for game_name, properties in collection.items():
        print(f"{game_name}:")
        for key, value in properties.items():
            print(f"  {key}: {value}")
        print()

# Function to display the menu and handle user input
def menu():
    while True:
        # Display the menu options
        print("\nVideo Game Collection Menu")
        print("1. Add a new game")
        print("2. Update an existing game")
        print("3. Remove a game")
        print("4. Display all games")
        print("5. Exit")
        choice = input("Enter your choice: ")

        # Handle the user's choice
        if choice == '1':
            # Add a new game
            game_name = input("Enter the game name: ")
            genre = input("Enter the genre: ")
            release_year = int(input("Enter the release year: "))
            platform = input("Enter the platform: ")
            add_game(game_collection, game_name, {
                "genre": genre,
                "release_year": release_year,
                "platform": platform
            })
            input("Press any key to continue.")
        elif choice == '2':
            # Update an existing game
            game_name = input("Enter the game name to update: ")
            property_name = input("Enter the property to update (genre, release_year, platform): ")
            new_value = input("Enter the new value: ")
            if property_name == "release_year":
                new_value = int(new_value)
            update_game(game_collection, game_name, property_name, new_value)
            input("Press any key to continue.")
        elif choice == '3':
            # Remove a game
            game_name = input("Enter the game name to remove: ")
            remove_game(game_collection, game_name)
            input("Press any key to continue.")
        elif choice == '4':
            # Display all games
            display_collection(game_collection)
            input("Press any key to continue.")
        elif choice == '5':
            # Exit the menu
            break
        else:
            # Handle invalid choice
            print("Invalid choice. Please try again.")
            input("Press any key to continue.")

# Run the menu
menu()
