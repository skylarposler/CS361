# CS361
Repository for CS361 - Software Engineering 1 at OSU


Microservice Portion - Must have the PokePicker running on your local machine <br>
** This microservice utilizes this json file: https://github.com/Purukitto/pokemon-data.json and it must be saved on your local PC

# Requesting Data:

Step 1. Make sure you're in the same directory as the pokepicker file and the pokemon-data.json <br>
Step 2. Run pokepicker.py - the get_pokemon_micro is the specific function for the microservice <br>
Step 3. Be sure to enter the correct path for the text file <br>

Example Call:

    def run_microservice():
      """runs the microservice"""
      
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
      

# Recieving Data:

Step 1. After request is written in the microservice.txt file, the function above will overwrite it with a random pokemon name <br>
Step 2. The pokemon name will be returned and available to be used at will. <br>

# UML Diagram
![image](https://github.com/skylarposler/CS361/assets/102645867/42545b8c-d9b4-4b78-aefb-0f8b3a20da6a)

