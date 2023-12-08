# PokePicker CLI by Skylar Posler for CS361 - Oregon State University
# A Pokemon Catching Game Simulation
# Utilizes pokemon-data.json by Purukitto - https://github.com/Purukitto/pokemon-data.json
# Microservice by Matt Trimner

import json
import random
import time

from clint.textui import puts, indent, colored
from pyfiglet import Figlet

party = []
pokemon_details = {"Pokedex Number": [], "Pokemon": [], "Type": [], "Level": []}
pokemon_pc = []

def get_pokemon():
    """Scrapes the pokedex to return a random pokemon"""

    randomize_dex = random.randint(0, 898) 
    location = "C:/Users/Tiana/Documents/Skye's Stuff/School/cs361/Assignment 6/pokedex.json"
    level = random.randint(1, 100) 
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


    pokemon_details["Pokedex Number"] = dex_num
    pokemon_details["Pokemon"] = pokemon 
    pokemon_details["Type"] = type
    pokemon_details["Level"] = level

    pokemon_menu(pokemon_details)

def catching():
    """progress bar 1"""

    puts(colored.green("Catching..."))
    time.sleep(1)

def logging_in():
    """progress bar 2"""

    puts(colored.blue("Logging into your Pokemon PC..."))
    time.sleep(1)

def returning():
    """progress bar 3"""

    puts(colored.cyan("Returning to the Main Menu..."))
    time.sleep(1)

def run_microservice():
    """writes to microservice file"""

    with open("./food_service.txt", "r+") as file:
        file.seek(0)
        file.truncate()
        file.write("request")
        file.flush()
        time.sleep(1)
        file.seek(0)
        food = file.read()
    return food

def pokemon_menu(pokemon_details):
    """Creates the Pokemon Menu"""

    with indent(20):
        print(f"Your pokemon is {pokemon_details['Pokemon']}\nLevel: {pokemon_details['Level']}")

    print("\n")
    
    pokemon_menu_select = input("Pokemon Menu:\n Select 1 to View Pokemon Details\n Select 2 to Add to your Party\n Select 3 to Discover this Pokemon's Favorite Food\n Select 4 to Return to the Main Menu\n")

    time.sleep(1)
    if pokemon_menu_select == "1":
        dex_entry = str(pokemon_details)
        print("\n")
        puts(colored.green(dex_entry))
        print("\n")
        puts(colored.green(f"Add {pokemon_details['Pokemon']} to the Party?\n"))
        check = input("Select 1 for Yes, 2 for No.\n")

        if check == "1" and len(party) < 6:
            party.append(pokemon_details['Pokemon'])
            puts(colored.green(f"{pokemon_details['Pokemon']} has been added to your Party.\n"))
            default_menu()

        elif check == "1" and len(party) >= 6:
            puts(colored.red(f"Your Party is full! Would you like to deposit a Party pokemon in your PC in order to keep {pokemon_details['Pokemon']} in your Party?\n"))
            response = input("Select 1 for Yes, 2 for No.\n")

            if response == "1":
                logging_in()
                logging_in()
                puts(colored.blue("Log in Successful!\n"))
                deposit_pc(party)
                party.append(pokemon_details['Pokemon'])
                puts(colored.green(f"{pokemon_details['Pokemon']} has been added to your Party.\n"))
                default_menu()

            elif response == "2":
                puts(colored.red(f"If you do not deposit a Party pokemon, {pokemon_details['Pokemon']} will be lost. Continue?\n")) 
                reply = input("Select 1 for Yes, 2 for No.\n")

                if reply == "1":
                    returning()
                    returning()
                    print("\n")
                    default_menu()

                elif reply == "2":
                    time.sleep(1)
                    pokemon_menu(pokemon_details)
                    
        elif check == "2":
            puts(colored.red(f"{pokemon_details['Pokemon']} was not added to your Party.\n"))
            time.sleep(1)
            default_menu()
        else:
            puts(colored.red("That is not a valid menu option, please try again."))
            pokemon_menu(pokemon_details)


    elif pokemon_menu_select == "2":
        if len(party) >= 6:
            puts(colored.red(f"Your Party is full! Would you like to deposit a Party pokemon in your PC in order to keep {pokemon_details['Pokemon']} in your Party?\n"))
            pc_input = input("Select 1 for Yes, 2 for No.\n")

            if pc_input == "1":
                logging_in()
                logging_in()
                puts(colored.blue("Log in Successful!\n"))
                deposit_pc(party)
                party.append(pokemon_details['Pokemon'])
                puts(colored.green(f"{pokemon_details['Pokemon']} has been added to your Party.\n"))
                default_menu()

            elif pc_input == "2":
                puts(colored.red(f"If you do not deposit a Party pokemon, {pokemon_details['Pokemon']} will be lost. Continue?\n")) 
                checker = input("Select 1 for Yes, 2 for No.\n")

                if checker == "1":
                    returning()
                    returning()
                    print("\n")
                    default_menu()

                elif checker == "2":
                    time.sleep(1)
                    pokemon_menu(pokemon_details)

        elif len(party) < 6:
            party.append(pokemon_details['Pokemon'])
            puts(colored.green(f"{pokemon_details['Pokemon']} has been added to your Party.\n"))
            time.sleep(1)
            default_menu()

    
    elif pokemon_menu_select == "3":
       food = run_microservice()
       puts(colored.magenta(f"{pokemon_details['Pokemon']}'s favorite food is {food}!\n"))
       pokemon_menu(pokemon_details)

    elif pokemon_menu_select == "4":
        puts(colored.red(f"If you return to the Main Menu, {pokemon_details['Pokemon']} will be lost. Return anyways?\n")) 
        checker = input("Select 1 for Yes, 2 for No.\n")

        if checker == "1":
            returning()
            returning()
            print("\n")
            default_menu()

        elif checker == "2":
            time.sleep(1)
            pokemon_menu(pokemon_details)

        else:
            puts(colored.red("That is not a valid menu option, please try again.\n"))
            time.sleep(1)
            pokemon_menu(pokemon_details)

    else:
        puts(colored.red("That is not a valid menu option, please try again.\n"))
        time.sleep(1)
        pokemon_menu(pokemon_details)

