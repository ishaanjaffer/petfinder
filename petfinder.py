from pets import *

'''
Petfinder program
'''

# Main method for program execution
def main():
    pets = []
    # Load pets.csv file
    for line in open('pets.csv'):
        params = [term.strip() for term in line.split(",") if len(term) > 0]
        if '' in params:
            params.remove('')
        if params[0].lower() == 'fish' and len(params) == 5:
            pets.append(Fish(params[1], params[2], params[3], params[4]))
        elif params[0].lower() == 'cat' and len(params) == 5:
            pets.append(Cat(params[1], params[2], params[3], params[4]))
        elif params[0].lower() == 'dog' and len(params) == 5:
            pets.append(Dog(params[1], params[2], params[3], params[4]))
        elif params[0].lower() == 'bird' and len(params) == 5:
            pets.append(Bird(params[1], params[2], params[3], params[4]))
    # Print menu in a loop
    while True:
        print("Menu:")
        print("  1. Show pet names")
        print("  2. Search for pet")
        print("  3. Show list")
        print("  4. Show pets of a certain type")
        print("  5. Exit")
        # Get user input
        while True:
            choice = input("Enter choice: ")
            # Choice 1: show pet names
            if choice == '1':
                for pet in pets:
                    print(pet.getName())
                break
            # Choice 2: search for pet
            elif choice == '2':
                name = input("Enter name of pet: ")
                found = False
                for index in range(len(pets)):
                    pet = pets[index]
                    if pet.getName().lower() == name.lower():
                        found = True
                        print("Found at index " + str(index) + ":")
                        print(pet)
                if found == False:
                    print("There are no pets with name " + name + " found in the list.")
                break
            # Choice 3: show list
            elif choice == '3':
                for pet in pets:
                    print(pet)
                break
            # Choice 4: show pets of a certain type
            elif choice == '4':
                petType = input("Enter type of pet: ")
                found = False
                for pet in pets:
                    if petType.lower() == 'fish' and type(pet) is Fish:
                        found = True
                        print(pet)
                    elif petType.lower() == 'cat' and type(pet) is Cat:
                        found = True
                        print(pet)
                    elif petType.lower() == 'dog' and type(pet) is Dog:
                        found = True
                        print(pet)
                    elif petType.lower() == 'bird' and type(pet) is Bird:
                        found = True
                        print(pet)
                if found == False:
                    print("There are no pets of type " + type + " found in the list.")
                break
            # Choice 5: exit
            elif choice == '5':
                return
            # Else, invalid input
            else:
                print("Error: Invalid input. Please try again!")
                break

# Run main method on program execution
if __name__ == "__main__":
    main()