import requests

def search_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon = response.json()
        print(f"Name: {pokemon['name'].capitalize()}")
        print(f"ID: {pokemon['id']}")
        print(f"Base XP: {pokemon['base_experience']}")
    else:
        print(f"Pokemon '{name}' not found.")

if __name__ == "__main__":
    # Prompt the user to enter up to 6 Pokemon names, separated by spaces
    input_names = input("Enter up to 6 Pokemon names (separated by spaces): ").split()
    
    if not input_names:
        print("No Pokemon names provided.")
    else:
        # Limit the number of names to 6 or less
        input_names = input_names[:6]

        # Iterate through the provided Pokemon names and call search_pokemon for each
        for pokemon_name in input_names:
            search_pokemon(pokemon_name)
