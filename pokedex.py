import requests

def search_pokemon(name):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")
    print(response.json())


if __name__ == "__main__":
    search_pokemon("charmander")