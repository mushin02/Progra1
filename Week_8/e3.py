
import json

def get_pokemon_type():

    ptype= input("Choose pokemon type: ")

    with open ("pokemons.json", "r") as file:
        pokemons= json.load (file)

    for pokemon in pokemons:
        if ptype in pokemon["type"]:
            print (f'These are the {ptype} pokemons {pokemon["name"]}')

get_pokemon_type()            