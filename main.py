def animals_lookup():
    animal_to_lookup=input("What animals are you looking for? Ex: \"cats,dogs?\": ")
    try: 
        f = open(f'week2/csv-reader/data/{animal_to_lookup}.csv', mode='r')
        user_input=True
    except:
        print(f'Sorry we don\'t have {animal_to_lookup} at our rescue Shelter')
        user_input=False
    if user_input:
        print(f.read())
        f.close()
print(animals_lookup())

