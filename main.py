import csv
def animals_lookup():
    animal_to_lookup=input("What animals are you looking for? Ex: \"cats,dogs?\": ")
    try: 
        selected_file = open(f'week2/csv-reader/data/{animal_to_lookup}.csv', mode='r')
        user_input=True
    except:
        print(f'Sorry we don\'t have {animal_to_lookup} at our rescue Shelter')
        user_input=False
    
    if user_input:
        dict=csv.DictReader(selected_file)
        print(f'Here are the {animal_to_lookup} we have for adoption')
        for row in dict:
            print(f'{row["name"]} is a {row[" age"]} year old {row[" breed"]}')

print(animals_lookup())

