# Microservice.py by Skylar Posler

import json
import random

def get_pokemon_micro():
    """Generates pokemon name for microservice"""

    randomize_dex = random.randint(0, 898) # generate random index
    location = "path"
    dex =  open(location, encoding="utf-8")
    data = json.load(dex)

    # select random pokemon
    counter = 0
    for idx in data:
        counter += 1 
        if counter == randomize_dex:
            name = data[counter]['name']
            pokemon = name['english']
            pokemon_name = json.dumps(pokemon)

    return pokemon_name

def run_microservice():
    """writes to microservice file"""
    
    while True:
        with open("microservice.txt", "r+") as file:
            line  = file.readline()

        if line == "request":
            pokemon = get_pokemon_micro() # calls the microservice
            outfile = open("microservice.txt", 'w')
            poke_name = pokemon.strip('"')
            outfile.write(poke_name)
            outfile.close()

run_microservice()