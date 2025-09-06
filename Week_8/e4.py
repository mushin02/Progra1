


import json

def print_statistics():

    with open("pokemons.json", "r") as file:
        pokemons= json.load(file)

        for pokemon in pokemons:
            print(f'name: {pokemon["name"]["english"]}')
            print(f'attack: {pokemon ["base"]["Attack"]}')
            print(f'defence: {pokemon["base"]["Sp. Defense"]}')
            print(f'speed: {pokemon["base"]["Speed"]}')
            print ()


print_statistics()            