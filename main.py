from character import Character
from utils import load_characters, save_characters
from events import random_event

def main():
    characters = load_characters()
    
    while True:
        print("Welcome to VirtuaLife!")
        print("1. Create Character")
        print("2. Load Character")
        print("3. Exit")
        print("4. whoami")
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter character name: ")
            age = int(input("Enter character age: "))
            traits = input("Enter initial traits (comma separated): ").split(',')
            character = Character(name, age, traits)
            characters.append(character)
            save_characters(characters)
            print(f"Character {name} created successfully!")
        
        elif choice == '2':
            if not characters:
                print("No characters found. Create a new character first.")
                continue
            
      
            
            print("Available characters:")
            for idx, char in enumerate(characters):
                print(f"{idx + 1}. {char.name}")
            char_idx = int(input("Select a character: ")) - 1
            character = characters[char_idx]
            print(f"Character {character.name} loaded successfully!")
            
            while True:
                print(f"{character.name} is {character.age} years old.")
                print("1. Progress Life")
                print("2. View Character Stats")
                print("3. Interact with Character")
                print("4. Edit Character")
                print("5. Save and Exit")
                print("6. whoami")
                choice = input("Choose an option: ")

                if choice == '1':
                    progress_life(character, characters)
                    character.age += 1
                    save_characters(characters)
                elif choice == '2':
                    print(character)
                elif choice == '3':
                    character.interact()
                elif choice == '4':
                    edit_character(character)
                    save_characters(characters)
                elif choice == '5':
                    save_characters(characters)
                    print("Progress saved. Exiting VirtuaLife.")
                    
                elif choice == '6':
                   print("A virtual life simulation developed by Awortu Ibenem")
            break

        elif choice == '3':
            print("Exiting VirtuaLife. Goodbye!")
            break
        
        elif choice == '4':
                print("A virtual life simulation developed by Awortu Ibenem")
                continue

def progress_life(character, characters):
    event = random_event(character)
    print(f"{character.name} {event['description']} and gained {event['experience']} experience.")

def edit_character(character):
    name = input(f"Enter new name (current: {character.name}): ")
    if name:
        character.name = name
    age = input(f"Enter new age (current: {character.age}): ")
    if age:
        character.age = int(age)
    traits = input(f"Enter new traits (current: {','.join(character.traits)}): ").split(',')
    if traits:
        character.traits = traits
    print("Character updated successfully!")

if __name__ == "__main__":
    main()
