import os
import json
from world import start_level


def display_mainmenu():
    print("=== Welcome to the RPG! ===")
    print("1. Create Character")
    print("2. Load Character")
    print("3. Start Game")
    print("4. Exit")
    print("============================")

def start_game(character_file):
    print(f"Starting game with {character_file} loaded.")
    start_level(character_file)

def create_character():
    filename = input("Enter the name of the save:")
    filename+= '.json'
    character_creation(filename)

    print("creating new character...")


def character_creation(filename):
    name = input("Enter your character's name:")

    with open('classes.json', "r") as json_file:
        classes = json.load(json_file)
    
    print("Available Classes:")
    for class_data in classes:
        print(f"pos:{class_data['pos']}, name:{class_data['name']}, Health: {class_data['health']}, Mana:{class_data['mana']}")
        print(f"Attacks: {', '.join([attack['name'] for attack in class_data['attacks']])}")


    class_selection = input("Please select a class from the list(1, 2, 3): ")

    selected_class = next((cls for cls in classes if cls['pos'] == class_selection), None)

    if selected_class: #character dictionary
        character = {
            "pos": selected_class['pos'],
            "name": name,
            "class": selected_class['name'],
            "health": selected_class['health'],
            "mana": selected_class['mana'],
            "attacks": selected_class['attacks']
        }

    save_character_to_file(filename, character)



def save_character_to_file(filename, character):
    with open(filename,"w") as json_file:
        json.dump(character, json_file, indent=2)
    print(f"Character saved to'{filename}'.")

def load_character(filename):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file) #loading data
            return data
    except FileNotFoundError:
         print(f"The file '{filename}' was not found")


