import os
import sys
import json
from battle import battle

def display_actionmenu():
    print("=== Welcome to the world! ===")
    print("1. Survey Surroundings")
    print("2. Check Status")
    print("3. Check Inventory")
    print("4. Move")
    print("5. Exit")
    print("============================")

def start_level(character_file):
    with open(character_file, 'r') as char_file:  # Getting attack data from save
        character_data = json.load(char_file)  # Correct the variable name to character_data
        attacks = character_data['attacks']  # Use character_data instead of character_file

    print("Welcome to the land of Camelot. There are many adventures to be had, but for now let's teach you how to battle!")
    battle(attacks)
