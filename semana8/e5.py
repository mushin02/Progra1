

import json

def get_level_avg():

    with open("pokemons.json", "r") as file:
        pokemons= json.load(file)

    type_level = {}

    for pokemon in pokemons:
        for ptype in pokemon["type"]:
            if ptype not in type_level:
                type_level[ptype]= []
            type_level[ptype].append(pokemon["level"])   
            
    for ptype, level in type_level.items():
        avg = sum(level) / len(level)
        print (f'Type:{ptype} - avg level: {avg}')   

get_level_avg()