# Define a dictionary that holds our pet's attributes.
from small_treat import SmallTreat
from medium_treat import MediumTreat
from large_treat import LargeTreat
from toy import Toy
from cuddly_pet import CuddlyPet
from pet import Pet

pet_name = input("What is your pet's name: ")
pet_type = int(input('''
1. Pet
2. Cuddly Pet
'''))
if pet_type == 1:
    pet = Pet(pet_name)
elif pet_type == 2:
    pet = CuddlyPet(pet_name)

# Prompt the user to interact with the pet
while True:
    print(pet.get_status())
    print('''
    0. Do nothing
    1. Feed Pet
    2. Play with pet
    3. Give Toy
    4. Give a Treat
    ''')
    choice = int(input(': '))
    if choice == 1:
        #feed the pet
        pet.eat_food()
    elif choice == 2:
        #play with the pet
        pet.get_love()
    elif choice == 3:
        #give toy to pet
        pet.give_toy(Toy())
    elif choice == 4:
        print('''''
        1. Small Treat
        2. Medium Treat
        3. Large Treat
        ''')
        treat_type = int(input(": "))
        if treat_type == 1:
            pet.give_small_treat(SmallTreat())
        elif treat_type == 2:
            pet.give_medium_treat(MediumTreat())
        elif treat_type == 3:
            pet.give_large_treat(LargeTreat())
        
         
    # Each time the loop runs, the pet will need some attention!
    pet.being_alive()
    #show the pet has passed away if their stats reach 0
    if not pet.is_alive():
        print(pet.get_status())
        print(f"R.I.P {pet.name}")
        break