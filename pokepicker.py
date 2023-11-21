# Milestone 1 Implementation - PokePicker CLI 
# Features: Default Menu/Pokemon Menu
#           Get Pokemon
#           Add to/View Party
#           View Pokemon Details

import json
import random
import time

party = []
pokemon_details = {"Pokedex Number": [], "Pokemon": [], "Type": [], "Level": []}
pokemon_pc = []


def get_pokemon():
    """Scrapes the pokedex to return a random pokemon"""

    # get json
    randomize_dex = random.randint(0, 898) # generate random index
    location = "C:/Users/Tiana/Documents/Skye's Stuff/School/cs361/Assignment 6/pokedex.json"
    level = random.randint(1, 100) # generate random level
    dex =  open(location, encoding="utf-8")
    data = json.load(dex)

    # select random pokemon
    counter = 0
    for idx in data:
        counter += 1 
        if counter == randomize_dex:
            dex_num = data[counter]['id']
            name = data[counter]['name']
            pokemon = name['english']
            type = data[counter]['type']

    # add to dict
    pokemon_details["Pokedex Number"] = dex_num
    pokemon_details["Pokemon"] = pokemon 
    pokemon_details["Type"] = type
    pokemon_details["Level"] = level

    pokemon_menu(pokemon_details)

def get_pokemon_micro():
    """Generates pokemon name for microservice"""

    randomize_dex = random.randint(0, 898) # generate random index
    location = "C:/Users/Tiana/Documents/Skye's Stuff/School/cs361/Assignment 6/pokedex.json"
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


def find_gen(id):
    """Locates the generation of the chose pokemon"""
    # to implement later

def run_microservice():
    """writes to microservice file"""
    
    while True:
        time.sleep(1)
        file = open("microservice.txt", 'w')
        file.write("request")
        file.close()
        time.sleep(1)

        file = open("microservice.txt", 'r+')
        line = file.readline()
        file.close()
        time.sleep(1)

        if line == "request":
            pokemon = get_pokemon_micro() # calls the microservice
            outfile = open("microservice.txt", 'w')
            poke_name = pokemon.strip('"')
            outfile.write(poke_name)
            outfile.close()
            break
        else:
            print("Microservice Error.")

    return poke_name



def pokemon_menu(pokemon_details):
    """Creates the Pokemon Menu"""

    time.sleep(2)

    print("Your pokemon is ", pokemon_details['Pokemon'], "\n Type: ", pokemon_details['Type'], "\n Level: ", pokemon_details['Level'])
    
    pokemon_menu_select = input("Pokemon Menu:\nSelect 1 to View Pokemon Details\n Select 2 to Add to your Party\n Select 3 to show this pokemon's favorite Food\nSelect 4 to return to the Main Menu\n")

    time.sleep(1)
    if pokemon_menu_select == "1":
        print(pokemon_details)
        check = input("Add this pokemon to the Party? Select 1 for Yes, 2 for No.\n")
        if check == "1" and len(party) < 6:
            party.append(pokemon_details['Pokemon'])
            print(pokemon_details['Pokemon'], "has been added to your Party.\n")
        if check == "2":
            print(pokemon_details['Pokemon'], "was not added to your Party.\n")
            default_menu()
        else:
            print("That is not a valid menu option, please try again.")
            pokemon_menu(pokemon_details)


    if pokemon_menu_select == "2":
        if len(party) >= 6:
            print("Your Party is full! Deposit a pokemon in the PC to keep catching Pokemon!\n")
            time.sleep(1)
            default_menu()
        if len(party) < 6:
            party.append(pokemon_details['Pokemon'])
            print(pokemon_details['Pokemon'], "has been added to your Party.\n")
            time.sleep(1)
            default_menu()

        # if pokemon_menu_select == "3":

        #     # to implement later

    if pokemon_menu_select == "4":
        checker = input("If you return to the Main Menu, this pokemon may be lost. Return anyways? Select 1 for Yes, 2 for No.\n")
        if checker == "1":
            time.sleep(1)
            default_menu()
        if checker == "2":
            time.sleep
            pokemon_menu(pokemon_details)
        else:
            print("That is not a valid menu option, please try again\n")
            pokemon_menu(pokemon_details)
    else:
        print("That is not a valid menu option, please try again.\n")
        pokemon_menu(pokemon_details)

def deposit_pc(party):
    """deposits a current pokemon from the party into the PC"""
    # to implement later

def view_party(party):
    """Returns the party of the current User"""

    if len(party) < 1:
        print("Your Party is empty. Catch some pokemon!")
        time.sleep(1)
        default_menu()
    else:
        print("Your Party is\n", party)
        print("\n")
        time.sleep(1)
        default_menu()

def default_menu():
    """Creates the default menu for the CLI"""

    menu_selection = input("PokePicker Main Menu:\nSelect 1 to Catch a new Pokemon!\nSelect 2 to View Your Current Party\nSelect 3 to Exit the PokePicker\n")

    while menu_selection is not None:

        if menu_selection == "1":
            return get_pokemon()
        
        if menu_selection == "2":
            view_party(party)

        if menu_selection == "3": 
            time.sleep(1)
            print("Thank you for using the PokePicker, come back soon!")
            exit()
        else:
            time.sleep(1)
            print("That is not a vaild menu option, please try again.\n")
            default_menu()

run_microservice()