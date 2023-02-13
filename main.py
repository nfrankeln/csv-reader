import csv
import os

def animals_lookup():
    # set up infinite loop to collect input with a way to exit the loop 
    while True:
        animal_to_lookup=input("(Press 'x' to exit ) \n What animals are you looking for? Ex: \"cats,dogs?\": ")
        if animal_to_lookup == "x":
            break
        try:
            #here we are creating a file path to our csv files. getcwd() returns what entering pwd in the terminal 
            #if said file path doesnt exist the try block will fail and user input will be set to false 
            data_folder = 'data'
            file_path = os.path.join(os.getcwd(), data_folder, f'{animal_to_lookup}.csv')
            selected_file = open( file_path, mode='r')
            user_input=True
        except:
            print(f'Sorry we don\'t have {animal_to_lookup} at our rescue Shelter')
            user_input=False
        
        if user_input:
            # skipinitialspace removes leading whitespace without it you need to parse your headers and strip whitespace
            # or call your dictionary with whitespace ex " age" " breed"
            dict = csv.DictReader(selected_file, skipinitialspace=True)
            print(f'Here are the {animal_to_lookup} we have for adoption')
            for animal in dict:
                print(f'{animal["name"]} is a {animal["age"]} year old {animal["breed"]}')
            selected_file.close()
    print("Goodbye")
    

print(animals_lookup())

