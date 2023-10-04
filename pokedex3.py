import requests

def search_pokemon(name, number):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon = response.json()

        # Extract HP stat value from the stats array
        hp_stat = next((stat for stat in pokemon['stats'] if stat['stat']['name'] == 'hp'), None)
        hp_value = hp_stat['base_stat'] if hp_stat else 'N/A'

        # Extract move names from the moves array
        move_names = [move['move']['name'] for move in pokemon['moves']]

        # Extract held item names from the held_items array
        held_item_names = [item['item']['name'] for item in pokemon['held_items']]

        print('*******************')
        print(f"Number: {number}")
        print(f"Name: {pokemon['name'].capitalize()}")
        print(f"ID: {pokemon['id']}")
        print(f"HP: {hp_value}")
        print(f"Base XP: {pokemon['base_experience']}")
        print(f"Moves:")
        for move in move_names:
            print(f"  - {move.capitalize()}")
        print(f"Held Items:")
        for item in held_item_names:
            print(f"  - {item.capitalize()}")
        
    else:
        print(f"Pokemon '{name}' not found.")

if __name__ == "__main__":
    # Initialize an empty list to store Pokemon names
    input_names = []

    # Prompt the user to enter up to 6 Pokemon names one at a time
    for i in range(6):
        name = input(f"Enter Pokemon name {i+1} (or press Enter to finish): ").strip()
        if name:
            input_names.append(name)
        else:
            break
    
    if not input_names:
        print("No Pokemon names provided.")
    else:
        # Iterate through the provided Pokemon names and call search_pokemon for each
        for index, pokemon_name in enumerate(input_names, start=1):
            search_pokemon(pokemon_name, index)
