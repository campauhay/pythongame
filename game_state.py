from world import start_level
from battle import battle

def handle_battle(attacks):
    result = battle(attacks)
    if result == "won":
        print("Moving to next scene!")
        next_scene()  # Call the function to move to the next part of the game
    else:
        print("Battle ended.")

def next_scene():
    print("You're now moving to the next part of the game.")
    # Here we could load a new level, have a new interaction, etc.
    start_level()