import json
#the fuckin problem - circular import


def handle_battle(attacks):
    result = battle(attacks)
    if result == "won":
        print("Moving to next scene!")
        next_state()  # Call the function to move to the next part of the game
    else:
        print("Battle ended.")

def next_state(character_file):
    from world import level1
    # Load the player's current state
    with open(character_file, 'r+') as save_file:
        save_data = json.load(save_file)
        
        save_data['state_number'] += 1

        #increment game state
        current_state = save_data['state_number']
    #test print remove later
    print(f"You're now moving from state {current_state} to the next part of the game.")

    # Save the updated state back to the save file
    with open(character_file, 'w') as save_file:
        json.dump(save_data, save_file)

    # Load the new scene based on the updated state
    level1(character_file)