def deposit_pc(party):
    """deposits a current pokemon from the party into the PC"""

    puts(colored.blue(f"Your current Party: {party}\n"))
    deposit = input("Select the party number of the pokemon you wish to deposit.\n")

    pokemon = 0
    for pokemon in range(len(party)):
        if pokemon == int(deposit):
            pokemon_pc.append(party[pokemon])
            time.sleep(1)
            puts(colored.blue(f"{party[pokemon]} has been deposited into your PC."))
            party.pop(pokemon)
            print("\n")
            pokemon += 1


def withdraw_pc(pokemon_pc):
    """withdraws a pokemon from the pc and puts it into the party"""

    puts(colored.blue(f"{pokemon_pc}"))
    print("\n")
    if len(party) >= 6:
        puts(colored.red("Your party is full, please deposit a pokemon before continuing.\n"))
        access_pc(pokemon_pc)
    
    withdraw = input("Please select the number of the Pokemon you want to withdraw.\n")
    idx = 0
    for idx in range(len(pokemon_pc)):
        if idx == int(withdraw):
            party.append(pokemon_pc[idx])
            puts(colored.blue(f"{pokemon_pc[idx]} has been withdrawn from the PC."))
            pokemon_pc.pop(idx)

    print("\n")
    time.sleep(1)
    access_pc(pokemon_pc)

def access_pc(pokemon_pc):
    """creates the PC menu"""

    pc_input = input("Welcome to the Pokemon PC!\n Select 1 to View the Pokemon in your PC\n Select 2 to Deposit a Pokemon\n Select 3 to Withdraw a Pokemon\n Select 4 to Return to the Main Menu\n")

    if pc_input == "1":
        if len(pokemon_pc) < 1:
            puts(colored.blue("Your PC is empty.\n"))
            time.sleep(1)
            access_pc(pokemon_pc)

        else:
            puts(colored.blue(f"Here are the pokemon currently stored in your PC:\n{pokemon_pc}"))
            print("\n")
            time.sleep(1)
            access_pc(pokemon_pc) 

    elif pc_input == "2":
        deposit_pc(party)
        access_pc(pokemon_pc)

    elif pc_input == "3":
        withdraw_pc(pokemon_pc)
    
    elif pc_input == "4":
        returning()
        returning()
        print("\n")
        default_menu()
    
    else:
        puts(colored.red("That is not a valid input selection, please try again."))
        access_pc(pokemon_pc)

def view_party(party):
    """Returns the party of the current player"""

    if len(party) < 1:
        puts(colored.green("Your Party is empty. Catch some Pokemon!\n"))
        time.sleep(1)
        default_menu()

    else:
        puts(colored.green(f"Your Party is:\n{party}"))
        print("\n")
        time.sleep(1)
        default_menu()

def default_menu():
    """Creates the default menu for the CLI"""

    menu_selection = input("PokePicker Main Menu:\n Select 1 to Catch a New Pokemon!\n Select 2 to View Your Current Party\n Select 3 to Access the Pokemon PC\n Select 4 to Exit the PokePicker\n")

    while menu_selection is not None:

        if menu_selection == "1":
            print("\n")
            catching()
            catching()
            puts(colored.green("Pokemon Caught Successfully!"))
            print("\n")
            get_pokemon()
        
        elif menu_selection == "2":
            view_party(party)
            print("\n")
        
        elif menu_selection == "3":
            logging_in()
            logging_in()
            puts(colored.blue("Log in Successful!"))
            print("\n")
            access_pc(pokemon_pc)

        elif menu_selection == "4": 
            time.sleep(1)
            exit_font = Figlet(font='standard', width = 200)
            goodbye = exit_font.renderText("Goodbye!")
            puts(colored.yellow(goodbye))
            print("\n")
            exit()

        else:
            time.sleep(1)
            puts(colored.red("That is not a vaild menu option, please try again.\n"))
            default_menu()

def main():

    title_font = Figlet(font='standard', width = 250)
    title = title_font.renderText("Welcome to the PokePicker!")
    puts(colored.yellow(title))

    with indent(20):
        puts(colored.green("A CLI tool that simulates a Pokemon Catching Game! Follow the CLI prompts to play!\n"))
        puts(colored.green("You will be able to:"))
        puts(colored.green(">>> Catch a Random Pokemon!"))
        puts(colored.green(">>> Navigate your Pokemon PC!"))
        puts(colored.green(">>> Customize your Team!"))
        puts(colored.green(">>> Get Details on each Pokemon you Catch!"))

        print("\n")
        default_menu()
    

if __name__ == "__main__":
    main()