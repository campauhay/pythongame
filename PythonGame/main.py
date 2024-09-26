import json
import os
import sys
from utils import display_mainmenu, create_character, load_character, start_game

character_loaded = False
loaded_filename = None

def main():
    global character_loaded, loaded_filename
    while True:
        display_mainmenu()
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            create_character()
        elif choice == '2':
            filename = input("Please enter save file name: ")
            filename+= '.json'
            load_character(filename)
            loaded_filename = filename
            character_loaded = True
        elif choice == '3':
            if character_loaded:
                start_game(loaded_filename)
        elif choice == '4':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()